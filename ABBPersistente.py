# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:31:02 2019

@author: rafae
"""
#Estamos usando um Delete bem ineficiente, eh possivel melhorar

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def BST():
    return None

#cria uma copia de node
def Copy(node):
    if node is None:
        return None
    return Node(node.key, node.left, node.right)

def Min(r):
    if r is None:
        return None
    node = r
    while node.left is not None:
        node = node.left
    return node

def Max(r):
    if r is None:
        return None
    node = r
    while node.right is not None:
        node = node.right
    return node

def Search(r,x):
    node = r
    while node is not None:
        if node.key == x:
            return node
        elif node.key < x:
            node = node.right
        else:
            node = node.left
    return None

def Insert(r,x):
    if r is None:
        return Node(x, None, None)
    root = Node(r.key, r.left, r.right)
    node = root
    while node != None:
        if node.key < x:

            if node.right is not None:
                newNode = Copy(node.right)
                node.right = newNode
                node = newNode
            else:
                node.right = Node(x, None, None)
                node = None

        else:
            if node.left is not None:
                newNode = Copy(node.left)
                node.left = newNode
                node = newNode
            else:
                node.left = Node(x, None, None)
                node = None
    return root

def Delete(r, key):
    root = Copy(r)
    node = root

    while node.key != key:
        if key > node.key:
            node.right = Copy(node.right)
            node = node.right
        else:
            node.left = Copy(node.left)
            node = node.left

    leftSubMax = Max(node.left)
    if leftSubMax is None:
        node = node.right
    else:
        node.key = leftSubMax.key
        leftSubMax = None

    return root

# ao inves de atualizar o node, basta copiar a key
#def Delete(r,x):
#    root = Copy(r)
#    fatherNode = root
#    node = root
#
#    #passeamos pela árvore até encontrar o node a ser deletado
#    while node.key != x:
#        fatherNode = node
#        if node.key <= x:
#            node.right = Copy(node.right)
#            node = node.right
#        else:
#            node.left = Copy(node.left)
#            node = node.left
#
#    #caso temos a raiz para deletar
#    if node is root:
#        if root.left is None: #caso Null na esquerda
#            return root.right
#        elif root.right is None:
#            return root.left
#        else:
#            fatherNode = root
#            newRoot = Copy(root.left)
#            node = newRoot
#            while node.right is not None:
#                fatherNode = node
#                node.right = Copy(node.right)
#                node = node.right
##            print("filho do pai: ", end = " ")
##            print(fatherNode.right.key)
##            fatherNode.right = None
#            node.right = root.right
#            return newRoot
#
#    #caso NULL e NULL
#    if node.left is None and node.right is None:
#        if fatherNode.left is node:
#            fatherNode.left = None
#        else:
#            fatherNode.right = None
#        return root
#
#    #caso NULL e coisas
#    if node.left is None and node.right is not None:
#        if fatherNode.right is node:
#            fatherNode.right = node.right
#            return root
#        else:
#            fatherNode.left = node.right
#            return root
#
#    #caso coisas e NULL
#    if node.left is not None and node.right is None:
#        if fatherNode.right is node:
#            fatherNode.right = node.left
#            node = None
#            return root
#        else:
#            fatherNode.left = node.right
#            node = None
#            return root
#
#    #caso coisas e coisas
#    #if node.left is not None and node.right is not None:
#
#    if fatherNode.right is node:
#        rightNode = node.right
#        node = Copy(node.left)
#        leftTreeRoot = node
#        stepFather = node
#        #fatherNode.right = node #morreu o ponteiro para node == deletado
#        while node.right is not None:
#            stepFather = node
#            node.right = Copy(node.right)
#            node = node.right
#        if stepFather is not node:
#            stepFather.right = node.left
#            node.left = leftTreeRoot
#            #    if fatherNode.right.left is leftTreeRoot:
#        fatherNode.right = node
##    else:
##        fatherNode.left = node
#        node.right = rightNode #pendura a arvore direita na copia esquerda
#        return root
#
#    else:
#        rightNode = node.right
#        node = Copy(node.left)
#        leftTreeRoot = node
#        stepFather = node
#        #fatherNode.left = node #morreu o ponteiro para node == deletado
#        while node.right is not None:
#            stepFather = node
#            node.right = Copy(node.right)
#            node = node.right
#        if stepFather is not node:
#            stepFather.right = node.left
#            node.left = leftTreeRoot
#        fatherNode.left = node
#        node.right = rightNode #pendura a arvore direita na copia esquerda
#
#        return root


#imprime os elementos em ordem crescente
def Print(r):
    Printi(r, 0)
    print("\n\n")

def Printi(r, i):
    if r is not None:
        Printi(r.left, i + 2)
        print(i*" ", r.key)
        Printi(r.right, i + 2)

