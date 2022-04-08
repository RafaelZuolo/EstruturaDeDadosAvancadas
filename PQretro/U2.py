# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:07:27 2019

@author: rafae
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:59:07 2019

@author: rafael
"""
inf = float("inf")

class Node:
    def __init__(self, data, key, left, right, p, color):
        self.data = data
        self.key = key
        self.left = left
        self.right = right
        self.subSum = 0             # soma total da subarvore
        self.maxSum = 0             # soma maxima dos prefixos na subarvore
        self.minSum = 0             # soma minima dos prefixos na subarvore
        self.p = p                  # noh pai
        self.color = color          # Implementacao da rubro-negra
        self.maxNotQ = (-inf, None)     # maior chave na subarvore direita
                                        #que nao esta em Qnow
        self.minInQ = (inf, None)       #menor chave na subarvore esquerda
                                        #que esta em Qnow

# Implementacao do CLRS, que usa o node especial T.NIL

class TREE:
    def __init__(self):
        self.NIL = Node(None, None, None, None, None, "black")
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.p = self.NIL
        self.root = self.NIL

    # O Search retorna a folha com a chave e o nó interno
    # com a última "descida" para a direita, que pode ter sua key
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

    # devolve o maior noh da subarvore de x
    def TreeMax(self, x):
        while x.data is None:
            x = x.right
        return x

    def TreeMin(self, x):
        while x.data is None:
            x = x.left
        return x

    #para usar nas funcoes max e min do python
    def MaxNotQArg(self, maxNotQ):
        return maxNotQ[0]

    def MinInQArg(self, minInQ):
        return minInQ[0]

    #conserta os campos extras em funcao dos filhos
    def FixMaxMin(self, x):
        x.subSum = x.left.subSum + x.right.subSum
        x.maxSum = max({x.left.maxSum, x.left.subSum + x.right.maxSum})
        x.minSum = min({x.left.minSum, x.left.subSum + x.right.minSum, 0})
        x.maxNotQ = max(x.left.maxNotQ, x.right.maxNotQ, key=self.MaxNotQArg)
        x.minInQ = min(x.left.minInQ, x.right.minInQ, key=self.MinInQArg)

    #aplica a correcao subindo na arvore
    def UpFix(self, x):
        while x is not self.NIL:
            self.FixMaxMin(x)
            x = x.p

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
        # consertar o delta max e delta min e maxNotQ
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

    # conserta a chave do noh de navegacao
    def FixKey(self, x):
        y = x.right
        while y.left is not self.NIL:
            y = y.left
        x.key = y.key

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
            self.UpFix(x)
            self.RB_InsertFix(newP)

    def Insert(self, key, data, signal):
        x = Node(data, key, self.NIL, self.NIL, self.NIL, "black")
        x.subSum = signal
        x.maxSum = signal
        x.minSum = signal
        if signal != 0:
            x.maxNotQ = (x.data, x.key)
            x.minInQ = (inf, x.key)
        else:
            x.maxNotQ = (-inf, x.key)
            x.minInQ = (x.data, x.key)
        self.RB_Insert(x)
        return x

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
    # note que x eh folha
    def Delete(self, key):
        x, lastRight = self.Search(key)
        x.subSum = x.maxSum = x.minSum = 0
        self.UpFix(x.p)
        self.RB_Delete(x)
        self.FixKey(lastRight)


    # para debugar melhor
    def NotInOrderTraverse(self, x):
        if x is not self.NIL:

            print("Key =", x.key, "p =", x.p.key, "Data=", x.data,
                  "subSum=", x.subSum, "maxSum=", x.maxSum,
                  "minSum=", x.minSum, "maxNotQ=",
                  x.maxNotQ, "minInQ=", x.minInQ)
            self.NotInOrderTraverse(x.left)
            self.NotInOrderTraverse(x.right)

    # para debugar melhor
    def ColorPrint(self):
        self.NotInOrderTraverse(self.root)

    # imprime os dados
    def RB_Print(self, x, i):
        if x is not self.NIL:
            self.RB_Print(x.right,(i+5))
            print(i*" ",
                  x.key,
                  x.data,
                  x.subSum,
                  x.maxSum,
                  x.minSum,
                  x.maxNotQ,
                  x.minInQ)
            self.RB_Print(x.left, (i+7))



    def RB_Print_Key(self, x):
        if x is not self.NIL:
            self.RB_Print_Key(x.left)
            if x.data is not None:
                print(x.key, end = " ")
            self.RB_Print_Key(x.right)

    def Print(self):
        print("x.key, x.data, x.subSum, x.maxSum, x.minSum, x.maxNotQ, x.minInQ")
        self.RB_Print(self.root, 0)


    # retorna a soma parcial ateh a chave key
    def SubSum(self, key):
        tempSum = 0
        x = self.root
        y = x
        while x is not self.NIL:
            y = x
            if key >= x.key: # lembrar como sao os nohs de navegacao
                tempSum += x.left.subSum
                x = x.right
            else:
                x = x.left
        tempSum += y.subSum
        return y, tempSum

    #encontra a ultima ponte antes de t
    def LastBridgeBeforeFinder(self, t):
        x, partSum = self.SubSum(t)
        if partSum == 0:
            return x

        flagEspinhaEsquerda = True # um bug raro
        # aqui a invariante é a soma até o maior elemento da subarvore de x
        while x is not self.root:
            y = x.p
            print("x eh", x.key, partSum)
            if y.right is x:
                print("y right eh", y.key, y.left.key)
                print(partSum - x.subSum
                    - y.left.subSum + y.left.minSum)
                if (partSum - x.subSum
                    - y.left.subSum + y.left.minSum == 0):
                    print(y.left.key)
                    partSum -= x.subSum
                    x = y.left
                    flagEspinhaEsquerda = False
                    break
            else:
                partSum += y.right.subSum
            x = x.p

        if flagEspinhaEsquerda is True:
            return self.TreeMin(self.root)

        while x.data is None:
            if partSum - x.right.subSum + x.right.minSum == 0:
                x = x.right
            else:
                partSum -= x.right.subSum
                x = x.left
        return x


    # encontra a maior chave depois da ponte t comparando com a
    # chave que entrou agora
    def FindBigKeyAfterBridge(self, t):
        x = self.LastBridgeBeforeFinder(t)
        print("PONTE LAST EH:", x.key)
        y = x.p
        maxNode = (-inf, t)
        while x is not self.NIL:
            if ((y.left is x )# or x is self.root)
                and maxNode[0] < y.right.maxNotQ[0]):
                maxNode = y.right.maxNotQ
            x = x.p
            y = x.p

        return maxNode

    def BigKeySearchNotQ(self, maxNode):
        return self.Search(maxNode[1])[0]

#        node = self.root
#        while t < node.key:
#            node = node.right

#        return node

    def KeyToInsert(self, t):
        tupla = self.FindBigKeyAfterBridge(t)
        node = self.BigKeySearchNotQ(tupla)
        assert node.data is not None
#        assert node.data is key
        node.maxNotQ = (-inf, node.key)
        node.minInQ = (node.data, node.key)

        node.maxSum = node.minSum = node.subSum = 0
        self.UpFix(node.p)
        return node.data

    # agora o insert_delmin
    # vamos procurar o t com a soma parcial ateh ele
    # e depois vamos subir e descer na arvore para encontrar a ponte
    def FirstBridgeAfterFinder(self, t): #FUNCIONANDO!!!!!!!!!!!!!!!!
        x, partSum = self.SubSum(t)
        if partSum == 0:
            return x
        assert x.data is not None
        #invariantes: partSum == soma ateh x se x eh folha ou
        # maior elemento de x.left se eh noh interno
        while x is not self.root:
            y = x.p
            if y.left is x:
                if partSum + y.right.minSum == 0:
                    x = y.right
                    break
                else:
                    partSum += y.right.subSum
            x = x.p
        while x.data is None:
            if partSum + x.left.minSum == 0:
                x =x.left
            else:
                partSum += x.left.subSum
                x = x.right
        return x

    def FindSmallKeyBeforeBridge(self, t):
        x = self.FirstBridgeAfterFinder(t)
#        print("A PONTE AFTER EH:", x.key)
        y = x.p
        minK = (inf, t)

        while x is not self.root:
            if (y.right is x and minK[0] > y.left.minInQ[0]):
                minK = y.left.minInQ
            x = x.p
            y = x.p
        # se nunca atualizamos entao a ponte eh Qnow
        if minK[0] == inf:
            minK = x.minInQ
        return minK

    # encontramos o valor de key mas nao o noh com key
    def SmallKeySearchInQ(self, minK):
        return self.Search(minK[1])[0]

    def KeyToRemove(self, t):
        tupla = self.FindSmallKeyBeforeBridge(t)
#        print("DELETANDO A CHAVE:", tupla[0])
        node = self.SmallKeySearchInQ(tupla)
        assert node.data != -inf
        node.maxNotQ = (node.data, node.key)
        node.minInQ = (inf, node.key)
        node.maxSum = 1
        node.minSum = 1
        node.subSum = 1
        self.UpFix(node.p)
        return node.data
