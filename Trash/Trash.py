#GetOpnd(inst_addr, 0)获取操作数名称
#GetOpType(ea, n)获得指令的操作类型
#GetOperandValue(ea, n)获得指令操作数的值
#GetString(imm_value)尝试直接根据该地址获取字符串

#==================================PFG=====================================
#Generate PFG
def GeneratePFG(CFG, SIGN):
    argTo=[[],[],[],[]]
    nodeNum=len(CFG)
    nodeTo = [[] for i in range(nodeNum)]
    affectPara=[[['rdi'],['rsi'],['rdx'],['rcx']],[['$a0'],['$a1'],['$a2'],['$a3']]]
    for u,v in CFG.edges():
        nodeTo[u].append(v)
    for i in range(4):
        nodeAccess=[]
        ArgSearch(CFG, SIGN, nodeTo, argTo[i], nodeAccess, affectPara[SIGN][i], 0)
    CFG.graph['pfg']=argTo

def ArgSearch(CFG, SIGN, NODE_TO, ARG_TO, NODE_ACCESS, AFFECT_PARA, NODE_NOW):
    affectPara=[]
    affectPara.extend(AFFECT_PARA)
    #Search data affected by arg
    instAddr = CFG.node[NODE_NOW]['startEA']
    if SIGN==0:
        while instAddr < CFG.node[NODE_NOW]['endEA']:
            op0=GetOpnd(instAddr, 0)
            op1=GetOpnd(instAddr, 1)
            op2=GetOpnd(instAddr, 2)
            if op0 in affectPara and op1 != '':
                affectPara.remove(op0)
            if op1 in affectPara:
                if NODE_NOW not in ARG_TO:
                    ARG_TO.append(NODE_NOW)
                affectPara.append(op0)
            if op2 in affectPara:
                if NODE_NOW not in ARG_TO:
                    ARG_TO.append(NODE_NOW)
                affectPara.append(op0)
            instAddr = NextHead(instAddr)
    elif SIGN==1:
        while instAddr < CFG.node[NODE_NOW]['endEA']:
            op0=GetOpnd(instAddr, 0)
            op1=GetOpnd(instAddr, 1)
            op2=GetOpnd(instAddr, 2)
            if op2 != '':
                if op2 in affectPara:
                    affectPara.remove(op2)
                if op1 in affectPara:
                    if NODE_NOW not in ARG_TO:
                        ARG_TO.append(NODE_NOW)
                    affectPara.append(op2)  
                if op0 in affectPara:
                    if NODE_NOW not in ARG_TO:
                        ARG_TO.append(NODE_NOW)
                    affectPara.append(op2)
            elif op1!= '':
                if op1 in affectPara:
                    affectPara.remove(op1)
                if op0 in affectPara:
                    if NODE_NOW not in ARG_TO:
                        ARG_TO.append(NODE_NOW)
                    affectPara.append(op1)
            instAddr = NextHead(instAddr)
    #Search next node
    for nodeNext in NODE_TO[NODE_NOW]:
        if nodeNext in NODE_ACCESS:
            continue
        else:
            NODE_ACCESS.append(nodeNext)
            ArgSearch(CFG, SIGN, NODE_TO, ARG_TO, NODE_ACCESS, affectPara, nodeNext)


def NodeFold(PCFG):
    for nodeId in range(1,len(PCFG)):
        #CheckNode
        if PCFG.node[nodeId]['literal'][0] <= 4 and PCFG.has_edge(nodeId-1,i):
            if PCFG.out_degree(nodeId)==2 and PCFG.out_degree(nodeId-1)==2:
                for j in range(GRAPH['Nodenum']):
                    if i in GRAPH['NodeTo'][j] and j!=i-1:
                        break
                if j != GRAPH['Nodenum']:
                    i+=1
                    continue
                sameNode = [x for x in GRAPH['NodeTo'][i-1] if x in GRAPH['NodeTo'][i]]
                if sameNode is None:
                    continue
            else:
                continue
        else:        
            continue
        #DeleteNode
        for j in range(len(GRAPH['NodeFeature'][0])):
            GRAPH['NodeFeature'][i-1][j]+=GRAPH['NodeFeature'][i][j]
        del GRAPH['NodeFeature'][i]
        for j in range(2):
            GRAPH['NodeTo'][i-1][j]=GRAPH['NodeTo'][i][j]
        del GRAPH['NodeTo'][i]
        GRAPH['Nodenum']-=1
        for j in range(GRAPH['Nodenum']):
            for k in range(len(GRAPH['NodeTo'][j])):
                if GRAPH['NodeTo'][j][k] > i:
                    GRAPH['NodeTo'][j][k]-=1


'''
for seg in Segments():
        if SegName(seg) == '.MIPS.stubs':
            sign=1
''' 