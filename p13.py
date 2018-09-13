# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:26:31 2018

@author: Zhiwei Pan
"""

class p13:
    players = ['charles','martina','michael','florence','eli']
    for n in range(4):
        l=players[n:n+2]
        for a in l:
            print(a.title(),end=' ')
        print()