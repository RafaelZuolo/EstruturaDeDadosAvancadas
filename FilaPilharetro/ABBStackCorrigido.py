# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:18:17 2019

@author: rafae
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:35:54 2019

@author: rafae
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:59:07 2019

@author: rafael
"""
class SmallNode:
    def __init__(self, data, filho):
        self.data = data
        self.filho = filho

class Node:
    def __init__(self, data, key, left, right, p, color):
        self.data = data
        self.key = key
        self.left = left
        self.right = right
        self.subSum = 0
        self.maxSum = 0
        self.minSum = 0
        self.p = p
        self.color = color


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
        lastRight = self.NIL
        while y.data is None:
            if key >= y.key:
                lastRight = y
                y = y.right
            else:
                y = y.left
        return y, lastRight

    def TreeMin(self, z):
        x = z
        while x.left is not self.NIL:
            x = x.left
        return x

    def FixMaxMin(self, x):
        x.subSum = x.left.subSum + x.right.subSum
        x.maxSum = max({x.left.maxSum, x.left.subSum + x.right.maxSum})
        x.minSum = min({x.left.minSum, x.left.subSum + x.right.minSum})

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
        y.subSum += x.left.subSum # consertar as somas parciais da subarvore
        x.subSum -= y.right.subSum
        # consertar o delta max e delta min
        self.FixMaxMin(x)
        self.FixMaxMin(y)

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
        y.subSum += x.right.subSum
        x.subSum -= y.left.subSum
        self.FixMaxMin(x)
        self.FixMaxMin(y)

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
        y = x.right
        while y.left is not self.NIL:
            y = y.left
        x.key = y.key

    def UpSizeFix(self, x):
        while x is not self.NIL:
            self.FixMaxMin(x)
            x = x.p

    # Inserimos como numa ABB comum
    # mas queremos apenas dados nas folhas
    def RB_Insert(self, z):
        y = self.NIL
        x = self.root
        lastRight = self.NIL
        while x is not self.NIL:
            y = x
            if z.key < x.key:
                if x.data is None:
                    x.subSum += z.subSum
                x = x.left
            else:
                if x.data is None:
                    lastRight = x
                    x.subSum += z.subSum
                x = x.right
        if x is self.root:
            self.root = z
        else:
            assert y.data is not None
            if z.key < y.key:
                newP = Node(None, y.key, z, y, y.p, "red")
                if lastRight is not self.NIL: # sempre será essa chave
                    lastRight.key = z.key
            else:
                newP = Node(None, z.key, y, z, y.p, "red")
            if y is self.root:
                self.root = newP
            else:
                if y.p.left is y:
                    y.p.left = newP
                else:
                    y.p.right = newP
            newP.subSum = y.subSum + z.subSum
            self.FixMaxMin(newP)
            y.p = newP
            z.p = newP
            self.UpSizeFix(newP.p)
#            z.color = "black"
#            z.left = self.NIL
#            z.right = self.NIL
            self.RB_InsertFix(newP)

    def Insert(self, key, data, signal):
        x = Node(data, key, self.NIL, self.NIL, self.NIL, "black")
        x.subSum = signal
        x.maxSum = signal
        x.minSum = signal
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

    # Esse search já devolve a pilha
    # para consertar o maxSum e o minSum
    # O DELETE SEMPRE TEM QUE ENCONTRAR A FOLHA!!!!
    def SearchDel(self, key):
        y = self.root
        lastRight = self.NIL
        while y.data is None:
            if key >= y.key:
                lastRight = y
                y = y.right
            else:
                y = y.left
        return y, lastRight

    # sempre deletamos algo que existe
    # note que x eh folha mas nao empilhamos a folha
    def Delete(self, key):
        x, lastRight = self.SearchDel(key)
        x.subSum = x.maxSum = x.minSum = 0
        self.UpSizeFix(x)
        self.RB_Delete(x)
        self.FixKey(lastRight)

    def InOrderTraverse(self, x):
        if x is not self.NIL:
            self.InOrderTraverse(x.left)
            print("Key =", x.key, "p =", x.p.key, "Data =", x.data,
                  "subSum =", x.subSum, "maxSum =", x.maxSum,
                  "minSum =", x.minSum)

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



    def SubSum(self, key):
        tempSum = 0
        x = self.root
        y = self.NIL
        while x is not self.NIL:
            y = x
            if key >= x.key:
                tempSum += x.left.subSum
                x = x.right
            else:
                x = x.left
        assert y.data is not None
        tempSum += y.subSum
        return y, tempSum

    def LastPush(self, t):
        x, subSum = self.SubSum(t)
        trackSum = 0
        if x.subSum == 1:
            return x.data
        x = self.root
        while x.data is None:
            if (x.left.subSum + x.right.minSum < subSum
                and x.left.subSum + x.right.maxSum <= subSum):
                trackSum +=x.left.subSum
                x = x.right
            elif (x.right.data is not None and trackSum + x.subSum == subSum
                  and x.right.subSum != -1):
                return x.right.data
            else:
                x = x.left
        return x.data

# valor de L - 1 no instante t, onde t é uma key
#    def Count(self, t):
#        count = 1
#        x = self.root
#        if self.root is self.NIL:
#            return 0
#        while x is not self.NIL:
#            if x.key < t:
#                count += x.left.subSize
#                x = x.right
#            else:
#                x = x.left
#        return count

# valor guardado em A[k]
#    def Kth(self, k):
#        count = 0
#        x = self.root
#        while x.data is None:
#            if x.left.subSize + count < k:
#                count += x.left.subSize
#                x = x.right
#            else:
#                x = x.left
#        return x.data
