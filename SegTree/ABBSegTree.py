# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 07:43:51 2019

@author: rafael
"""

class Node:
    def __init__(self, data, key, left, right, p, color):
        self.data = data
        self.key = key
        self.left = left
        self.right = right
#        self.subSize = 1
        self.p = p
        self.color = color  # campo para a implementacao Rubro-Negra
        self.segList = []
        self.minKey = None  # guarda o sup dos intervalos
        self.maxKey = None  # guarda o inf dos intervalos
                            # note que intervalo do noh eh [minKey, maxKey]

# Implementacao do CLRS, que usa o node especial T.NIL


class TREE:
    def __init__(self):
        self.NIL = Node(None, None, None, None, None, "black")
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
#        self.NIL.subSize = 0
        self.NIL.p = self.NIL
        self.root = self.NIL

    # O Search retorna a folha com a chave e o nó interno
    # com a última "descida" para a esquerda, que pode ter sua key
    # atualizada
    def Search(self, key):
        y = self.root
        lastLeft = self.NIL
        lastRight = self.NIL
        while y.data is None:
            if key < y.key:
                lastLeft = y
                y = y.left
            else:
                lastRight = y
                y = y.right
        return y, lastLeft, lastRight

    # Esse search já diminui em 1 o x.subSize
    # O DELETE SEMPRE TEM QUE ENCONTRAR A FOLHA!!!!
    def SearchDel(self, key):
        y = self.root
        lastLeft = self.NIL
        while y.data is None:
#            y.subSize -= 1
            if key < y.key:
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

    # para fins de debug
    def MaxCheck(self, x):
        if x is self.NIL:
            return 0
        y = x
        while y.right is not self.NIL:
            y = y.right
        assert x.maxKey == y.maxKey
    # para fins de debug
    def MinCheck(self, x):
        if x is self.NIL:
            return 0
        y = x
        while y.left is not self.NIL:
            y = y.left
        assert x.minKey == y.minKey

    def LeftRotate(self, x):
        y = x.right
        self.MaxCheck(x)
        self.MinCheck(x)
        self.MaxCheck(y)
        self.MinCheck(y)
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
        x.maxKey = x.right.maxKey
        x.minKey = x.left.minKey
        y.maxKey = y.right.maxKey
        y.minKey = y.left.minKey
#        y.minKey = x.minKey
#        x.maxKey = y.left.maxKey
        self.MaxCheck(x)
        self.MinCheck(x)
        self.MaxCheck(y)
        self.MinCheck(y)
#        y.subSize += x.left.subSize
#        x.subSize -= y.right.subSize

    def RightRotate(self, x):
        y = x.left
        self.MaxCheck(x)
        self.MinCheck(x)
        self.MaxCheck(y)
        self.MinCheck(y)
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
        x.maxKey = x.right.maxKey
        x.minKey = x.left.minKey
        y.maxKey = y.right.maxKey
        y.minKey = y.left.minKey
#        y.maxKey = x.maxKey
#        x.minKey = y.right.minKey
        self.MaxCheck(x)
        self.MinCheck(x)
        self.MaxCheck(y)
        self.MinCheck(y)
#        y.subSize += x.right.subSize
#        x.subSize -= y.left.subSize

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

    # conserta o nó interno de navegação
    def FixKey(self, x):
        y = x.left
        while y.right is not self.NIL:
            y = y.right
        x.key = y.key

    # conserta o minKey do noh e dos filhos a esquerda
    def FixMinKey(self, x):
        y = x
        while y.left is not self.NIL:
            y = y.left
        minKey = y.minKey
        y = x
        while y.left is not self.NIL:
            y.minKey = minKey
            y = y.left

    # conserta o maxKey do noh e dos filhos a direita
    def FixMaxKey(self, x):
        y = x
        while y.right is not self.NIL:
            y = y.right
        maxKey = y.maxKey
        y = x
        while y.right is not self.NIL:
            y.maxKey = maxKey
            y = y.right

    # Inserimos como numa ABB comum
    # mas queremos apenas dados nas folhas
    def RB_Insert(self, z):
        y = self.NIL
        x = self.root
        lastLeft = self.NIL
#        lastRight = self.NIL

        while x is not self.NIL:
            y = x
            if z.key < x.key:
                if x.data is None:
                    lastLeft = x
#                    x.subSize += 1
                x = x.left
            else:
#                if x.data is None:
#                    lastRight = x
#                    x.subSize += 1
                x = x.right

        if x is self.root:
            self.root = z
        else:
            assert y.data is not None
            if z.key < y.key:
                newP = Node(None, z.key, z, y, y.p, "red")
                newP.minKey = z.minKey
                newP.maxKey = y.maxKey
            else:
                newP = Node(None, y.key, y, z, y.p, "red")
                newP.minKey = y.minKey
                newP.maxKey = z.maxKey

                if lastLeft is not self.NIL: # sempre será essa chave
                    lastLeft.key = z.key
            if y is self.root:
                self.root = newP
            else:
                if y.p.left is y:
                    y.p.left = newP
                else:
                    y.p.right = newP
#                    self.FixMinKey(lastRight.right, newP.minKey)
#            self.MaxCheck(newP)
#            self.MinCheck(newP)
            self.UpFixing(newP)

            y.p = newP
            z.p = newP
            z.color = "black"
            z.left = self.NIL
            z.right = self.NIL
            self.RB_InsertFix(newP)

    def UpFixing(self, x):
        while x is not self.root:
            if x.p.left is x:
                x.p.minKey = x.minKey
            else:
                x.p.maxKey = x.maxKey
            x = x.p

    def Insert(self, key, data):
        x = Node(data, key, self.NIL, self.NIL, self.NIL, "black")
        x.maxKey = data[1]
        x.minKey = data[0]
        assert data[0] == key
        self.RB_Insert(x)

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

    def NotInOrderTraverse(self, x):
        if x is not self.NIL:
            print("Key = ", x.key, "Data = ", x.data,
#                  "subSize = ", x.subSize,
                  "parent = ", x.p.key, "interval = [", x.minKey, x.maxKey, "]")
            self.NotInOrderTraverse(x.left)
            self.NotInOrderTraverse(x.right)

    # para debugar melhor
    def ColorPrint(self):
        self.NotInOrderTraverse(self.root)

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

#    def PrintTree(self):
#        self.PrintTreei(self.root, 0)
#
#    def PrintTreei(self, x, i):
#        if x is not self.NIL:
#            self.

    def PrintKey(self):
        self.RB_Print_Key(self.root)
        print("\n")

##############################################################################
##########  Começa os códigos extras  ########################################
##############################################################################

    # inserimos o intervalo na lista de intervalos do noh x
    def IntervalInsert(self, x ,interval):
        if x is self.NIL:
            return 0
        elif interval[0] <= x.minKey and interval[1] >= x.maxKey:
            x.segList.append(interval)
        else:
            #if x.minKey < interval[1]:
            if x.left is not self.NIL and x.left.maxKey >= interval[0]:
                self.IntervalInsert(x.left, interval)
            #if x.maxKey > interval[0]:
            if x.right is not self.NIL and x.right.minKey <= interval[1]:
                self.IntervalInsert(x.right, interval)

    # inserimos todos os intervalos da lista
    def ProcessList(self, segList):
        for i in segList:
            self.IntervalInsert(self.root, i)

    # percorremos a árvore imprimindo os intervalos que contem o ponto point
    # recursivamente
    def IntervalSearch(self, x, point, bag):
        if x is not self.NIL:
            for i in x.segList:
                bag.add(i)
            if x.left is not self.NIL and x.left.maxKey >= point:
                self.IntervalSearch(x.left, point, bag)
            if x.right is not self.NIL and x.right.minKey <= point:
                self.IntervalSearch(x.right, point, bag)

    def IntervalSearchCall(self, point):
        bag = set()
        self.IntervalSearch(self.root, point, bag)
        print(bag)
