# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:25:27 2019

@author: rafae
"""
from FilaPersistente import Queue, Enqueue, Dequeue, Size, First, K_TH, Print

q0 = Queue()
Print(q0)
q1 = Enqueue(q0, 1)
q2 = Enqueue(q1,2)
q3 = Enqueue(q2,3)
q4 = Enqueue(q1,4)
print(First(q2))        # 1
q5 = Dequeue(q2)
Print(q5)               # 2
print(First(q5))        # 2
q6 = Enqueue(q2,5)
Print(q4)               # 4 1
print(First(q4))        # 1
q7 = Enqueue(q4,6)
print(Size(q6))         # 3
q8 = Enqueue(q3,7)
q9 = Dequeue(q3)
print(First(q7))        # 1
Print(q8)               # 7 3 2 1
print(K_TH(q8, 3))      # 3
Print(q9)               # 3 2
print(Size(q9))         # 2
print(K_TH(q9, 2))      # 3