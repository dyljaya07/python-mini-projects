# Python Banking Program

# Main UI 1. Show Balance 2. Deposit 3. Withdraw 4. Exit Enter Choice

# imports
import time
import random

# variables
money = 1000
first_roller = random.choice(["Player", "Opponent"])
people = ["Dylan", "Jeffery", "Lil Jeff", "Q50WLil50", "Big Capone", "King Von", "John Pork", "Lebron James"]
adjectives = ["scary", "notorious", "devious", "demonic", "cheating", "notable", "popular", "rich"]
story_lines = ["known to rob his opponent if he loses",
               "known to shoot his opponent out of anger",
               "known to cheat his dice rolls",
               "known to fart while he rolls for good luck"]

# main game
def starter_menu():
    print("Welcome to the 7-11 Banking Game!")
    print("------------------------------------")
    print("1. Quick Tutorial")
    print("2. Start Game")
    print("3. Quit")
    print("------------------------------------")

    starter_choice = int(input("Your choice: "))

    match starter_choice:
        case 1:
            tutorial()
            time.sleep(2)
            starter_menu()
        case 2:
            game()
        case 3:
            pass

def tutorial():
    print("Hello newcomer! This program simulates the 7-11 dice game by rolling two dice, ")
    print("adding their values, and checking the result. ")
    print("If the total is 7 or 11, the player wins; otherwise, they lose. ")
    print("The dice rolls and outcome are displayed to the user.")

    print(" ")

    print("The dice game 7-11 is traditionally a street gambling game so we will also simulate some currency, our money will be chicken nuggets")

def game():
    print("------------------------------------")
    print("1. Gamble")
    print("2. Bank Account")
    print("3. Tutorial")
    print("4. Quit")
    print("------------------------------------")

    menu_choice = int(input("Your choice: "))

    match menu_choice:
        case 1:
            gamble_game()
        case 2:
            pass
        case 3:
            tutorial()
        case 4:
            pass

def gamble_game():
    opponent = random.choice(people)

    print("------------------------------------")
    print(f"Your versing {opponent}")
    print(f"He's a {random.choice(adjectives)} opponent")
    print(f"Some people say he is {random.choice(story_lines)}!?")
    print("------------------------------------")
    gamble = int(input(f"{opponent}: How much money do you want to gamble!?: "))
    print(f"{opponent}: Only {gamble} chicken nuggets!? Pffft! Let's do it!")
    print("------------------------------------")

    if first_roller == "Opponent":
        print("A random homeless man barges in-between you too! He flips a coin!?")
        time.sleep(2)
        print(f"{opponent} wins the coinflip, he rolls first!")
        print("------------------------------------")
        dice_rolling()
    else:
        print("A random homeless man barges in-between you too! He flips a coin!?")
        time.sleep(2)
        print("Homeless Dude: You roll first young buck!")
        print("------------------------------------")
        dice_rolling()

def dice_rolling():
    pass

def main():
    starter_menu()


main()