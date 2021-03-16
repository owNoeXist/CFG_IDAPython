import collections
import networkx as nx

from idc import *
from idaapi import *
from idautils import *

def GenerateJson(FUNC_NAME, FUNC_C, SIGN):
    rawData=raw_graph(FUNC_NAME, FUNC_C, SIGN)
    data=collections.OrderedDict()
    data["Funcname"]=rawData.funcName
    data["Nodenum"]=rawData.nodeNum
    data["NodeTo"]=rawData.nodeTo
    data["NodeWords"]=rawData.words
    return data

#The cfg date of one function
class raw_graph:
    def __init__(self, FUNC_NAME, CFG, SIGN):
        self.funcName = FUNC_NAME
        self.nodeNum = len(CFG)
        self.nodeTo = self.__GenerateEdge(CFG)
        self.words = self.__GenerateWords(CFG)

    def __GenerateEdge(self,CFG):
        lists = [[] for i in range(self.nodeNum)]
        for u,v in CFG.edges():
            lists[u].append(v)
        return lists

    def __GenerateWords(self,CFG):
        lists = []
        for i in range(len(CFG)):
            lists.append(CFG.node[i]['words'])
        return lists
        