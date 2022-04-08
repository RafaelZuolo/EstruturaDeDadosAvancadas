# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:59:07 2019

@author: rafael
"""


class Node:
    def __init__(self, data, key, left, right, p, color):
        self.data = data
        self.key = key
        self.left = left
        self.right = right
#        self.bigestKey = None
#        self.isLeaf = None
        self.subSize = 1
        self.p = p
        self.color = color
        self.nLeft = 1

# Implementacao do CLRS, que usa o node especial T.NIL


class TREE:
    def __init__(self):
        self.NIL = Node(None, None, None, None, None, "black")
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.nLeft = 0
        self.NIL.subSize = 0
        self.NIL.p = self.NIL
        self.root = self.NIL

    # O Search retorna a folha com a chave e o nó interno
    # com a última "descida" para a esquerda, que pode ter sua key
    # atualizada
    def Search(self, key):
        y = self.root
        lastLeft = self.NIL
        while y.data is None:
            if y.key >= key:
                lastLeft = y
                y = y.left
            else:
                y = y.right
        return y, lastLeft

    # Esse search já diminui em 1 o x.subSize
    # O DELETE SEMPRE TEM QUE ENCONTRAR A FOLHA!!!!
    def SearchDel(self, key):
        y = self.root
        lastLeft = self.NIL
        while y.data is None:
            y.subSize -= 1
            if y.key >= key:
                lastLeft = y
                y = y.left
            else:
                y = y.right
        return y, lastLeft

    def TreeMin(self, z):
        x = z
        while x.left is not self.NIL:
            x = x.left
        return x

    def LeftRotate(self, x):
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
#        y.nLeft += x.nLeft
        y.subSize += x.left.subSize
        x.subSize -= y.right.subSize

    def RightRotate(self, x):
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
#        x.nLeft -= y.nLeft
        y.subSize += x.right.subSize
        x.subSize -= y.left.subSize

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
                        z = z.p
                        self.RightRotate(z)
                    z.p.color = "black"
                    z.p.p.color = "red"
                    self.LeftRotate(z.p.p)
        self.root.color = "black"

    def FixKey(self, x):
        y = x.left
        while y.right is not self.NIL:
            y = y.right
        x.key = y.key

    # Inserimos como numa ABB comum
    # mas queremos apenas dados nas folhas
    def RB_Insert(self, z):
        y = self.NIL
        x = self.root
        lastLeft = self.NIL
        while x is not self.NIL:
            y = x
            if z.key < x.key:
                if x.data is None:
                    lastLeft = x
                    x.subSize += 1
#                x.nLeft += 1
                x = x.left
            else:
#                z.nLeft = x.nLeft + z.nLeft
                if x.data is None:
                    x.subSize += 1
                x = x.right

        if x is self.root:
            self.root = z
        else:
            assert y.data is not None
            if z.key < y.key:
                newP = Node(None, z.key, z, y, y.p, "red")
#                newP.nLeft = z.nLeft
            else:
                newP = Node(None, y.key, y, z, y.p, "red")
#                newP.nLeft = y.nLeft
                if lastLeft is not self.NIL: # sempre será essa chave
                    lastLeft.key = z.key
            if y is self.root:
                self.root = newP
            else:
                if y.p.left is y:
                    y.p.left = newP
                else:
                    y.p.right = newP
#            newP.nLeft = newP.left.nLeft
            newP.subSize = 2
            y.p = newP
            z.p = newP
            z.color = "black"
            z.left = self.NIL
            z.right = self.NIL
            self.RB_InsertFix(newP)

    def Insert(self, key, data):
        self.RB_Insert(Node(data, key,
                            self.NIL, self.NIL, self.NIL, "black"))

#   deletaremos como no CLRS, utilizando o TreeTransplant
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
                    if w.left.color is "black":
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
        y = z.p
        y_orig_color = y.color
        if z is y.left:
            self.RB_Transplant(y, y.right)
        else:
            self.RB_Transplant(y, y.left)
        if y_orig_color is "black":
            self.RB_DeleteFix(y.p)

    # sempre deletamos algo que existe, neh?
    def Delete(self, key):
        x, lastLeft = self.SearchDel(key)
        if x is self.NIL:
            print("nao tem isso aki naum, a arvore estragou agora")
            assert x is not self.NIL
            return -1
        self.RB_Delete(x)
        self.FixKey(lastLeft)

    def InOrderTraverse(self, x):
        if x is not self.NIL:
            self.InOrderTraverse(x.left)
            print("Key = ", x.key, " Data = ", x.data,
                  " subSize = ", x.subSize, "  color = ", x.color, "  parent = ", x.p.key)
            self.InOrderTraverse(x.right)

    # para debugar melhor
    def ColorPrint(self):
        self.InOrderTraverse(self.root)

    # imprime os dados
    def RB_Print(self, x):
        if x is not self.NIL:
            self.RB_Print(x.left)
            if x.data is not None:
                print(x.data, end = " ")
            self.RB_Print(x.right)

    def RB_Print_Key(self, x):
        if x is not self.NIL:
            self.RB_Print_Key(x.left)
            if x.data is not None:
                print(x.key, end = " ")
            self.RB_Print_Key(x.right)

    def Print(self):
        self.RB_Print(self.root)
        print(" ")

    def PrintKey(self):
        self.RB_Print_Key(self.root)
        print("\n")

# valor de L - 1 no instante t, onde t é uma key
    def Count(self, t):
        count = 1
        x = self.root
        if self.root is self.NIL:
            return 0
        while x is not self.NIL:
            if x.key < t:
                count += x.left.subSize
                x = x.right
            else:
                x = x.left
        return count

# valor guardado em A[k]
    def Kth(self, k):
        count = 0
        x = self.root
        while x.data is None:
            if x.left.subSize + count < k:
                count += x.left.subSize
                x = x.right
            else:
                x = x.left
        return x.data
g = TREE()
g.Insert(20, 6)
g.Insert(10, 7)
g.Insert(50, 8)
g.Delete(10)
g.Insert(30, 0)
g.Print