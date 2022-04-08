# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:28:13 2019

@author: rafael
"""

#perde nota se ao inves de .depth for .size?
class Node:
    def __init__(self, val, parent, size):
        self.val = val
        self.size = size
        self.parent = parent
        self.jump =  self

# tentar fazer raiz.jump = raiz
# se v.jump.jump == v.jump entao v.jump eh a raiz
def AddLeaf(u):
    v = u.parent
    if v == None:# entao u eh a raiz
        u.jump = u
    elif (v.jump.jump != v.jump and
          v.size - v.jump.size == v.jump.size - v.jump.jump.size):
        u.jump = v.jump.jump
    else:
        u.jump = v
        
def LevelAncestor(u, k):
    y = u.size - k
    while u.size != y:
        if u.jump != None and u.jump.size >= y:
            u = u.jump
        else:
            u = u.parent
    return u

# precisa testar, talvez de ruim se LCA(u, v) = None
def LCA(u, v): 
	if u.size > v.size:
		u,v = v,u
	v = LevelAncestor(v, v.size - u.size)
	if u == v:
		return u
	while u.parent != v.parent:
		if u.jump != v.jump:
			u = u.jump
			v = v.jump
		else:
			u = u.parent
			v = v.parent
	return u.parent
    
    
