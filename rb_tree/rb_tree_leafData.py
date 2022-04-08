# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:59:07 2019

@author: rafae
"""

class Node:
    def __init__(self, data, key, left, right, p, color):
        self.data = data
        self.key = key
        self.left = left
        self.right = right
        #self.bigestKey = None
        self.isLeaf = None
        self.p = p
        self.color = color
#        self.isLeaf = isLeaf
   
# Implementacao do CLRS, que usa o node especial T.NIL     
class TREE:
    def __init__(self):
        self.NIL = Node(None, None, None, None, None, "black")
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.p = self.NIL
        self.root = self.NIL

# O Search retorna a folha com a chave e o nó interno
# com a última "descida" para a esquerda, que pode ter sua key
# atualizada
def Search(r, key):
    y = r.root
    lastLeft = r.NIL
    while y.data is None:
        if y.key >= key:
            lastLeft = y
            y = y.left
        else:
            y= y.right
    return y, lastLeft
        
def TreeMin(r, z):
    x = z
    while x.left is not r.NIL:
        x = x.left
    return x
    
def RB_TREE():
    return TREE()
        
def LeftRotate(r, x):
    y = x.right
    x.right = y.left
    if y.left is not r.NIL:
        y.left.p = x
    y.p = x.p
    if x.p is r.NIL:
        r.root = y
    elif x is x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y

def RightRotate(r, x):
    y = x.left
    x.left = y.right
    if y.right is not r.NIL:
        y.right.p = x
    y.p = x.p
    if x.p is r.NIL:
        r.root = y
    elif x is x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y
        
def RB_InsertFix(r, z):
    while z.p.color is "red":
        if z.p is z.p.p.left:
            y = z.p.p.right
            if y.color is "red":
                z.p.color = "black"
                y.color = "black"
                z.p.p.color = "red"
                z = z.p.p
            else:
                if z is z.p.right:
                    z = z.p
                    LeftRotate(r, z)
                z.p.color = "black"
                z.p.p.color = "red"
                RightRotate(r, z.p.p)
        else:
            y = z.p.p.left
            if y.color is "red":
                z.p.color = "black"
                y.color = "black"
                z.p.p.color = "red"
                z = z.p.p
            else:
                if z is z.p.left:
                    z = z.p
                    RightRotate(r, z)
                z.p.color = "black"
                z.p.p.color = "red"
                LeftRotate(r, z.p.p)
    r.root.color = "black"

    
def FixKey(r, x):
    y = x.left
    while y.right is not r.NIL:
        y = y.right
    x.key = y.key
    
# Inserimos como numa ABB comum
# mas queremos apenas dados nas folhas
def RB_Insert(r, z): 
    y = r.NIL
    x = r.root
    lastLeft = r.NIL
    while x is not r.NIL:
        y = x
        if z.key < x.key:
            if x.data is None:
                lastLeft = x
            x = x.left
        else:
            x = x.right
   # z.p = y
    if  x is r.root:
        r.root = z
        
    else:
        #print(y.key)
        assert y.data is not None    
        if z.key < y.key:
            newP = Node(None, z.key, z, y, y.p, "red")
        else:
            newP = Node(None, y.key, y, z, y.p, "red")
            if lastLeft is not r.NIL:
                lastLeft.key = z.key
        if y is r.root:
            r.root = newP
        else:
            if y.p.left is y:
                y.p.left = newP
            else:
                y.p.right = newP
        y.p = newP
        z.p = newP
        z.color = "black"
        z.left = r.NIL
        z.right = r.NIL
        RB_InsertFix(r, newP)
    
def Insert(r, data, key):
    RB_Insert(r, Node(data, key, r.NIL, r.NIL, r.NIL, "black"))

    
#deletaremos como no CLRS, utilizando o TreeTransplant
def RB_Transplant(r, u, v):
    if u.p is r.NIL:
        r.root = v
    elif u is u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p

def RB_DeleteFix(r, x):
    while x is not r.root and x.color is "black":
        if x is x.p.left:
            w = x.p.right
            if w.color is "red":
                w.color = "black"
                x.p.color = "red"
                LeftRotate(r,x.p)
                w = x.p.right
            if w.left.color is "black" and w.right.color is "black":
                w.color = "red"
                x = x.p
            else:
                if w.right.color is "black":
                    w.left.color = "black"
                    w.color = "red"
                    RightRotate(r, w)
                    w = x.p.right
                else:
                    w.color = x.p.color
                    x.p.color = "black"
                    w.right.color = "black"
                    LeftRotate(r, x.p)
                    x = r.root
        else:
            w = x.p.left
            if w.color is "red":
                w.color = "black"
                x.p.color = "red"
                RightRotate(r,x.p)
                w = x.p.left
            if w.left.color is "black" and w.right.color is "black":
                w.color = "red"
                x = x.p
            else:
                if w.left.color is "black" :
                    w.right.color = "black"
                    w.color = "red"
                    LeftRotate(r, w)
                    w = x.p.left
                else: 
                    w.color = x.p.color
                    x.p.color = "black"
                    w.left.color = "black"
                    RightRotate(r, x.p)
                    x = r.root
    x.color = "black"
    
#def RB_Delete(r, z):
#    y = z
#    y_orig_color = y.color
#    if z.left is r.NIL:
#        x = z.right
#        RB_Transplant(r, z, z.right)
#    elif z.right is r.NIL:
#        x = z.left
#        RB_Transplant(r, z, z.left)
#    else:
#        y = TreeMin(r, z.right)
#        y_orig_color = y.color
#        x = y.right
#        if y.p is z:
#            x.p = y
#        else:
#            RB_Transplant(r, y, y.right)
#            y.right = z.right
#            y.right.p = y
#        RB_Transplant(r, z, y)
#        y.left = z.left
#        y.left.p = y
#        y.color = z.color
#    if y_orig_color is "black" :
#        RB_DeleteFix(r, x)
def RB_Delete(r, z):
    y = z.p
    y_orig_color = y.color
    if z is y.left:
        RB_Transplant(r, y, y.right)
    else:
        RB_Transplant(r, y, y.left)
    if y_orig_color is "black":
        RB_DeleteFix(r, y.p)
        
    
def Delete(r, key):
    x, lastLeft = Search(r, key)
    if x is r.NIL:
        print("nao tem isso aki naum")
        return -1
    RB_Delete(r, x)
    FixKey(r, lastLeft)
 
    
def InOrderTraverse(r, x):
    if x is not r.NIL:
        InOrderTraverse(r, x.left)
        print("Key = ", x.key, " Data = ", x.data, "   color = ", x.color, "   parent = ", x.p.key )
        InOrderTraverse(r, x.right)
        
def ColorPrint(r):
    InOrderTraverse(r, r.root)
    
def RB_Print(r, x):
    if x is not r.NIL:
        RB_Print(r, x.left)
        if x.data is not None:
            print(x.data)
        RB_Print(r, x.right)
        
def Print(r):
    RB_Print(r,  r.root)
    