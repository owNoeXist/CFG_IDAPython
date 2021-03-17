import collections
import networkx as nx

from idc import *
from idaapi import *
from idautils import *

def GenerateJson(FUNC_NAME, PCFG):
    rawData = raw_graph(FUNC_NAME, PCFG)
    data = collections.OrderedDict()
    data["Funcname"] = rawData.funcName
    data["Nodenum"] = rawData.nodeNum
    data["CFG"] = rawData.cfg
    data["PFG"] = rawData.pfg
    data["Literal"]=rawData.literal
    data["Semantic"]=rawData.semantic
    return data

#The pcfg date of one function
class raw_graph:
    def __init__(self, FUNC_NAME, PCFG):
        self.funcName = FUNC_NAME
        self.nodeNum = len(PCFG)
        self.cfg = self.__GenerateCFG(PCFG)
        self.pfg = self.__GeneratePFG(PCFG)
        self.literal = self.__GenerateLiteral(PCFG)
        self.semantic = self.__GenerateSemantic(PCFG)

    def __GenerateCFG(self,PCFG):
        cfg = [[] for i in range(self.nodeNum)]
        for u,v in PCFG.edges():
            cfg[u].append(v)
        return cfg

    def __GeneratePFG(self,PCFG):
        pfg = PCFG.graph['pfg']
        return pfg

    def __GenerateLiteral(self,PCFG):
        literal = []
        for i in range(len(PCFG)):
            literal.append(PCFG.node[i]['literal'])
        return literal

    def __GenerateSemantic(self,PCFG):
        semantic = []
        for i in range(len(PCFG)):
            semantic.append(PCFG.node[i]['semantic'])
        return semantic