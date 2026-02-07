# Python Banking Program

# Main UI 1. Show Balance 2. Deposit 3. Withdraw 4. Exit Enter Choice

# main game
def starter_menu():
    print("Welcome to the 7-11 Banking Game!")
    print("------------------------------------")
    print("1. Quick Tutorial")
    print("2. Start Game")
    print("------------------------------------")
    starter_choice = int(input("Your choice: "))

    match starter_choice:
        case 1:
            tutorial()
        case 2:
            pass

def tutorial():
    print("Hello newcomer! This program simulates the 7-11 dice game by rolling two dice, ")
    print("adding their values, and checking the result. ")
    print("If the total is 7 or 11, the player wins; otherwise, they lose. ")
    print("The dice rolls and outcome are displayed to the user.")

    print(" ")

    print("The dice game 7-11 is traditionally a street gambling game so we will also simulate some currency, our money will be chicken nuggets")

starter_menu()