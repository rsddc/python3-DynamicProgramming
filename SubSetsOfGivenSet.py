# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 23:07:12 2018

@author: rakesh sharma
"""

n=[1,2,3]
subset=1<<len(n)

result=[]
print(type(set))
for i in range(subset):
    subset=[]
    mask=1
    
    for k in range(len(n)):
        print(mask)
        if mask&i !=0:
            subset.append(n[k])
        
        mask = mask<<1
    result.append(subset)
            
print(result)