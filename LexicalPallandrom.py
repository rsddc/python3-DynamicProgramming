# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:57:16 2018

@author: Rakesh
"""


in_str='bac.cb'
def checkPallandrom(in_list):
        for i in range(len(in_list)):
            if in_list[i] is not in_list[-1-i]:
                return False
        return True
            
    
def findDots(in_list):
    dots=[]
    for i in range(len(in_list)):
        if in_list[i]=='.':
            dots.append(i)
    return dots
    
def isPallandrom(in_list):
        dots = findDots(in_list)
        for i in range(ord('a'),ord('z')+1):
            for j in dots:
                in_list[j] = chr(i)
            if checkPallandrom(in_list) == True:
                in_str = ''.join(k for k in in_list)
                print(in_str)
                return
            else:
                continue
        print(-1)
            
            
def pallandrom(in_str):
    # string is immutable. convert it into list
    in_list=[i for i in in_str]
    isPallandrom(in_list)


pallandrom(in_str)