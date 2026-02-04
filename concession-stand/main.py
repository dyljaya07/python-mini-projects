# Concession Stand Program
menu = {"Pizza": 3.00,
              "Hamburger": 2.00,
              "Soda": 1.50,
              "Hot Dog": 3.50,
              "Nachos": 4.00,
              "Chicken Sandwich": 4.50,
              "Sonic Blue Curry": 100.00
              }
total = 0
cart = []

print("WELCOME TO THE WORLDS GREATEST CONCESSION STAND!")
print("--------   MENU   --------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----------  YOUR ORDER  --------------")
for food in cart:
    total += menu.get(food)
    print(food, end= " ")

print()
print(f"Total cost: ${total:.2f}")

