# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 00:30:07 2018

@author: rakesh sharma
"""

def rec_call(list,min,max,number):
     if min > max:
         return -1
     else:
         mid = (min+max)//2
         if list[mid] == number:
             return mid+1
         elif list[mid] >= number:
             return rec_call(list,min,mid-1,number)
         else:
             return rec_call(list,mid+1,max,number)
         
            
def binarySeach(list,number):
    
    list.sort()
    if number <list[0] or number > list[len(list)-1]:
        return -1
    else:
        return rec_call(list,0,len(list)-1,number)