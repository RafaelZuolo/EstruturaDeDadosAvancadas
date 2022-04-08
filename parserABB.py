# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:37:11 2019

@author: rafae
"""

from ABBPersistente import BST, Insert, Delete, Search, Min, Print

r0 = BST()
r1 = Insert(r0, 4)
r2 = Insert(r1, 2)
r3 = Insert(r2, 6)
r4 = Insert(r3, 1)
r5 = Insert(r4, 3)
r6 = Insert(r5, 5)
r7 = Insert(r6, 7)
r8 = Insert(r7, 8)
r9 = Insert(r8, 11)
r10 = Insert(r9, 9)
r11 = Insert(r10, 12)
r12 = Insert(r11, 10)
#print(Min(r3).key)          # 2
#Print(r7)                   # 1 2 3 4 5 6 7

r8 = Delete(r7, 4)
#print(r8)
Print(r12)                   # 1 2 3 5 6 7
r13 = Delete(r12, 11)
Print(r13)                  # 1 2 3 4 5 6 7 8 10 11 12
#print(Search(r13, 6).key)   # 6
#r14 = Delete(r13, 1) 
#print(Min(r14).key)         #2
