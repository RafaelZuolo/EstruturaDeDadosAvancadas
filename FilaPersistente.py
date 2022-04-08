# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:28:04 2019

@author: rafae
"""
import PilhaPersistente

# essa classe define a "dupla" (pilha, removidos)
class Fila:
    def __init__(self, stack, rem):
        self.stack = stack
        self.rem = rem

def Queue():
    return Fila(None, 0)

def Size(q):
    if q.stack == None:
        return 0
    else:
        return q.stack.size - q.rem

def Enqueue(q, val):
    return Fila( PilhaPersistente.Push(q.stack, val), q.rem)
    
def Dequeue(q):
    return Fila(q.stack, q.rem + 1)
  
def First(q):
    return PilhaPersistente.K_TH(q.stack, q.rem + 1)

def K_TH(q, k):
    return PilhaPersistente.K_TH(q.stack, q.rem + k)
    
def Print(q):
    u = q.stack
    while PilhaPersistente.Size(u) - q.rem > 0:
        print(u.val, end =  " ")
        u = u.parent
    print("")
    