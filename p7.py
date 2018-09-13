# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:26:59 2018

@author: Zhiwei Pan
"""

class p7:
    import random
    
    a=random.randint(0,100)
    b=random.randint(0,100)
    c=random.randint(0,100)
    
    def exchange(a,b):
        a,b=b,a
        return a,b
    
    def resort(a,b,c):
        if (a<=b):
            a,b=p7.exchange(a,b)
        if (b<=c):
            b,c=p7.exchange(b,c)
        if (a<=c):
            a,c=p7.exchange(a,c)
        if (a<=b):
            a,b=p7.exchange(a,b)
        return a,b,c;
    
    print (a,b,c)
    print (resort(a,b,c))