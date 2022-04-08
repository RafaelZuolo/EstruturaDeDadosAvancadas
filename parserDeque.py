#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:17:47 2019

@author: rafael
"""
from DequePersistente import Deque, Front, Back, PushFront, PushBack, PopFront, PopBack, K_TH, Print

d0 = Deque()
d1 = PushBack(d0, 3)
d2 = PushBack(d1, 4)
d3 = PushFront(d2, 2)
d4 = PushFront(d3, 1)
d5 = PopBack(d3)
d6 = PopBack(d5)
d66 = PushFront(d6, 66)
d77 = PushFront(d66, 77)
d88 = PopFront(d77)
d7 = PushFront(d6, 9)
d8 = PopFront(d6)
d9 = PushFront(d8, 6)
Print(d2)           # 3 4
Print(d88)          # 66 2
print(Front(d4))    #1
print(Back(d4))     # 4
Print(d4)           # 1 2 3 4
print(K_TH(d4, 1))  # 1
print(K_TH(d4, 2))  # 2
print(K_TH(d4, 3))  # 3
print(K_TH(d4, 4))  # 4
Print(d2)           # 3 4
print(Back(d9))     # 6
print(Front(d9))    # 6
Print(d9)           # 6
Print(d5)           # 2 3
Print(d6)           # 2
Print(d7)           # 9 2
