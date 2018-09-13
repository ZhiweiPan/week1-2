# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:03:07 2018

@author: Zhiwei Pan
"""

l=[]
for num in range(1,100):
    total=0
    i=num**3
    list1=list(str(i))
    for n in list1:
        total=total+int(n)
    if num==total:
        if i<10:
            print (num,"^3 = ",i)
        else:
            list1=list(str(i))
            print (num,"^3 = ",i,"->",end='')
            for n in range(len(list1)):
                if n==len(list1):
                    print (list1[n],end='')
                else:
                    print (list1[n],"+",end='')
            print ("=",num)