#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:14:56 2019
Trie compacta
@author: rafael
"""
import rb

class Edge:
    def __init__(self, ini, end, tree, sufix):
        self.ini = ini      # indice inicial da aresta
        self.end = end      # idice final da aresta
        self.tree = tree    # arvore de letras
        self.size = 1
        self.sufix = sufix
        self.branchIndex = 0 # o comprimento da raiz ateh a edge em caracteres
        self.isMarked = False # um marcador para saber se jah visitamos a Edge
                              # eh usado no LCP

class AS:
    def __init__(self, T):
        self.text = list(T)
        self.text.append('\0')
        self.textEnd = len(self.text) - 1 # ultimo indice do texto
        self.root = Edge(None, None, rb.TREE(), 0)
        for i in range(0, self.textEnd + 1):
            self.Insert(i)

    def BranchSplit(self, length, i, j, branch):
        #o split nao deve mudar nada, seu comprimento ainda é o do branch,
        # mesmo que o branch tenha que ter uma arborecencia
        split = Edge(j, branch.end, branch.tree, branch.sufix)
        split.size = branch.size
        split.branchIndex = branch.branchIndex
        leaf = Edge(i, self.textEnd, rb.TREE(), 0)
        leaf.branchIndex = length
        branch.end = j - 1
        branch.size += 1
        # encurtamos o edge do branch, precisamos acertar seu tamanho
        branch.branchIndex = length - (self.textEnd - i + 1)
        branch.tree = rb.TREE()
        rb.Insert(branch.tree, self.text[j], split)
        rb.Insert(branch.tree, self.text[i], leaf)
        return leaf

    def Insert(self, i):
        leaf = self.InsertRecursivo(self.textEnd - i + 1, i, self.root)
        leaf.sufix = i

    def InsertRecursivo(self, length, i, edge):
        edge.size += 1
        branch = rb.Search(edge.tree, self.text[i])
        if branch is False:
            leaf = Edge(i, self.textEnd, rb.TREE(), 0)
            leaf.branchIndex = length
            rb.Insert(edge.tree, self.text[i], leaf)
            return leaf
        else:
            branch = branch.data # agora branch eh um Edge, nao um Node da rbTREE
            j = branch.ini
            while j <= branch.end:
                if self.text[i] != self.text[j]:
                    return  self.BranchSplit(length, i, j, branch)
                i, j = i + 1, j + 1
            return self.InsertRecursivo(length, i, branch)


    def InSearch(self, word, i, edge):
        branch = rb.Search(edge.tree, word[i])
        if branch is False:
            return False, None, None
        else:
            branch = branch.data
            j = branch.ini
            while j <= branch.end:
                if word[i] == '\0':
                    return True, branch.size, branch
                elif word[i] != self.text[j]:
                    return False, None
                i, j = i + 1, j + 1
            if word[i] == '\0':
                return True, branch.size, branch
            return self.InSearch(word, i, branch)

    def Search(self, P):
        word = list(P)
        word.append('\0')
        return self.InSearch(word, 0, self.root)[0]

    def NOcurrences(self, P):
        word = list(P)
        word.append('\0')
        return self.InSearch(word, 0, self.root)[1]

    def Ocurrences(self, P):
        word = list(P)
        word.append('\0')
        branch = self.InSearch(word, 0, self.root)[2]
        OcurrencesRec(branch)
        print('')

    def SufixVec(self):
        rb.PrintOcurrences(self.root.tree)
        print('')

    # nessa implementacao, andamos na arvore in order, e quando chegamos numa
    # edge, marcamo-o e imprimimos o branchIndex seu pai se ele estiver marcado.
    # a ideia eh fazer meio que uma busca em profundidade, se existe uma
    # bifurcacao na edge, significa que duas folhas tem como LCP essa edge,
    # entao basta imprimir seu branchIndex na hora certa
    def LcpVec(self):
        rb.PrintLcp(self.root.tree, self.root)
        print('')
        # usamos marcadores nas Edges que devem ser resetados
        self.root.isMarked = False
        rb.ResetMark(self.root.tree)

def ResetMarkRec(edge):
    edge.isMarked = False
    rb.ResetMark(edge.tree)

def LcpRec(edge):
    rb.PrintLcp(edge.tree, edge)

def OcurrencesRec(edge):
    rb.PrintOcurrences(edge.tree)

def Print(h):
    PrintTrie(h.root, 0)

def PrintTrie(edge, h):
    rb.PrintT(edge.tree, h)
