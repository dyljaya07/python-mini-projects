# Exercise 2 Shopping Cart Program

# Variables
item = input("Please enter the name of your item: ")
price = float(input("How much does this item cost?: "))
quantity = int(input("How many amounts of this item do you need?: "))

total = price * quantity

# Final Total
print(f"You are purchasing {quantity} amount(s) of the item; {item}")
print(f"Your total price is ${total}")
print("Enjoy your day!")