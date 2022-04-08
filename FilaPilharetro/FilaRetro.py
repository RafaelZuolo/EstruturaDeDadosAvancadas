# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:41:42 2019

@author: rafae
"""

# fila parcialmente retro
#import ABBQueue
from ABBQueueCorrigido import TREE


class FilaRetro:
    def __init__(self):
        self.enq = TREE()
        self.deq = TREE()

    def Insert_Enqueue(self, t, x):
        self.enq.Insert(t, x)

    def Delete_Enqueue(self, t):
        self.enq.Delete(t)

    def Insert_Dequeue(self, t):
        self.deq.Insert(t, -1)

    def Delete_Dequeue(self, t):
        self.deq.Delete(t)

    def Query_Kth(self, t, k):
        l = self.deq.Count(t)
        print("o valor de l eh:", l)
        return self.enq.Kth(k + l)

    def Query_First(self, t):
        return self.Query_Kth(t, 1)
