# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:47:16 2019

@author: rafae
"""
from ABBStackCorrigido import TREE
#from ABBStack import TREE

p = TREE()
p.Insert(1, "push1", +1)
p.Insert(2, "push2", +1)
p.Insert(3, "push3", +1)
p.Insert(4, "pop4", -1)
p.Insert(5, "push5", +1)
p.Insert(6, "pop6", -1)
p.Insert(7, "push7", +1)
p.Insert(8, "push8", +1)
p.Delete(7)
p.Delete(3)
#p.ColorPrint()
print(p.LastPush(1)) # push1
print(p.LastPush(2)) # push2
print(p.LastPush(3)) # push2
print(p.LastPush(4)) # push1
print(p.LastPush(5)) # push5
print(p.LastPush(6)) # push1
print(p.LastPush(7)) # push1
print(p.LastPush(8)) # push8
