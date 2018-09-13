# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:21:18 2018

@author: Zhiwei Pan
"""
class p5:
    def half_squared(list):
        for num in range(len(list)):
            n=list[num]
            list[num]=n*n/2
        return list

    l_0=[3,3]
    print (half_squared(l_0))
