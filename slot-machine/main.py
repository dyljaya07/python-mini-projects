import random
import time

def spin_row():
    symbols = ["🍒", "🍉",  "🍋",  "🔔",  "⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 6
        elif row[0] == '⭐':
            return bet * 7
    return 0

def main():
    balance = 100

    print("*************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current balance: ${balance:.2f}")

        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...")
        print("-------------")
        time.sleep(1)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout:.2f}")
        else:
            print(f"Sorry, you lost")

        balance += payout

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != 'y':
            break

    print("***************************************************")
    print(f"Game over! Your final balance is ${balance:.2f}")
    print("***************************************************")

if __name__ == "__main__":
    main()