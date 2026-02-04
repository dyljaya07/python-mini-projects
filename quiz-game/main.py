# Python Quiz Game

questions = ("What year is it?: ",
             "How many elements are in the periodic table?: ",
             "How many wheels are on a standard bicycle?: ",
             "How many months are in a year?: ",
             "How many days are in a year?: ")

options = (("A. 2011", "B. 2024", "C. 2026", "D. 2016"),
           ("A. 117", "B. 118", "C. 120", "D. 132"),
           ("A. 2", "B. 3", "C. 4", "D. 2.5"),
           ("A. 11", "B. 10", "C. 19", "D. 12"),
           ("A. 375", "B. 362", "C. 367", "D. 365"))

answers = ("C", "B", "A", "D", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
    question_num += 1

print(f"Your final score is: {score}/{len(questions)}")
