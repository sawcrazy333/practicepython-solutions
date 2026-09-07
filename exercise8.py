import random

gesture = input("Rock, paper or scissors? ")

while gesture != "quit":
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"You chose {gesture}")
    print(f"Computer chose {computer}")

    if gesture == computer:
        print("It's a draw!")
    elif gesture == "rock" and computer == "scissors":
        print("you win")
    elif gesture == "paper" and computer == "rock":
        print("you win")
    elif gesture == "scissors" and computer == "paper":
        print("you win")
    else:
        print("computer wins")

    gesture = input("Rock, paper or scissors? (or 'quit' to stop) ")