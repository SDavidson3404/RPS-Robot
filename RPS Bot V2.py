import random
userScore = 0
computerScore = 0
def RPS():
    choices = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(choices)
    userChoice = input("Enter rock, paper, or scissors: ").lower()
    global userScore, computerScore
    if userChoice not in choices:
        print("Invalid choice. Please try again.")
        return RPS()
    print(f"Computer chose: {computerChoice}")
    if userChoice == computerChoice:
        print("It's a tie!")
    elif (userChoice == 'rock' and computerChoice == 'scissors') or \
         (userChoice == 'paper' and computerChoice == 'rock') or \
         (userChoice == 'scissors' and computerChoice == 'paper'):
        print("You win!")
        userScore += 1
    else:
        print("Computer wins!")
        computerScore += 1
def playAgain():
    again = input("Do you want to play again? (Y/N): ")
    if again == 'Y':
        RPS()
        playAgain()
    elif again == 'N':
        print("Thanks for playing!")
        print(f"Your Score: {userScore}")
        print(f"Computer Score: {computerScore}")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        playAgain()

RPS()
playAgain()