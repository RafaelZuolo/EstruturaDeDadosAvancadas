# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:26:06 2019

@author: rafae
"""
from ABBStackCorrigido import TREE

class PilhaRetro:
    def __init__(self):
        self.event = TREE()
        
    def Insert_Push(self, t, x):
        self.event.Insert(t, x, 1)
        
    def Insert_Pop(self, t):# na minha implementacao, nao pode ter data = None
        self.event.Insert(t, "void", -1)
        
    def Delete(self, t):
        self.event.Delete(t)
        
    def Query_Top(self, t):
        return self.event.LastPush(t)
        