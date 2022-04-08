# -*- coding: utf-8 -*-
"""
TRIE

Created on Wed Jul  3 14:26:34 2019

@author: rafael
"""
import rb

class AS:
    def __init__(self, T):
        self.root = rb.TREE()
        self.text = list(T)
        self.text.append('\0')
        self.n = len(self.text)
        for i in range(0, self.n):
            self.SulfixInsert(i)

    def SulfixInsert(self, i):
        x = self.root
        for j in range(i, self.n):
            node = rb.Search(x, self.text[j])
            if node is False:
                rb.Insert(x, self.text[j], rb.TREE())
            x = rb.Search(x, self.text[j]).data

    def Search(self, P):
        x = self.root
        word = list(P)
        for j in range(0, len(word)):
            node = rb.Search(x, word[j])
            if node is False:
                return False
            x = node.data
        return True

tri = AS("abracadabra")
print(tri.Search("bra"))
print(tri.Search("abroba"))