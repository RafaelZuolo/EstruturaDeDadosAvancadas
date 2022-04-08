# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:29:12 2019

@author: rafael
"""
from NodePointers import Node, AddLeaf, LevelAncestor, LCA

#classe para representar a dupla (first, last)
class Dupla:
    def __init__(self, first, last):
        self.first = first
        self. last = last
 
#funcao que executa o AddLeaf logo quando cria o Node       
def NewNode(x, parent, size):
    u = Node(x, parent, size)
    AddLeaf(u)
    return u

def Deque():
    return Dupla(None, None)
    
def Front(d):
    return d.first.val
    
def Swap(d):
    return Dupla(d.last, d.first)

def Back(d):
    return Front(Swap(d))
    
def PushFront(d,x):
    if d.first == None:
        u = NewNode(x, d.first, 0)
        return Dupla(u,u)
    else:
        return Dupla(NewNode(x, d.first, d.first.size + 1), d.last)
    
def PushBack(d,x):
    return Swap(PushFront(Swap(d), x))
    
def PopFront(d):
    if d.first == d.last:
        return Dupla(None, None)
    if d.first != LCA(d.first, d.last):
        return Dupla(d.first.parent, d.last)
    else:
        return Dupla(LevelAncestor(d.last, d.last.size - d.first.size - 1), d.last)
    
def PopBack(d):
    return Swap(PopFront(Swap(d)))

def K_TH(d,k):
    lca = LCA(d.first, d.last)
    l1 = d.first.size - lca.size
    l2 = d.last.size - lca.size
    if k <= l1:
        return LevelAncestor(d.first, k-1).val
    else:
        return LevelAncestor( d.last, l2 + l1 - k + 1).val

def Print(d):
    lca = LCA(d.first, d.last)
    u = d.first
    while u != lca:
        print(u.val, end = " ")
        u = u.parent
    u = d.last
    w = u
    while u != lca:
        w = Node(u.val, w, 0)
        u = u.parent
    print(lca.val, end = " ")
    while w != d.last:
        print(w.val, end = " ")
        w = w.parent
    print("\n", end = "")