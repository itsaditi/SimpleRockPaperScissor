import random
import sys
import tkinter as tk
import time
try:
    computer = ['Rock', 'Paper', 'Scissor']
    validinput=['a','w','d']
    userinputhist =[]
    print("=======================================================\n"," SIMPLE ROCK, PAPER, SCISSOR MADE IN PYTHON 3  ","\n=======================================================\n")
    username= input("What is your name ? ")
    print("Welcome, ", username,"\n")
    print("==========================================\n           INSTRUCTIONS\n==========================================\n", 
    ".\n[X] Switch off the caps lock of your keyboard. \n[X] a=Rock \n[X] w=Paper \n[X] d=Scissor. \n[X] Type the alphabet and press ENTER and repeat.",
    "\n[X] Press ctrl+c to exit the game.")
    input("==========================================\nPress any key to start the game.\n==========================================\n")
    print("Your game starts in :",)
    for i in range(5,0,-1):
        print(i, sep=' ', end=' ', flush=True); time.sleep(0.5)

    possiblecombination= [(0,2,0), (1,0,0), (2,1,0),(2,0,1),(0,1,1),(1,2,1)]
    score =[0,0]
    def compare(userinput, compinput, score):
        user,comp= validinput.index(userinput), computer.index(compinput)
        for x in possiblecombination:
            if x[0]== user and x[1]==comp:
                score[x[2]]= score[x[2]] +1
                return x[2], score
        return None, score

    print("\n")
    while True:
        
            inputval= input(username+" : ")
            if inputval in validinput:
                computerchoice = random.choice(computer)
                print("Computer : ",computerchoice)
                winner, currscore = compare(inputval,computerchoice, score )
                if winner == 0:
                    print("WINNER :", username)
                elif winner ==1:
                    print("WINNER : Computer")
                else:
                    print("Its a tie !")
                print("Score: ",username," : ",score[0], " | Computer : ",score[1])
            else:
                print("Sorry. Computer does not understand you. :-(")
            print("\n")
except KeyboardInterrupt:
    exit(1)