import random

input("Rock, Paper, Scissors, press enter to continue ")
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Rock, Paper, or Scissors? ").lower()
print("The computer plays", computer)
if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")

