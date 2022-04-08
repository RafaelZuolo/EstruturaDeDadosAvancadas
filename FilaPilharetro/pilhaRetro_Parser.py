# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:01:25 2019

@author: rafae
"""

from pilhaRetro import PilhaRetro

p = PilhaRetro()
p.Insert_Push(1, "push1")
p.Insert_Push(5, "push5")
p.Insert_Push(8, "push8")
p.Insert_Pop(7)
p.Insert_Push(2, "push2")
p.Insert_Pop(6)
p.Insert_Push(3, "push3")
p.Delete(7)
p.Insert_Pop(4)
print(p.Query_Top(1)) #push1
print(p.Query_Top(2)) #push2
print(p.Query_Top(3)) #push3
print(p.Query_Top(4)) #push2
print(p.Query_Top(5)) #push5
print(p.Query_Top(6)) #push2
print(p.Query_Top(7)) #push2
print(p.Query_Top(8), "\n\n") #push8
p.Delete(3)
print(p.Query_Top(1)) #push1
print(p.Query_Top(2)) #push2
print(p.Query_Top(3)) #push2
print(p.Query_Top(4)) #push1
print(p.Query_Top(5)) #push5
print(p.Query_Top(6)) #push1
print(p.Query_Top(7)) #push1
print(p.Query_Top(8), "\n\n") #push8