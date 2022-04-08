# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:24:01 2019

@author: rafae
"""

#RB_Parser

from rb_tree_leafData import RB_TREE, Insert, Delete, Print, ColorPrint

T = RB_TREE()
Insert(T, "welp1", 1)
Insert(T, "welp6", 6)
#ColorPrint(T)
#print("\n\n")
Insert(T, "welp5", 5)
#ColorPrint(T)
#print("\n\n")
Insert(T, "welp4", 4)
#ColorPrint(T)
#print("\n\n")
Insert(T, "welp2", 2)
#ColorPrint(T)
#print("\n\n")
Insert(T, "welp3", 3)
#ColorPrint(T)
#print("\n\n")
Insert(T, "welp7", 7)
Insert(T, "welp15", 15)
Insert(T, "welp14", 14)
Insert(T, "welp13", 13)
Delete(T, 4)
Insert(T, "welp12", 12)
Insert(T, "welp11", 11)
Delete(T, 2)
Insert(T, "welp10", 10)
Insert(T, "welp9", 9)
Delete(T, 7)
Insert(T, "welp8", 8)
Delete(T, 3)

Delete(T, 1)

Delete(T, 6)
ColorPrint(T)