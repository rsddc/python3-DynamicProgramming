# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 12:57:45 2018

@author: Rakesh
"""
import random

        
def getLadder(score):
     ladder={5:25,10:29,22:41,28:55,44:95,70:89,79:81}
     sc = score
     if ladder.__contains__(score):
         print("Wow there is a ladder!!!: ", score,'you will climb up',ladder.get(score))
         sc = ladder.get(score)
     return sc
 
def getSnake(score):    
     snake={31:14,37:17,73:53,78:49,92:35,99:7}
     sc = score
     if snake.__contains__(score):
         print("There is a snake at: ", score,'you will reach down',snake.get(score))

         sc = snake.get(score)
     return sc


  
def play():
    player_1_name=''
    player_2_name=''
    win_score=100
    dice=[int(i) for i in range(1,7)]

    player_1_name=input('Enter your name:-')
    player_2_name=input('Enter your name:-')
    player_1_score=0
    player_2_score=0
    turn=0
    counter=0
    while (player_1_score <= win_score or player_2_score <= win_score):

        if turn%2 == 0:
            score=0
            print(player_1_name," is playing...")
            score = int(random.choice(dice))
            print(player_1_name,'got',score)

            player_1_score = player_1_score+score
            player_1_score = getSnake(player_1_score)
            player_1_score = getLadder(player_1_score)
            
            print(player_1_name, 'your final score is',player_1_score)
            if player_1_score >= win_score:
                print(player_1_name," is winner")
                break
            turn = turn+1
            
        if turn%2 == 1:

            score=0
            print(player_2_name," is playing...")
            score = int(random.choice(dice))
            print(player_2_name,'got',score)
            
            player_2_score = player_2_score+score
            player_2_score = getSnake(player_2_score)
            player_2_score = getLadder(player_2_score)
            
            print(player_2_name, 'your final score is',player_2_score)
            if player_2_score >= win_score:
                print(player_2_name," is winner")
                break

            turn = turn+1
            counter = counter+1

            
play()