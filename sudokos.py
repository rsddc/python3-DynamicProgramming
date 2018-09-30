# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 08:14:21 2018

@author: rakesh sharma
"""

sudo=[
      [1,0,2,4],
      [0,0,3,1],
      [3,4,0,2],
      [2,0,4,3]
      ]



sudo=[[7,8,0,4,0,0,1,2,0],
      [6,0,0,0,7,5,0,0,9],
      [0,0,0,6,0,1,0,7,8],
      [0,0,7,0,4,0,2,6,0],
      [0,0,1,0,5,0,9,3,0],
      [9,0,4,0,6,0,0,0,5],
      [0,7,0,3,0,0,0,1,2],
      [1,2,0,0,0,7,4,0,0],
      [0,4,9,2,0,6,0,0,7]]

#sudo=[
#      [0,6,0,1,0,4,0,5,0],
#      [0,0,8,3,0,5,6,0,0],
#      [2,0,0,0,0,0,0,0,1],
#      [8,0,0,4,0,7,0,0,6],
#      [0,0,6,0,0,0,3,0,0],
#      [7,0,0,9,0,1,0,0,4],
#      [5,0,0,0,0,0,0,0,2],
#      [0,0,7,2,0,6,9,0,0],
#      [0,4,0,5,0,8,0,7,0]
#      ]

#sudo=[
#    [0, 0, 0, 2, 6, 0, 7, 0, 1],
#    [6, 8, 0, 0, 7, 0, 0, 9, 0],
#    [1, 9, 0, 0, 0, 4, 5, 0, 0],
#    [8, 2, 0, 1, 0, 0, 0, 4, 0],
#    [0, 0, 4, 6, 0, 2, 9, 0, 0],
#    [0, 5, 0, 0, 0, 3, 0, 2, 8],
#    [0, 0, 9, 3, 0, 0, 0, 7, 4],
#    [0, 4, 0, 0, 5, 0, 0, 3, 6],
#    [7, 0, 3, 0, 1, 8, 0, 0, 0]
#]


#N=9

def canPlace(sudo,number,i,j):
    #rows
    col_0=[i for i in sudo[i]]
    row_0=[row[j] for row in sudo]
    if number in col_0:
        return False
    elif number in row_0:
        return False
    return True
    



def printsudo():    
    for i in range(len(sudo)):
        for j in range(len(sudo)):
            print(sudo[i][j],end=' ')
        print()

def sudoko(sudo):
    emp=False
    for i in range(len(sudo)):
        for j in range(len(sudo)):
            if sudo[i][j] == 0:
               emp=True
               break
        if emp:
            break
    if emp == False:
        return True
    for number in range(1,len(sudo)+1):
        if canPlace(sudo,number,i,j):
            sudo[i][j]=number
            if(sudoko(sudo)):
                return True
        sudo[i][j]=0
    return False            
                
ans=sudoko(sudo)
if ans:                
    printsudo()              