# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:50:00 2019

@author: rafae
"""
from random import randint
import numpy as np

class Node:
    def __init__(self, key, data):
        self.key = key
        self.rand = randint(1, 1000)
        self.data = data
        self.left = None
        self.right = None
        self.p = None

class Treap:
    def __init__(self):
        self.count = 0
        self.root = None
        self.min = None

    def Rotate(self, y):
        assert y.p is not y
        x = y.p
        if x.left is y: # rotacione para a direita
            x.left = y.right
            if y.right is not None:
                y.right.p = x
            y.p = x.p
            if x.p is None:
                self.root = y
            elif x is x.p.right:
                x.p.right = y
            else:
                x.p.left = y
            y.right = x
            x.p = y
        else:           # rotacione para a esquerda
            x.right = y.left
            if y.left is not None:
                y.left.p = x
            y.p = x.p
            if x.p is None:
                self.root = y
            elif x is x.p.left:
                x.p.left = y
            else:
                x.p.right = y
            y.left = x
            x.p = y

    def InSearch(self, key): #devolve o noh
        x = self.root
        self.count += 1
        while x is not None and x.key != key:
            self.count += 1
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def SobeHeap(self, x):
        while x is not self.root and x.rand < x.p.rand:
            self.Rotate(x)

    def TrocaKey(self, x, y):
        x.key, y.key = y.key, x.key

def Insert(r, key, data): #insere x na treap com raiz r
    if r.root is None:
        r.root = Node(key, data)
        r.min = key
    else:
        if r.min > key:
            r.min = key
        x = r.root
        y = r.root
        while x is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        newNode = Node(key,data)
        if key < y.key:
            y.left = newNode
        else:
            y.right = newNode
        newNode.p = y
        r.SobeHeap(newNode)

def Delete(r, key): #remove x da treap com raiz r
    x = r.InSearch(key)
    if x.left is None:
        if x is r.root:
            r.root = r.root.right
            r.root.p = None
        elif x.p.left is x:
            x.p.left = x.right
        else:
            x.p.right = x.right
        if x.right is not None:
            x.right.p = x.p
    else:
        temp = x.left
        while temp.right is not None:
            temp = temp.right
        r.TrocaKey(x, temp)
        if temp is x.left:
            x.left = temp.left
            if temp.left is not None:
                temp.left.p = x.left
        else:
            temp.p.right = temp.left
            temp.left.p = temp.p
    minNode = r.root
    while minNode.left is not None:
        minNode = minNode.left
    r.min = minNode.key



def Search(r, key): #true se key está na treap com raiz r e false caso contrário
   x = r.InSearch(key)
   if x is None:
      return False
   else:
       return True

def Min(r):# menor chave presente na treap com raiz r
    return r.min

def Print(r): #imprime todos os elementos na treap com raiz r
    Printi(r.root, 0)

def Printi(x, i):
    if x is not None:
        Printi(x.right, i+4)
        print(i*" ", x.key, x.rand)
        Printi(x.left, i+4)

#tr = Treap()
#Insert(tr, 1, 123)
#Insert(tr, 2, 123)
#Insert(tr, 3, 123)
#Insert(tr, 4, 123)
#Insert(tr, 5, 123)
#Delete(tr, 1)
##Print(tr)
#Insert(tr, 11, 123)
#Insert(tr, 6, 123)
#Insert(tr, 7, 123)
#Insert(tr, 8, 123)
#Insert(tr, 9, 123)
#Insert(tr, 10, 123)
#Print(tr)
print("Testes da Treap:")
r = Treap()
size = 10000
tests =1000000
for i in range(size):
    Insert(r, i, None)
for i in range(tests):
    if not Search(r, randint(0, size-1)):
        print("buca falha")
print("uniforme:", r.count/tests)
r.count = 0

for i in range(tests):
    if not Search(r, np.random.binomial(size-1, 0.5)):
        print("busca falha")
print("binomial:", r.count/tests)