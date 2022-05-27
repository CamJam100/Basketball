import csv
from secrets import choice
import sys
from operator import truediv
import os
import keyboard
import subprocess
import array as arr
import time
import random

# Screen Class, controls screen attributes
class Screen:                    

    #set screen attributes
    def __init__(self):
        self.width = 90
        self.lines = 42
        self.backgroundColor = 0
        self.foregroundColor = 1
    
    #Clears the console screen
    def clear_screen(self):
        #Clear the console 
        #os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        subprocess.run('', shell=True)
        print('\033[3F' * CycleScreen.lines + " ")

# menu Class, controls various menu attributes
class MenuScreen:                    

    # Set player one attributes
    def __init__(self):
        self.choice = "z"

# screenchoice Class, controls various screenchoice attributes
class ScreenChoice:                    

    # Set player one attributes
    def __init__(self):
        self.screenOn = 1  

# playerteam Class, controls various player controlled team attributes
class PlayerTeam:                    

    # Set player one attributes
    def __init__(self):
        self.score = 0

# computerteam Class, controls various computer controlled team attributes
class ComputerTeam:                    

    # Set player one attributes
    def __init__(self):
        self.score = 0

# playerselection Class, controls various player choices attributes
class PlayerSelection:                    

    # Set player one attributes
    def __init__(self):
        self.decision = 0
        self.input = "a"

# computerselection Class, controls various computer choices attributes
class ComputerSelection:                    

    # Set player one attributes
    def __init__(self):
        self.decision = 0

# playerstreak Class, controls various player streak attributes
class PlayerStreak:                    

    # Set player one attributes
    def __init__(self):
        self.streak = 0

# computerstreak Class, controls various computer streak attributes
class ComputerStreak:                    

    # Set player one attributes
    def __init__(self):
        self.streak = 0

# coin Class, controls various coin attributes
class Coin:                    

    # Set player one attributes
    def __init__(self):
        self.flip = random.randint(1,2)

# possession Class, controls various possession attributes
class Possession:                    

    # Set player one attributes
    def __init__(self):
        self.ball = 0

# shot Class, controls various shooting attributes
class Shot:

    # Set player one attributes
    def __init__(self):
        self.shooting = 0
        self.block = 0

BasketballMenu = MenuScreen
BasketballScreen = Screen
BasketballScreenChoice = ScreenChoice
BasketballPlayerTeam = PlayerTeam
BasketballComputerTeam = ComputerTeam
BasketballPlayerSelection = PlayerSelection
BasketballComputerSelection = ComputerSelection
BasketballPlayerStreak = PlayerStreak
BasketballComputerStreak = ComputerStreak
BasketballCoin = Coin
BasketballPossession = Possession
BasketballShot = Shot

#Clear Console
os.system('cls' if os.name in ('nt', 'dos') else 'clear')

#Create Home Menu
def main():
    menu()

def menu():
    print("************Welcome to Basketball Beta**************")
    print()

    BasketballMenu.choice = input("""
                    A: Play
                    B: Help

                    Please enter your choice: """)

    if BasketballMenu.choice == "A" or BasketballMenu.choice =="a":
        BasketballScreenChoice.screenOn = 3
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    elif BasketballMenu.choice == "B" or BasketballMenu.choice =="b":
        BasketballScreenChoice.screenOn = 2
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()
menu()

#Create Help Menu
os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print("Select what you want to do on your offensive possession and be the first player to 21 to win the game!")
BasketballScreenChoice.screenOn = 3
time.sleep(4)
#Create Playing Menu
BasketballPlayerTeam.score = 0
BasketballComputerTeam.score = 0
if BasketballScreenChoice.screenOn == 3:
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    
    #Coin Flip For Possession
    BasketballCoin.flip = random.randint(1,2)
    PlayerSelection.decision = input("Heads(H) Or Tails(T)? ")
    if PlayerSelection.decision == "H" or PlayerSelection.decision == "h":
        if BasketballCoin.flip == 1:
            print("You Won The Coin Toss!")
            print("Loading...")
            BasketballPossession.ball = 1
        if BasketballCoin.flip == 2:
            print("You Lost The Coin Toss...")
            print("Loading...")
            BasketballPossession.ball = 2
    if PlayerSelection.decision == "T" or PlayerSelection.decision == "t":
        if BasketballCoin.flip == 2:
            print("You Won The Coin Toss!")
            print("Loading...")
            BasketballPossession.ball = 1
        if BasketballCoin.flip == 1:
            print("You Lost The Coin Toss...")
            print("Loading...")
            BasketballPossession.ball = 2
    
    #Create Basketball Scene
    time.sleep(2.5)
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    print("First to 21 Wins.")
    while BasketballPlayerTeam.score < 21 and BasketballPlayerTeam.score < 21:
        time.sleep(1)
        #Player On Offense, Computer On Defense
        if BasketballPossession.ball == 1:
            BasketballComputerSelection.decision = random.randint(1,2)
            if BasketballComputerSelection.decision == 1:
                BasketballComputerSelection.decision = "Sagging Off"
            if BasketballComputerSelection.decision == 2:
                BasketballComputerSelection.decision = "Playing Close"
            def main():
                menu()

            def menu():
                print("************You're On Offense**************")
                print(f"The Score is {BasketballPlayerTeam.score}-{BasketballComputerTeam.score}")
                print()
                print(f"The Defense is {BasketballComputerSelection.decision}")
                BasketballMenu.choice = input("""
                                A: Shoot 3
                                B: Drive And Shoot Mid-Range
                                C: Drive And Do A Layup
                                D: Drive And Dunk

                                Please enter your choice: """)

                if BasketballMenu.choice == "A" or BasketballMenu.choice =="a":

                    #Sagging Defense
                    if BasketballComputerSelection.decision == "Sagging Off":
                        BasketballShot.shooting = random.randint(1,3)
                        BasketballShot.block = random.randint(1,20)
                        if BasketballShot.shooting == 1:
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("Spla-a-a-a-ash!!!")
                                BasketballPlayerTeam.score = BasketballPlayerTeam.score + 3
                                BasketballPossession.ball = 2
                                if BasketballPlayerTeam.score >= 21:
                                    print("You Win!!!")
                        else: 
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Missed")
                                BasketballPossession.ball = 2

                    #Tight Defense
                    if BasketballComputerSelection.decision == "Playing Close":
                        BasketballShot.shooting = random.randint(1,10)
                        BasketballShot.block = random.randint(1,20)
                        if BasketballShot.shooting == 1:
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("Spla-a-a-a-ash!!!")
                                BasketballPlayerTeam.score = BasketballPlayerTeam.score + 3
                                BasketballPossession.ball = 2
                                if BasketballPlayerTeam.score >= 21:
                                    print("You Win!!!")
                        else: 
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Missed")
                                BasketballPossession.ball = 2

                elif BasketballMenu.choice == "B" or BasketballMenu.choice =="b":

                    #Sagging Defense
                    if BasketballComputerSelection.decision == "Sagging Off":
                        BasketballShot.shooting = random.randint(1,5)
                        BasketballShot.block = random.randint(1,20)
                        if BasketballShot.shooting == 1:
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Made The Shot")
                                BasketballPlayerTeam.score = BasketballPlayerTeam.score + 2
                                BasketballPossession.ball = 2
                                if BasketballPlayerTeam.score >= 21:
                                    print("You Win!!!")
                        else: 
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Missed")
                                BasketballPossession.ball = 2
                    
                    #Tight Defense
                    if BasketballComputerSelection.decision == "Playing Close":
                        BasketballShot.shooting = random.randint(1,2)
                        BasketballShot.block = random.randint(1,20)
                        if BasketballShot.shooting == 1:
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Made The Shot")
                                BasketballPlayerTeam.score = BasketballPlayerTeam.score + 2
                                BasketballPossession.ball = 2
                                if BasketballPlayerTeam.score >= 21:
                                    print("You Win!!!")
                        else: 
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Missed")
                                BasketballPossession.ball = 2

                elif BasketballMenu.choice == "C" or BasketballMenu.choice =="c":

                    #Sagging Defense
                    if BasketballComputerSelection.decision == "Sagging Off":
                        BasketballShot.shooting = random.randint(1,1)
                        BasketballShot.block = random.randint(1,5)
                        if BasketballShot.shooting == 1:
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Made The Layup, But Layups Are Boring")
                                BasketballPlayerTeam.score = BasketballPlayerTeam.score + 2
                                BasketballPossession.ball = 2
                                if BasketballPlayerTeam.score >= 21:
                                    print("You Win!!!")
                        else: 
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Missed")
                                BasketballPossession.ball = 2
                    
                    #Tight Defense
                    if BasketballComputerSelection.decision == "Playing Close":
                        BasketballShot.shooting = random.randint(1,2)
                        BasketballShot.block = random.randint(1,4)
                        if BasketballShot.shooting == 1:
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Made The Layup, But Layups Are Boring")
                                BasketballPlayerTeam.score = BasketballPlayerTeam.score + 3
                                BasketballPossession.ball = 2
                                if BasketballPlayerTeam.score >= 21:
                                    print("You Win!!!")
                        else: 
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Missed")
                                BasketballPossession.ball = 2
                
                elif BasketballMenu.choice == "D" or BasketballMenu.choice =="d":

                    #Sagging Defense
                    if BasketballComputerSelection.decision == "Sagging Off":
                        BasketballShot.shooting = random.randint(1,1)
                        BasketballShot.block = random.randint(1,5)
                        if BasketballShot.shooting == 1:
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Just Posterized Him!!!")
                                BasketballPlayerTeam.score = BasketballPlayerTeam.score + 2
                                BasketballPossession.ball = 2
                                if BasketballPlayerTeam.score >= 21:
                                    print("You Win!!!")
                        else: 
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Missed")
                                BasketballPossession.ball = 2
                    
                    #Tight Defense
                    if BasketballComputerSelection.decision == "Playing Close":
                        BasketballShot.shooting = random.randint(1,2)
                        BasketballShot.block = random.randint(1,4)
                        if BasketballShot.shooting == 1:
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Got An Easy Dunk")
                                BasketballPlayerTeam.score = BasketballPlayerTeam.score + 2
                                BasketballPossession.ball = 2
                                if BasketballPlayerTeam.score >= 21:
                                    print("You Win!!!")
                        else: 
                            if BasketballShot.block == 1:
                                print("Your Shot Was Blocked... That sucks")
                                BasketballPossession.ball = 2
                            else:
                                print("You Missed")
                                BasketballPossession.ball = 2
                else:
                    print("You must only select a choice")
                    print("Please try again")
                    menu()
            menu()
        
        #Computer On Offense, Player On Defense
        if BasketballPossession.ball == 2:
            def main():
                menu()

            def menu():
                print("************You're On Defense**************")
                print(f"The Score is {BasketballPlayerTeam.score}-{BasketballComputerTeam.score}")
                print()
                print(f"Select Your Defense")
                BasketballMenu.choice = input("""
                                A: Sag Off
                                B: Defend Close

                                Please enter your choice: """)

            if BasketballMenu.choice == "A" or BasketballMenu.choice =="a" or BasketballMenu.choice == "C" or BasketballMenu.choice =="c":
                BasketballComputerSelection.decision = random.randint(1,4)

                #Computer Shooting 3 On Sagging Defense
                if BasketballComputerSelection.decision == 1:
                    BasketballShot.shooting = random.randint(1,3)
                    BasketballShot.block = random.randint(1,20)
                    if BasketballShot.shooting == 1:
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("Spla-a-a-a-ash!!! (Oof...)")
                            BasketballComputerTeam.score = BasketballComputerTeam.score + 3
                            if BasketballComputerTeam.score >= 21:
                                print("Computer Wins...")
                    else: 
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Missed!")

                #Computer Drive + Mid On Sagging Defense
                if BasketballComputerSelection.decision == 2:
                    BasketballShot.shooting = random.randint(1,5)
                    BasketballShot.block = random.randint(1,20)
                    if BasketballShot.shooting == 1:
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Made The Shot (Oof...)")
                            BasketballComputerTeam.score = BasketballComputerTeam.score + 2
                            if BasketballComputerTeam.score >= 21:
                                print("Computer Wins...")
                    else: 
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Missed!")
                
                #Computer Drive + Layup On Sagging Defense
                if BasketballComputerSelection.decision == 3:
                    BasketballShot.shooting = random.randint(1,1)
                    BasketballShot.block = random.randint(1,5)
                    if BasketballShot.shooting == 1:
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Made The Layup, But Layups Are boring")
                            BasketballComputerTeam.score = BasketballComputerTeam.score + 2
                            if BasketballComputerTeam.score >= 21:
                                print("Computer Wins...")
                    else: 
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Missed!")

                #Computer Drive + Dunk On Sagging Defense
                if BasketballComputerSelection.decision == 4:
                    BasketballShot.shooting = random.randint(1,1)
                    BasketballShot.block = random.randint(1,5)
                    if BasketballShot.shooting == 1:
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Posterized You!")
                            BasketballComputerTeam.score = BasketballComputerTeam.score + 2
                            if BasketballComputerTeam.score >= 21:
                                print("Computer Wins...")
                    else: 
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Missed!")

            if BasketballMenu.choice == "B" or BasketballMenu.choice =="b" or BasketballMenu.choice == "D" or BasketballMenu.choice =="d":
                BasketballComputerSelection.decision = random.randint(1,4)

                #Computer Shooting 3 On Close Defense
                if BasketballComputerSelection.decision == 1:
                    BasketballShot.shooting = random.randint(1,10)
                    BasketballShot.block = random.randint(1,20)
                    if BasketballShot.shooting == 1:
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("Spla-a-a-a-ash!!! (Oof...)")
                            BasketballComputerTeam.score = BasketballComputerTeam.score + 3
                            if BasketballComputerTeam.score >= 21:
                                print("Computer Wins...")
                    else: 
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Missed!")

                #Computer Drive + Mid On Sagging Defense
                if BasketballComputerSelection.decision == 2:
                    BasketballShot.shooting = random.randint(1,2)
                    BasketballShot.block = random.randint(1,20)
                    if BasketballShot.shooting == 1:
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Made The Shot (Oof...)")
                            BasketballComputerTeam.score = BasketballComputerTeam.score + 2
                            if BasketballComputerTeam.score >= 21:
                                print("Computer Wins...")
                    else: 
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Missed!")
                
                #Computer Drive + Layup On Sagging Defense
                if BasketballComputerSelection.decision == 3:
                    BasketballShot.shooting = random.randint(1,2)
                    BasketballShot.block = random.randint(1,4)
                    if BasketballShot.shooting == 1:
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Made The Layup, But Layups Are boring")
                            BasketballComputerTeam.score = BasketballComputerTeam.score + 2
                            if BasketballComputerTeam.score >= 21:
                                print("Computer Wins...")
                    else: 
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Missed!")

                #Computer Drive + Dunk On Sagging Defense
                if BasketballComputerSelection.decision == 4:
                    BasketballShot.shooting = random.randint(1,2)
                    BasketballShot.block = random.randint(1,4)
                    if BasketballShot.shooting == 1:
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Posterized You!")
                            BasketballComputerTeam.score = BasketballComputerTeam.score + 2
                            if BasketballComputerTeam.score >= 21:
                                print("Computer Wins...")
                    else: 
                        if BasketballShot.block == 1:
                            print("You Blocked The Shot!")
                        else:
                            print("He Missed!")
        if BasketballPossession.ball == 2:
            BasketballPossession.ball = 1
