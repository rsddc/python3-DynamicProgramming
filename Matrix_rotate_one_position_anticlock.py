# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 20:43:05 2018

@author: rakesh sharma
"""

def shift_1_anti_clock(rows,cols,a):
    
    top = 0
    bottom=rows-1
    left = 0
    right = cols-1
    while left< right and top < bottom:
        prev = a[top+1][right]
        
        #move right to left
        for l in range(right,left-1,-1):
            curr = a[top][l]
            print(prev,end=' ')
            prev=curr
        top+=1

        #move top to bottom
        for d in range (top,bottom+1):
            curr = a[d][left]
            print(prev,end=' ')
            prev=curr
        left+=1
        
        #move left to right
        for r in range (left,right+1):
            curr = a[bottom][r]
            print(prev,end=' ')
            prev=curr        
        bottom-=1
        
        #move bottom to up
        for u in range(bottom,top-1,-1):
          if(top==bottom):#odd number of rows and cols 
            curr=a[u][right-1]
            print(curr,)
          else:
            curr=a[u][right]
            print(prev,end=' ')
            prev=curr
        right-=1
        print()


#shift_1_anti_clock(4,4,[[1,2,3,4],
#                        [5,6,7,8],
#                        [9,10,11,12],
#                        [13,14,15,16]
#                        ])
    
    
    
#shift_1_anti_clock(3,3,[[1,2,3],
#                        [5,6,7],
#                        [9,10,11]
#                        ])
        
        
shift_1_anti_clock(5,5,[[1,2,3,97,8],
                        [5,6,7,67,111],
                        [9,10,11,55,54],
                        [19,20,21,22,23],
                        [79,25,29,24,230]
                        ])

    
#shift_1_anti_clock(2,2,[[1,2],[15,16]
#                        ])
    
    
#shift_1_anti_clock(6,6,[[1,2,3,90,98,11],
#                        [5,6,7,67,56,17],
#                        [9,10,11,55,66,18],
#                        [12,13,14,15,16,19],
#                        [21,22,234,3,65,20],
#                        [32,33,34,68,69,91]
#                        
#                        ])