"""
ROCK PAPER SCISSORS GAME:
================================================================
"""

import random

option_list = ["rock", "paper", "scissors"]

computer = random.choice(option_list)
userinput = input("Enter your choice: \n").lower()

# 3 options to lose:
lose1 = userinput == "scissors" and computer == "rock"
lose2 = userinput == "paper" and computer == "scissors"
lose3 = userinput == "rock" and computer == "paper"

if userinput not in option_list:
    print("Enter an option from: rock, paper, scissors")
    quit()

if userinput == computer:
    print("Tie")

elif lose1 == True or lose2 == True or lose3 == True:
    print("You lose")

else:
    print ("YOU WIN")