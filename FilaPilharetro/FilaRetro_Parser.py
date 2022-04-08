# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:48:41 2019

@author: rafae
"""
now = 99999
from FilaRetro import FilaRetro

def PrintNow(q):
    print(q.Query_First(now))

def PrintTemp(q, t):
    print(q.Query_First(t))

def PrintKthTemp(q, k, t):
    print(q.Query_Kth(t, k))

q = FilaRetro()
q.Insert_Enqueue(.2, 2)
q.Insert_Enqueue(.5, 5)
q.Insert_Enqueue(.55, 55)
q.Insert_Enqueue(.7, 7)
q.Insert_Enqueue(.3, 3)
PrintNow(q)                 # 2
q.Insert_Enqueue(.1, 1)
q.Insert_Enqueue(.6, 6)
q.Insert_Enqueue(.4, 4)
PrintNow(q)                # 1
q.Insert_Dequeue(.35)
q.Insert_Dequeue(.8)
PrintNow(q)                # 3
q.Delete_Enqueue(.2)
q.Delete_Enqueue(.55)
PrintNow(q)               # 4
PrintTemp(q, .31)         # 1
#PrintKthTemp(q, 1, .31)
PrintTemp(q, .36)         # 3


#q.Insert_Enqueue(4, 1)
#print(q.Query_First(now))
#q.Insert_Enqueue(3, 2)
#print(q.Query_First(now))
#q.Insert_Enqueue(5, 3)
#print(q.Query_First(now))
#q.Insert_Dequeue(8)
#print(q.Query_First(4))
#q.Delete_Enqueue(5)
#print(q.Query_First(11))