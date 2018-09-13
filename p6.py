# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:18:00 2018

@author: Zhiwei Pan
"""

class p6:
    score=int(input("input your score: (no less than 0 and no larger than 100)"))
    
    if (100>score>=90):
        print ("A")
    elif (90>score>=60):
        print("B")
    elif (60>score>=0):
        print("C")
    else:
        print("please input a reasonable score as required")
        