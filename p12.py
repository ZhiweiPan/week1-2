# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 13:14:31 2018

@author: Zhiwei Pan
"""

class p12:
    l=[1,2,3,4,5,6]
    for n in range(6):
        for a in l:
            print (a,end='')
        print ()
        l.append(l[0])
        del l[0]