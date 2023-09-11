# # # We will write a rock paper scissors game in class - Complete it in this file
import random 

def plyrSelect():  
    global player
    player = input('Pick rock, paper, or scissors ')
    check()

def plyrSelect0():  
    global player
    print('Pick exactly one of the three options, rock, paper, or scissors ')
    player = input()
    check()

def check():
    if player == "rock":
        print("You picked:rock")
        cmptrSelect()
        scoring()
    elif player == "paper":
        print("You picked:paper")
        cmptrSelect()
        scoring()
    elif player == "scissors":
        print("You picked:scissors")
        cmptrSelect()
        scoring()
    else:
        plyrSelect0()
    
def cmptrSelect():
    global computer
    selection = ["rock", "paper", "scissors"]
    computer = random.choice(selection)
    print("The computer picked:" + computer)

def scoring():
    if player == "rock":
        if computer == "rock":
            print("Tie")
        elif computer == "paper":
            print("You Lose")
        elif computer == "scissors":
            print("You Win")
    if player == "paper":
        if computer == "rock":
            print("You Win")
        elif computer == "paper":
            print("Tie")
        elif computer == "scissors":
            print("You Lose")
    if player == "scissors":
        if computer == "rock":
            print("You Lose")
        elif computer == "paper":
            print("You Win")
        elif computer == "scissors":
            print("Tie")

plyrSelect()
