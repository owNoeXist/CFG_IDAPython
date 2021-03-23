import collections
import networkx as nx

from idc import *
from idaapi import *
from idautils import *

def GenerateJson(FUNC_NAME, CFG):
    rawData = raw_graph(FUNC_NAME, CFG)
    data = collections.OrderedDict()
    data["Funcname"] = rawData.funcName
    data["Nodenum"] = rawData.nodeNum
    data["CFG"] = rawData.cfg
    data["Literal"]=rawData.literal
    data["Semantic"]=rawData.semantic
    return data

#The cfg date of one function
class raw_graph:
    def __init__(self, FUNC_NAME, CFG):
        self.funcName = FUNC_NAME
        self.nodeNum = len(CFG)
        self.cfg = self.__GenerateCFG(CFG)
        self.literal = self.__GenerateLiteral(CFG)
        self.semantic = self.__GenerateSemantic(CFG)

    def __GenerateCFG(self,CFG):
        cfg = [[] for i in range(self.nodeNum)]
        for u,v in CFG.edges():
            cfg[u].append(v)
        return cfg

    def __GenerateLiteral(self,CFG):
        literal = []
        for i in range(len(CFG)):
            literal.append(CFG.node[i]['literal'])
        return literal

    def __GenerateSemantic(self,CFG):
        semantic = []
        for i in range(len(CFG)):
            semantic.append(CFG.node[i]['semantic'])
        return semantic