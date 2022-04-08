# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:07:41 2019

@author: rafae
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 10 07:48:27 2019

@author: rafael
"""
import QnowTeste as Qnow
import U2_Copia_QUE_FUNCIONOU as U
inf = float("inf")

class HeapRetro:
    def __init__(self):
        self.qnow = Qnow.TREE()     # heap atual
        self.u = U.TREE()

    def Insert_insert(self, t, k):
        if self.u.root is self.u.NIL:
            self.u.Insert(t, k, 0)
            self.qnow.Insert(k, t)
        else:
            preTupla = self.u.FindBigKeyAfterBridge(t, False)
            if preTupla[0] > k:#atualiza o noh que vai ser inserido em qNow
                nodeIn = self.u.Search(preTupla[1])[0]
                nodeIn.maxSum = nodeIn.minSum = nodeIn.subSum = 0
                nodeIn.maxNotQ = (-inf, nodeIn.key)
                self.u.UpFix(nodeIn.p)
                self.qnow.Insert(preTupla[0], preTupla[1])
                nodeIn.minInQ = (nodeIn.data, nodeIn.key)
                self.u.Insert(t, k, +1)
            else:
                self.u.Insert(t, k, 0)
                self.qnow.Insert(k, t)

    def Insert_delMin(self, t):
        kNow = self.u.KeyToRemove(t)
        self.u.Insert(t, -inf, -1)
        self.qnow.Delete(kNow)

    def Delete_insert(self, t):
        x = self.u.Search(t)[0]
        if x.data is self.qnow.Search(x.data).key:
            self.u.Delete(t)
            self.qnow.Delete(x.data)
        else:
            kNow = self.u.KeyToRemove(t)
            self.u.Delete(t)
            self.qnow.Delete(kNow)

    def Delete_delMin(self, t):
        kNow = self.u.KeyToInsert(t, True)
        self.u.Delete(t)
        self.qnow.Insert(kNow, t)

def Query_Min(h):
    print(h.qnow.ABBminKey())

def Print(h):
    h.qnow.Print()

def PrintU(h):
    h.u.Print()

# parsing
h = HeapRetro()
#h.Insert_insert(6,20)
#h.Insert_insert(7,10)
#h.Insert_insert(8,50)
#Print(h)
#
#h.Insert_delMin(9)
#Print(h)
#h.Insert_insert(0,30)
#print("hhhm")
#Print(h)
#print("woot?")
#h.Insert_insert(1,40)
#Print(h)
#
#h.Insert_delMin(2)
#
#Print(h)
#
#h.Insert_insert(3,90)
#Print(h)
#
#h.Insert_insert(4,70)
#Print(h)
#
#h.Insert_delMin(5)
#print("h eh:")
#
#Print(h)
#h.u.Print()
#h.Insert_delMin(10)
#Print(h)
#h.Insert_delMin(11)
#h.Insert_insert(12,35)
#Print(h)                # 35 70 90
#h.Insert_insert(1.5, 150)
#Print(h)
#h.Insert_insert(1.7, 15)
#Print(h)
#h.Insert_insert(-1, -10)
#Print(h)
# #----------------------------------------------------------------
h.Insert_insert(1,1)
print("H eh", end = ' ')
Print(h)
h.Insert_insert(2,2)
print("H eh", end = ' ')
Print(h)
h.Insert_insert(3,3)
print("H eh", end = ' ')
Print(h)
h.Insert_delMin(4)
print("H eh", end = ' ')
Print(h)
h.Insert_delMin(5)
print("H eh", end = ' ')
Print(h)
h.Insert_delMin(6)
print("H eh", end = ' ')
Print(h)
h.Insert_insert(7,7)
print("H eh", end = ' ')
Print(h)
h.Insert_delMin(8)
print("H eh", end = ' ')
Print(h)
h.Insert_insert(9,0.5)
print("H eh", end = ' ')
Print(h)
h.Delete_delMin(6)
print("H dps do del eh", end = ' ')
Print(h)
h.Delete_delMin(5)
print("H dps do del eh", end = ' ')
Print(h)
h.Delete_delMin(4)
print("H dps do del eh", end = ' ')
Print(h)
h.Delete_delMin(8)
print("H dps do del eh", end = ' ')
Print(h)
h.Delete_insert(7)
print("H dps do rem eh", end = ' ')
Print(h)
h.Delete_insert(9)
print("H dps do rem eh", end = ' ')
Print(h)
# #--------------------------------------------------------
#h.Insert_insert(1,1)
#print("H eh", end = ' ')
#Print(h)
#h.Insert_insert(2,2)
#print("H eh", end = ' ')
#Print(h)
#h.Insert_insert(3,3)
#print("H eh", end = ' ')
#Print(h)
#h.Insert_insert(4,0)
#print("H eh", end = ' ')
#Print(h)
#h.Insert_insert(5,-1)
#print("H eh", end = ' ')
#Print(h)
#h.Insert_delMin(6)
#print("H eh dps do DelMin", end = ' ')
#Print(h)
#h.Insert_delMin(7)
#print("H eh dps do DelMin", end = ' ')
#Print(h)
#h.Insert_delMin(8)
#print("H eh dps do DelMin", end = ' ')
#Print(h)
#h.Insert_delMin(9)
#print("H eh dps do DelMin", end = ' ')
#Print(h)
#h.Insert_delMin(10)
#print("H eh dps do DelMin", end = ' ')
#Print(h)
#h.Delete_delMin(10)
#print("H eh dps do Rem", end = ' ')
#Print(h)
#h.Delete_delMin(9)
#print("H eh dps do Rem", end = ' ')
#Print(h)
#h.Delete_delMin(8)
#print("H eh dps do Rem", end = ' ')
#Print(h)
#h.Delete_delMin(7)
#print("H eh dps do Rem", end = ' ')
#Print(h)
#h.Delete_delMin(6)
#print("H eh dps do Rem", end = ' ')
#Print(h)


