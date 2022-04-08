#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:14:56 2019
Trie compacta
@author: rafael
"""
import rb_tree as rb

class Node:
    def __init__(self, ini, fim, tree):
        self.ini = ini
        self.fim = fim
        self.tree = tree

class AS:
    def __init__(self, T):
        self.root = rb.TREE()
        self.text = list(T)
        self.text.append('\0')
        self.process(self.text)
        
    def AddSulfix(self, i):
        x = self.root
        y = rb.Search(x, self.text[i])
        if y is None:
            rb.Insert(x, )
    
    def Search(self, P):
        word = list(P)
        word.append('\0')
