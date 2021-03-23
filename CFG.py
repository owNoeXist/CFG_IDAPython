import copy
import collections
import json
import networkx as nx

from idc import *
from idaapi import *
from idautils import *
from Instruction import x86_I,MIPS_I

#=================================CFG=====================================
#Generate CFG data
def GenerateCFG(FUNCTION,SIGN):
    cfg = nx.DiGraph()
    #obtain basic block
    basicBlock = [(v.startEA, v.endEA) for v in FlowChart(FUNCTION)]

    #Generate basic block 
    for bb in basicBlock:
        #ignore blank block that IDA pro generated
        if bb[0]!=bb[1]:
            nodeId = len(cfg)
            cfg.add_node(nodeId)
            cfg.node[nodeId]['startEA'] = bb[0]
            cfg.node[nodeId]['endEA'] = bb[1]
    if len(cfg) == 1:
        return cfg
    
    #Generate cfg
    for destNode in range(len(cfg)):
        refs = CodeRefsTo(cfg.node[destNode]['startEA'], 1)
        for ref in refs:
            for srcNode in range(len(cfg)):
                if cfg.node[srcNode]['startEA']<= ref < cfg.node[srcNode]['endEA']:
                    cfg.add_edge(srcNode, destNode)
                    break

    GenerateLiteral(cfg,SIGN)
    GenerateSemantic(cfg,SIGN)

    return cfg

#==============================Code literals===============================
#Generate code literals for each BasicBlock
def GenerateLiteral(CFG,SIGN):
    for nodeId in CFG:
        bbAddr = [CFG.node[nodeId]['startEA'],CFG.node[nodeId]['endEA']]
        literals = []
        #code literals --Instruction Number
        literals.append(GetInstructNum(bbAddr,SIGN))
        #code literals --Immediate Number
        literals.append(GetImmediateNum(bbAddr,SIGN))
        #code literals --String Number
        literals.append(GetStringNum(bbAddr,SIGN))
        #code literals --Calculate
        literals.append(GetInsTypeNum(bbAddr,SIGN,2))
        #code literals --BitOperate
        literals.append(GetInsTypeNum(bbAddr,SIGN,3))
        #code literals --Call
        #literals.extend(GetCallNum(bbAddr,SIGN))
        literals.append(GetCallNum(bbAddr,SIGN))
        #code literals --Return
        literals.append(GetInsTypeNum(bbAddr,SIGN,8))
        #Add features to node
        CFG.node[nodeId]['literal']=literals

#Collect instruction number from one basic block
def GetInstructNum(BB,SIGN):
    num = 0
    instAddr = BB[0]
    while instAddr < BB[1]:
        num+=1
        instAddr = NextHead(instAddr)
    return num

#Collect immediate number from one basic block
def GetImmediateNum(BB,SIGN):
    num = 0
    instAddr = BB[0]
    if SIGN==0:
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            if opcode in ['la','jalr','call', 'jal']:
                instAddr = NextHead(instAddr)
                continue
            if opcode != 'lea':
                for offset in range(3):
                    try:
                        optype = GetOpType(instAddr, offset)
                        if optype == o_imm:
                            num+=1
                    except:
                        pass
            instAddr = NextHead(instAddr)
    elif SIGN==1:
        #Need repair
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            if opcode != 'la':
                num+=1
            instAddr = NextHead(instAddr)

    return num

#Collect string number from one basic block
def GetStringNum(BB,SIGN):
    num = 0
    instAddr = BB[0]
    if SIGN==0:
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            if opcode == 'lea':
                str_value = GetString(GetOperandValue(instAddr, 1))
                if str_value != None:
                    num+=1
            instAddr = NextHead(instAddr)
    elif SIGN==1:
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            if opcode == 'la':
                str_value = GetString(GetOperandValue(instAddr, 1))
                if str_value != None:
                    num+=1
            instAddr = NextHead(instAddr)

    return num

#Collect call number from one basic block
def GetCallNum(BB,SIGN):
    num = [0,0]
    instAddr = BB[0]
    if SIGN==0:
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            if opcode=='call':
                if SegName(GetOperandValue(instAddr,0)) == '.text':
                    num[0]+=1
                else:
                    num[1]+=1
            instAddr = NextHead(instAddr)
    elif SIGN==1:
        funcType='.text'
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            if opcode in ['jal','jalr']:
                if funcType == '.text':
                    num[0]+=1
                else:
                    num[1]+=1
            elif opcode == 'bal':
                if SegName(GetOperandValue(instAddr,0)) == '.text':
                    num[0]+=1
                else:
                    num[1]+=1
            elif opcode == 'la' and GetOpnd(instAddr,0) == '$t9':
                funcType=SegName(GetOperandValue(instAddr,1))
            instAddr = NextHead(instAddr)
    return num[0]+num[1]

#Collect Instruction number in one class from one basic block
def GetInsTypeNum(BB,SIGN,TYPE):
    num = 0
    instAddr = BB[0]
    if SIGN==0:
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            if opcode in x86_I:
                if x86_I[opcode]==TYPE:
                    num+=1
            instAddr = NextHead(instAddr)
    elif SIGN==1:
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            if opcode in MIPS_I:
                if MIPS_I[opcode]==TYPE:
                    num+=1
            instAddr = NextHead(instAddr)
    return num


#============================Semantic Sequence=============================
#Generate semantic sequence for each BasicBlock
def GenerateSemantic(CFG,SIGN):
    for nodeId in CFG:
        bbAddr = [CFG.node[nodeId]['startEA'],CFG.node[nodeId]['endEA']]
        #Exact semantic sequence from BasicBlock 
        CFG.node[nodeId]['semantic']=InstructionSequence(bbAddr,SIGN)

def InstructionSequence(BB,SIGN):
    semantic = []
    instAddr = BB[0]
    if SIGN == 0:
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            semantic.append(x86_I[opcode])
            instAddr = NextHead(instAddr)
    elif SIGN == 1:
        while instAddr < BB[1]:
            opcode = GetMnem(instAddr)
            semantic.append(MIPS_I[opcode])
            instAddr = NextHead(instAddr)
    return semantic


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