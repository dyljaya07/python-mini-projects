import random
options = ["rock", "paper", "scissors"]

print("Welcome to the rock paper scissors game!")
name = input("What is your name?: ")
print(f"Ready to begin {name}!? Don't say I didn't warn you!")

while True:
    choice = random.choice(options)
    guess = (input("Pick your weapon!(rock, paper, or scissors): ")).lower()

# rock options
    if guess == "rock" and choice == "scissors":
        print("URGHHHH YOU DEFEATED ME!!!!!")
        rematch = input("I challenge you to a rematch, that's if your not scared!? (y/n): ")
        if rematch == "y":
            continue
        elif rematch == "n":
            break
    if guess == "rock" and choice == "paper":
        rematch = input("Haaa! I win! Want to play again? (y/n): ")
        if rematch == "y":
            continue
        elif rematch == "n":
            break
    if guess == "rock" and choice == "rock":
        print("Copy cat!")
        continue

# paper options
    if guess == "paper" and choice == "rock":
        print("URGHHHH YOU DEFEATED ME!!!!!")
        rematch = input("I challenge you to a rematch, that's if your not scared!? (y/n): ")
        if rematch == "y":
            continue
        elif rematch == "n":
            break
    if guess == "paper" and choice == "scissors":
        rematch = input("Haaa! I win! Want to play again? (y/n): ")
        if rematch == "y":
            continue
        elif rematch == "n":
            break
    if guess == "paper" and choice == "paper":
        print("Copy cat!")
        continue

# scissors options
    if guess == "scissors" and choice == "paper":
        print("URGHHHH YOU DEFEATED ME!!!!!")
        rematch = input("I challenge you to a rematch, that's if your not scared!? (y/n): ")
        if rematch == "y":
            continue
        elif rematch == "n":
            break
    if guess == "scissors" and choice == "rock":
        rematch = input("Haaa! I win! Want to play again? (y/n): ")
        if rematch == "y":
            continue
        elif rematch == "n":
            break
    if guess == "scissors" and choice == "scissors":
        print("Copy cat!")
        continue

