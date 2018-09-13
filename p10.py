# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:03:44 2018

@author: Zhiwei Pan
"""

class p10:
    import random
    a=random.randint(1,10)
    b=random.randint(1,10)
    
    print (a,b)
    def exchange(a,b):
        a,b=b,a
        return a,b
    a,b=exchange(a,b)
    print (a,b)