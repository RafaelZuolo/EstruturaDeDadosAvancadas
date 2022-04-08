# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:15:55 2019

@author: rafael
"""

from PilhaPersistente import Stack, Push, Pop, Top, Size, Print, K_TH

p0 = Stack()
p1 = Push(p0, 1)
p2 = Push(p1,2)
p3 = Push(p2,3)
p4 = Push(p1,4)
print(Top(p2))          # 2
p5 = Pop(p2)
print(Top(p5))          # 1
p6 = Push(p2,5)
print(Top(p4))          # 4
p7 = Push(p4,6)
print(Size(p6))         # 3
p8 = Push(p3,7)
p9 = Pop(p3)
print(Top(p7))          # 6
Print(p8)               # 7 3 2 1
print(K_TH(p8, 4))      # 7
print(K_TH(p8, 3))      # 3
print(K_TH(p8, 2))      # 2
print(K_TH(p8, 1))      # 1
Print(p9)               # 2 1