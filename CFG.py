import copy
import collections
import json
import networkx as nx

from idc import *
from idaapi import *
from idautils import *
from Instruction import x86_I,MIPS_I

#=================================CFG Function=====================================
#Generate transfer cfg data to vector and add some attribution
def GenerateCFG(FUNC,SIGN):
    cfg = nx.DiGraph()
    #obtain basic block information
    basicBlock = [(v.startEA, v.endEA) for v in FlowChart(FUNC)]

    #Generate node information 
    for bb in basicBlock:
    #ignore blank block that IDA pro generated
        if bb[0]!=bb[1]:
            nodeId = len(cfg)
            cfg.add_node(nodeId)
            cfg.node[nodeId]['startEA'] = bb[0]
            cfg.node[nodeId]['endEA'] = bb[1]
    if len(cfg) == 1:
        return cfg

    #Generate edge information
    for destNode in range(len(cfg)):
        refs = CodeRefsTo(cfg.node[destNode]['startEA'], 1)
        for ref in refs:
            for srcNode in range(len(cfg)):
                if cfg.node[srcNode]['startEA']<= ref < cfg.node[srcNode]['endEA']:
                    cfg.add_edge(srcNode, destNode)
                    break

    #Generate nodeword information
    GenerateWords(cfg,SIGN)

    return cfg


#=================================Words Function=====================================
#Generate nodes' word-feature in CFG
def GenerateWords(CFG,SIGN):
    for nodeId in CFG:
        bl=[CFG.node[nodeId]['startEA'],CFG.node[nodeId]['endEA']]
        #Transfer instruction to words
        words=NodeWords(bl)
        #Add words to node
        CFG.node[nodeId]['words']=words

def NodeWords(BL):
    start = BL[0]
    end = BL[1]
    words=[]
    instAddr = start
    while instAddr < end:
        lines=[]
        opcode = GetMnem(instAddr)
        lines.append(StringEncode(opcode))
        for i in range(3):
            string=GetOpnd(instAddr, i)
            if string=="":
                break
            lines.append(StringEncode(string))
        words.append([])
        words[-1]=lines
        instAddr = NextHead(instAddr)
    return words

def StringEncode(string):
    num=[0,0,0]
    for i in range(len(string)):
        if ord('A')<=ord(string[i])<=ord('Z'):
            temp=ord(string[i])-ord('A')+1
        elif ord('a')<=ord(string[i])<=ord('z'):
            temp=ord(string[i])-ord('a')+1
        else:
            temp=0
        num[0]+=temp/9
        num[1]+=(temp/3)%3
        num[2]+=temp%3
    temp=(num[0]%10)*100+(num[1]%10)*10+(num[2]%10)
    return temp


#=================================Other Function=======================================
#Obtain the function name from EA
def get_unified_funcname(EA):
    funcName = GetFunctionName(EA)
    if len(funcName) > 0:
        if '.' == funcName[0]:
            funcName = funcName[1:]
    return funcName

#Check one function whether has other instruction not in x86_I or MIPS_I 
def CheckInstruct(FUNC,SIGN):
    start=FUNC.startEA
    end=FUNC.endEA
    instAddr=start
    addr=list(FuncItems(start))
    if SIGN==0:
        for instAddr in addr:
            opcode = GetMnem(instAddr)
            if opcode not in x86_I:
                return 1
    elif SIGN==1:
        for instAddr in addr:
            opcode = GetMnem(instAddr)
            if opcode not in MIPS_I:
                return 1
    return 0
'''
for seg in Segments():
        if SegName(seg) == '.MIPS.stubs':
            sign=1
'''