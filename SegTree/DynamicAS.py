# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 11:19:13 2019

@author: rafae
"""

from AS import AS, Segments

class DynAS:
    def __init__(self):
#        self.count = 0
        self.treeList = [] # todas as AS montadas
        self.segs = []     # os elementos inseridos

    def DynSegments(self, x): # verificamos em cada arvore
        for i in self.treeList:
            if i is not None:
                Segments(i, x)
        print("")


    # vamos coletando os elementos das arvores e apagando elas,
    # depois ao encontrarmos uma arvore vazia, montamos ela
    def Insert(self, s):
        partSegs = [s]
#        self.count += 1
        for i in range(0, len(self.treeList)):
            if self.treeList[i] is not None:
                for j in self.segs[i]:
                    partSegs.append(j)
                self.segs[i] = None
                self.treeList[i] = None
            else:
                self.treeList[i] = AS(partSegs)
                self.segs[i] = partSegs
                return                   # recontruimos a arvore vazia
        newAS = AS(partSegs)             # extendemos "em 1 bit" com tudo vazio
        self.treeList.append(newAS)
        self.segs.append(partSegs)

dinAS = DynAS()
dinAS.Insert([1,4])
dinAS.Insert([3,6])
dinAS.Insert([7,9])
dinAS.Insert([0,11])
dinAS.Insert([-2,8])
dinAS.Insert([-1,3.33])
dinAS.Insert([2,5])
dinAS.DynSegments(3.1)   # [2, 5] [-1, 3.33] [-2, 8] [0, 11] [1, 4] [3, 6]
dinAS.DynSegments(4.5)   # [2, 5] [-2, 8] [0, 11] [3, 6]
dinAS.DynSegments(0.1)   # [-1, 3.33] [-2, 8] [0, 11]
