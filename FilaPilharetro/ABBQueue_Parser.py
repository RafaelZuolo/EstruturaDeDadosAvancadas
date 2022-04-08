# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:25:29 2019

@author: rafae
"""
from ABBQueueCorrigido import TREE
#from ABBQueue import TREE

t = TREE()
t.Insert(10, "waa1")
t.Insert(30, "waa3")
t.Insert(41, "waa41")
t.Insert(20, "waa2")
t.Insert(40, "waa4")
t.Insert(21, "waa21")
t.Insert(50, "waa5")
t.Delete(41)
t.Insert(70, "waa7")
t.Insert(61, "waa61")
t.Insert(80, "waa8")
t.Insert(31, "waa31")
t.Insert(60, "waa6")
t.Delete(61)
t.Delete(21)
t.Delete(31)
t.PrintKey()
t.Print()
print(t.Kth(1))
print(t.Kth(2))
print(t.Kth(3))
print(t.Kth(4))
print(t.Kth(5))
print(t.Kth(6))
print(t.Kth(7))
print(t.Kth(8))
