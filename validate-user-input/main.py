# Validating user input exercise

# Rules:
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

# onboarding
print("Welcome!")
print("Before you create a username, we have a couple rules!")
print("1. Username is no more than 12 characters!")
print("2. Username must not contain spaces!")
print("3. Username must not contain digits!")

# user-input
username = input("Please enter your username: ")

# checking username
if len(username) > 12:
    print("Your username must be no more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username must not contain spaces")
elif not username.isalpha():
    print("Your username must not contain any digits")
else:
    print(f"Welcome {username}")
