# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:36:33 2019

@author: rafae
"""
from random import randint
import numpy as np

# Splay Tree

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.p = None

class SplayTree:
    def __init__(self):
        self.root = None
        self.count = 0
        self.min = None

    def Rotate(self, y):
        assert y.p is not y
        x = y.p
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        if x.left is y: # rotacione para a direita
            x.left = y.right
            if y.right is not None:
                y.right.p = x
#            y.p = x.p
#            if x.p is None:
#                self.root = y
#            elif x is x.p.right:
#                x.p.right = y
#            else:
#                x.p.left = y
            y.right = x
            x.p = y
        else:           # rotacione para a esquerda
            x.right = y.left
            if y.left is not None:
                y.left.p = x
#            y.p = x.p
#            if x.p is None:
#                self.root = y
#            elif x is x.p.left:
#                x.p.left = y
#            else:
#                x.p.right = y
            y.left = x
            x.p = y

    def Zigzig(self, x):
        assert x.p is not self.root
        self.Rotate(x.p)
        self.Rotate(x)

    def Zigzag(self, x):
        assert x.p is not self.root
        self.Rotate(x)
        self.Rotate(x)

    def Splay(self, x):
        while (x.p is not self.root and x is not self.root):
            if ((x.p.left is x and x.p.p.left is x.p)
                or (x.p.right is x and x.p.p.right is x.p)):
                self.Zigzig(x)
            else:
                self.Zigzag(x)
        if x is not self.root:
            self.Rotate(x)

    def InSearch(self, key):
        x = self.root
        y = x
        self.count += 1
        while x is not None and x.key != key:
            self.count += 1
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        if x is not None:
            self.Splay(x)
            return x
        else:
            self.Splay(y)
            return None

    def TrocaKey(self, x, y):
        x.key, y.key = y.key, x.key
        x.data, y.data = y.data, x.data

    def Printi(self, x, i):
        if x is not None:
            self.Printi(x.right, i + 2)
            print(i*" ", x.key)
            self.Printi(x.left, i + 2)

def Search(r, key):
    x = r.InSearch(key)
    if x is None:
        return False
    else:
        return True

def Insert(r, key, data):
    x = r.root
    y = x
    while x is not None:
        y = x
        if key < x.key:
            x = x.left
        else:
            x = x.right
    if x is r.root:
        r.root = Node(key, data)
        r.min = key
#        self.root.p = self.root
    else:
        if key < y.key:
            y.left = Node(key, data)
            y.left.p = y
            r.Splay(y.left)
        else:
            y.right = Node(key, data)
            y.right.p = y
            r.Splay(y.right)
        if r.min > key:
            r.min = key

def Delete(r, key):
    x = r.InSearch(key)
    if x.left is None:
        if x is r.root:
            r.root = r.root.right
            r.root.p = None
        else:
            if x.p.left is x:
                x.p.left = x.right
            else:
                x.p.right = x.right
            if x.right is not None:
                x.right.p = x.p
            r.Splay(x.p)
    else:
        temp = x.left
        while temp.right is not None:
            temp = temp.right
        tempPai = temp.p
        r.TrocaKey(x, temp)
        if temp is x.left:
            x.left = temp.left
            if temp.left is not None:
                temp.left.p = x.left
        else:
            temp.p.right = temp.left
            temp.left.p = temp.p
        r.Splay(tempPai)
    minNode = r.root
    while minNode.left is not None:
        minNode = minNode.left
    r.min = minNode.key

def Print(r):
    r.Printi(r.root, 0)

print("testes da Splay:")
s = SplayTree()
size = 10000
tests= 1000000
for i in range(size):
    Insert(s, i, None)
for i in range(tests):
    if not Search(s, randint(0, size-1)):
        print("busca falha")

print("uniforme:", s.count/tests) #numero medios de nohs tocados em 1 acesso

s.count = 0
for i in range(tests):
    if not Search(s, np.random.binomial(size-1, .5) ):
        print("busca falha")
print("binomial:", s.count/tests)


