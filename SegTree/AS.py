# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 07:54:20 2019

@author: rafael
"""
# se o ponto é o da extremidade, pode dar xabu
# Usar Set do python?
# evitar impressão repetida

from ABBSegTree import TREE
# OS SEGMENTOS DEVEM SER TUPLAS
inf = float('inf')
segs = [(1, 3),(2, 5),(4, 9),(6, 8),(0,10)]
segs2 = [(1, 3),(2, 5),(4, 9),(6, 8),(0,10), (5,6), (4,8)]


class AS:
    def __init__(self, segList):
        elements = elemSort(segList) # quebra os segmentos em elementares
        self.segTree = TREE()
        for i in elements:
            self.segTree.Insert(i[0], i)
        self.segTree.ProcessList(segList) # depois de montada a arvore, procesamos

def elemSort(segList):  # retorna os segmentos elementares
        elements = []
        conjunto = set()
        for i in segList:# arrumar as repetiçoes
            conjunto.add(i[0])
            conjunto.add(i[1])
        for i in conjunto:
            elements.append(i)
        elements.sort()
        elemSeg = [[-inf, elements[0]]] # comecamos a montar o vetor de segs elem
        for i in range(0, len(elements) -1):
            elemSeg.append([elements[i], elements[i + 1] ])
        elemSeg.append([elements[len(elements) - 1], inf])
        return elemSeg

def Segments(aSeg, x):
    aSeg.segTree.IntervalSearchCall(x)


st = AS(segs2)
print("\n\n\n\n")
#st.segTree.ColorPrint()
Segments(st, 3)