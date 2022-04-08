# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:59:41 2019

@author: rafae
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:59:07 2019

@author: rafae
"""


class Node:
    def __init__(self, key, data, left, right, p, color):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
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

    def Search(self, key):
        y = self.root
        while y is not self.NIL and y.key != key:
            if y.key > key:
                y = y.left
            else:
                y= y.right
        if y is self.NIL:
            return False
        else:
            return y


    def TreeMin(self, z):
        x = z
        while x.left is not self.NIL:
            x = x.left
        return x

    def RB_TREE():
        return TREE()

    def LeftRotate(self, x):
        if x is self.NIL:
            return
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.p = x
        y.p = x.p
        if x.p is self.NIL:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def RightRotate(self, x):
        if x is self.NIL:
            return
        y = x.left
        x.left = y.right
        if y.right is not self.NIL:
            y.right.p = x
        y.p = x.p
        if x.p is self.NIL:
            self.root = y
        elif x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def RB_InsertFix(self, z):
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
                        #z = z.p.right
                        z = z.p
                        self.LeftRotate(z)
                    z.p.color = "black"
                    z.p.p.color = "red"
                    self.RightRotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color is "red":
                    z.p.color = "black"
                    y.color = "black"
                    z.p.p.color = "red"
                    z = z.p.p
                else:
                    if z is z.p.left:
                        #z = z.p.left
                        z = z.p
                        self.RightRotate(z)
                    z.p.color = "black"
                    z.p.p.color = "red"
                    self.LeftRotate(z.p.p)
        self.root.color = "black"

    # Inserimos como numa ABB comum
    def RB_Insert(self, z):
        y = self.NIL
        x = self.root
        while x is not self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if  y is self.NIL:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z
        z.color = "red"
        z.left = self.NIL
        z.right = self.NIL
        self.RB_InsertFix(z)

    def Insert(self, key, data):
        self.RB_Insert(Node(key, data, self.NIL, self.NIL, self.NIL, "red"))


    #deletaremos como no CLRS, utilizando o TreeTransplant
    def RB_Transplant(self, u, v):
        if u.p is self.NIL:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def RB_DeleteFix(self, x):
        while x is not self.root and x.color is "black":
            if x is x.p.left:
                w = x.p.right
                if w.color is "red":
                    w.color = "black"
                    x.p.color = "red"
                    self.LeftRotate(x.p)
                    w = x.p.right
                if w.left.color is "black" and w.right.color is "black":
                    w.color = "red"
                    x = x.p
                else:
                    if w.right.color is "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.RightRotate(w)
                        w = x.p.right
                    else:
                        w.color = x.p.color
                        x.p.color = "black"
                        w.right.color = "black"
                        self.LeftRotate(x.p)
                        x = self.root
            else:
                w = x.p.left
                if w.color is "red":
                    w.color = "black"
                    x.p.color = "red"
                    self.RightRotate(x.p)
                    w = x.p.left
                if w.left.color is "black" and w.right.color is "black":
                    w.color = "red"
                    x = x.p
                else:
                    if w.left.color is "black" :
                        w.right.color = "black"
                        w.color = "red"
                        self.LeftRotate(w)
                        w = x.p.left
                    else:
                        w.color = x.p.color
                        x.p.color = "black"
                        w.left.color = "black"
                        self.RightRotate(x.p)
                        x = self.root
        x.color = "black"

    def RB_Delete(self, z):
        y = z
        y_orig_color = y.color
        if z.left is self.NIL:
            x = z.right
            self.RB_Transplant(z, z.right)
        elif z.right is self.NIL:
            x = z.left
            self.RB_Transplant(z, z.left)
        else:
            y = self.TreeMin(z.right)
            y_orig_color = y.color
            x = y.right
            if y.p is z:
                x.p = y
            else:
                self.RB_Transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.RB_Transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_orig_color is "black" :
            self.RB_DeleteFix(x)


    def Delete(self, key):
        x = self.Search(key)
        if x is self.NIL:
            print("nao tem isso aki naum")
            return -1
        self.RB_Delete(x)


    def InOrderTraverse(self, x):
        if x is not self.NIL:
            self.InOrderTraverse(x.left)
            print("Key = ", x.key, "   color = ", x.color, "   parent = ", x.p.key )
            self.InOrderTraverse(x.right)

    def ColorPrint(self):
        self.InOrderTraverse(self.root)

    def RB_PrintT(self, x, h):
        import ShortTrie
        if x is not self.NIL:
            self.RB_PrintT( x.left, h )
            print(h*'   ', x.key, '[', x.data.ini, x.data.end,']' )
            ShortTrie.PrintTrie(x.data, h + 1)
            self.RB_PrintT( x.right, h )

    def PrintT(self, h):
        self.RB_PrintT(self.root, h)

    def Print(self):
        self.RB_Print(self.root,0)
        print('\n')

    def RB_Print(self, x, i):
        if x is not self.NIL:
            self.RB_Print( x.left, i)
            print(i*' ', x.key, end = ' ')
            self.RB_Print( x.right, i)

    def RB_PrintOcurrences(self, x):
        import ShortTrie
        if x is not self.NIL:
            self.RB_PrintOcurrences(x.left)
            if x.data.size == 1:
                print(x.data.sufix, end = ' ')
            ShortTrie.OcurrencesRec(x.data)
            self.RB_PrintOcurrences(x.right)

    def PrintOcurrences(self):
        self.RB_PrintOcurrences(self.root)

