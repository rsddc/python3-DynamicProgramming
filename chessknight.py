# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:14:22 2018

@author: rakesh sharma
"""


board=[]
# =============================================================================
# Calculate the relative position where knight can be placed 2nd half from the
# current. Suppose current is (3,3) there are 8 possible moves from the current.
# position Next move can be (5,4)/(4,5)/(2,5) etc.
# =============================================================================

nextRow_i=[2,1,-1,-2,-2,-1,1,2]
nextCol_j=[1,2,2,1,-1,-2,-2,-1]

def printBoard(b):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end=' ')
        print()
    

def isvalidMove(currentBoard,r,c):
    #check the position in 9x9 board . It should be empty.First time move.
    if r >= 0 and r < len(currentBoard) and c >=0 and c < len(currentBoard) and currentBoard[r][c] ==0:
       return True
    else:
        return False

        
def allNextMovesByKnight(b,moveSofar,currR,currC):
    
    #Task 1:-Return Final results when all 64 moves completed.
    if moveSofar == 64:
        return True
    else:
        for i in range(8):
            #current position passed in recursion call i.e.0,0. 
            #Explore the next 8 possiblities in the range of 8
            nextR=currR+nextRow_i[i]
            nextC=currC+nextCol_j[i]
            if isvalidMove(b,nextR,nextC):
                #Place the first next move if it is empty with the help of next moves lists
                b[nextR][nextC]=moveSofar+1
                
# =============================================================================
#                 All remaing 7 will be called by recursion
#                 Here the Backtraking Logic:- All 7 possibles moves we are calling
#                 Through recursion.Boundary check and blank position is good.
#                 Still for all calls movessofar can be exceeds or may not 
#                 provide all 8 directions to move. like top row, last col,
#                 last row etc. so backtree will all recursive calling is success
#                 return true else make the position 0 again.
# =============================================================================
            
                ans=allNextMovesByKnight(b,moveSofar+1,nextR,nextC)
                if ans==True:
                    return True
                b[nextR][nextC]=0
#======================================BackTrack=======================================
    return False        
    
board=[[0 for i in range(8)] for j in range(8)]
board[0][0] = 1
printBoard(board)
print("Final positions:-")
ans = allNextMovesByKnight(board,1,0,0)    
if ans==True:
    printBoard(board)