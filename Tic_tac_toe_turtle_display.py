# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:36:29 2020

@author: jbris
"""
# #|#|#   =   0|1|2
# #|#|#   =   3|4|5
# #|#|#   =   6|7|8

import turtle
import random

def difference (answers, list2):
   list_dif = [i for i in answers if i not in list2]
   return list_dif

def canwin(player): # checks if ai can win, if it can, it puts in its answer and the game ends as win is set to true
    global win
    options = []
    for i in win_states:
        options.append(difference(i,player))
        out = []
        for i in options:
            if len(i) == 1:
                if i[0] not in ans_p:
                    out.append(i[0])
    if len(out) != 0:
        return out
    else:
        return False

possibles = list(range(0,9))    

win_states = [[0,1,2],[3,4,5],[6,7,8],
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6]]   

# visual output of board

wn = turtle.Screen()
wn.title("Tic tac toe")
wn.bgcolor("White")
wn.setup(width=600, height=400)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.hideturtle()
pen.penup()
def display_board(ans, x):
    for ans in ans:
        if ans < 3:    
            pen.goto(ans*30 - 50, 50)
        if ans > 2 and ans < 6:
            pen.goto(ans*30 - 140, 0)
        if ans >5 and ans <9:
            pen.goto(ans*30 - 230, -50)
    if x == 0:
        pen.write("X", align="center", font=("Courier", 24, "normal"))
    elif x == 1:
        pen.write("O", align="center", font=("Courier", 24, "normal"))
    else:
        pen.write(".", align="center", font=("Courier", 24, "normal"))
    wn.update()
            
# main loop
# (work in progress) 

edges = [1,3,5,7]
corners = [0,2,6,8]
middle = [4]
win = False

# who goes first
dummy = random.randint(1,2)
if dummy == 1:
    first = True    
else:
    first = False

if first:
    turn = "player turn"
    print("The player goes first")
else:
    turn = "ai turn"
    print("The AI will go first")

ans_ai = []
ans_p = []
ans = ans_p + ans_ai
while not win:
    if turn == "ai turn":
        if canwin(ans_ai):
            z = random.choice(canwin(ans_ai))
            print("ai puts answer in square :",z)
            print("GAMEOVER")
            ans_ai.append(z)
            display_board(ans_ai,0)
            win = True
            break
        
        if canwin(ans_p):
            put = [i for i in canwin(ans_p) if i in (edges+corners+middle)]
            if put:
                z = random.choice(put)
            else:
                z = []
        else:
            z = []
        if z:
            print("ai puts answer in square :", z, "to stop player from winning")
            ans_ai.append(z)
            ans = ans_p + ans_ai
            if z in edges:
                edges.remove(z)
            if z in corners:
                corners.remove(z)
            if z == 4:
                middle.remove(z)
            turn = "player turn"
            
        else:
            if corners:
                une = random.choice(corners)
                ans_ai.append(une)
                ans = ans_ai + ans_p
                corners.remove(une)
                turn = "player turn"
                print("ai puts answer in square: ", une)
            elif middle:
                une = random.choice(middle)
                ans_ai.append(une)
                ans = ans_ai + ans_p
                middle.remove(une)
                turn = "player turn"
                print("ai puts answer in square: ", une)
            elif edges:
                une = random.choice(edges)
                ans_ai.append(une)
                ans = ans_ai + ans_p
                edges.remove(une)
                turn = "player turn"
                print("ai puts answer in square: ", une)
    
    display_board(ans_ai, 0)
            
    if not corners and not edges and not middle:
        win = True
        print("Game is a tie")
        break
        
    if turn == "player turn":
        move = []
        canmove = corners + edges + middle
        print("Your options are: ", canmove)
        while move not in canmove:
            print('What is your next move? (0-8)')
            move = int(input())
        print("You put an O in ", move)
        ans_p.append(move)
        if move in corners:
            corners.remove(move)
        if move in edges:
            edges.remove(move)
        if move in middle:
            middle.remove(move)
        ans = ans_p + ans_ai
        # check if player has won
        check = []
        for each in win_states:
            check.append(difference(each,ans_p))
            if not difference(each,ans_p):
                print("The Player wins!")
                win = True
                break
        turn = "ai turn"
    display_board(ans_p, 1)
    wn.update()
while True:
    wn.update()