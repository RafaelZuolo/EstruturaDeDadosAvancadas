# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:18:58 2019

@author: rafae
"""
from NodePointers import Node, AddLeaf, LevelAncestor
    
def Stack():
    return None
        
def Size(p):        #None.size nao existe
    if p == None:
        return 0
    else:
        return p.size

def Push(p, val):
    u = Node(val, p, Size(p) + 1)
    AddLeaf(u)
    return u
    
def Top(p):
    return p.val
    
def Pop(p):
    return p.parent
    
def Print(u):
    while u != None:
        print(u.val, end=" ")
        u = u.parent
    print("\n", end = "")
    
def K_TH(p, k):  # o prieiro a ser empilhado eh o "primeiro"
    return LevelAncestor(p, p.size - k).val