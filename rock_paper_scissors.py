import random

# Options for the computer
options = ["rock", "paper", "scissors"]

# User Input
user_choice = input("Enter rock, paper, or scissors: ")
user_choice.lower()  # Convert input to lowercase

# Computer's Choice
computer_choice = random.choice(options)

# Determine Winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock smashes scissors.")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Paper covers rock.")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors cut paper.")
else:
    print("You lose! Better luck next time.")

print(f"Computer chose: {computer_choice}")
