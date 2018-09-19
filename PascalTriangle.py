# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 07:18:33 2018

@author: rakesh sharma
"""

#pascal triangle
# =============================================================================
# 1
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1 
# 1 5 10 10 5 1 
# 1 6 15 20 15 6 1 
# 1 7 21 35 35 21 7 1 
# 
# =============================================================================

m=[1]
print(1)
for i in range(1,8):
    l=[]
    for j in range(0,i+len(m)+1,len(m)):
        if j == 0 or j==len(m)+i:
            print(1,end=' ')
            l.append(1)
            
        else:
            for k in range(len(m)-1):
                sum2 = m[k]+m[k+1]
                print(sum2,end=' ')
                l.append(sum2)
                
            
             
    m.clear()
    m.extend(l)
    print()
                