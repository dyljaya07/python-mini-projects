import random
print("Welcome to the number guessing game!")

name = input("What is your name?: ")

while True:
    high = int(input(f"Hello {name}! Please pick the highest number you want: "))
    low = int(input(f"Thanks {name}! Please pick the lowest number you want: "))

    if high <= low:
        print("Sorry, high must be greater than low. Please try again.\n")
    elif high <= 0:
        print("Sorry, high must be greater than 0. Please try again.\n")
    else:
        break

print(f"Great! Your range is {low} to {high}.")
print("Let's play the number guessing game!")
print("----------------------------------------")

number = random.randint(low, high)

while True:
    guess = int(input("Please pick a number: "))

    if guess == number:
        print("You guessed the number!")
        print("Thank you for playing! Goodbye!")
        break
    elif guess != number:
        print("Wrong guess. Try again!")
