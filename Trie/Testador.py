# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:19:07 2019

@author: rafae
"""

from ShortTrie import AS, Print


# TESTER
#       01234567890 # um guia das posicoes dos caracteres
h = AS("abracadabra")
print(h.NOcurrences("cadabr"))
print(h.NOcurrences("abra"))
print(h.Search("ara"))
print(h.NOcurrences(" "))
h.Ocurrences("bra")
h.SufixVec()            # 11 10 7 0 3 5 8 1 4 6 9 2
h.LcpVec()              # 0 1 4 1 1 0 3 0 0 0 2
Print(h)

