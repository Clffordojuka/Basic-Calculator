# Name = "Ojuka"
# Favorite_color = "Blue"

# print(f"Hello {Name}, your Favorite_color is {Favorite_color}")

# def programmer_quiz():
#     questions = [
#          {"question": "What is the first program most programmers write?", "answer": "hello world"},
#          {"question": "Which language is known as the 'mother of all languages'?", "answer": "c"},
#          {"question": "What do programmers hate the most in their code?", "answer": "bugs"},
#     ]
#     print("Welcome to the Programmer Quiz!")
#     print("Type your answers. Let's see how many you get right!\n")
    
#     score = 0

#     for i, q in enumerate(questions):
#         print(f"Question {i + 1}: {q['question']}")
#         answer = input("Your answer: ").strip().lower()
#         if answer == q["answer"]:
#             print("Correct!")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer is '{q['answer']}'.")
#         print()

#     print(f"You scored {score}/{len(questions)}.")

#     play_again = input("Do you want to play again? (yes/no): ").strip().lower()
#     if play_again == "yes":
#         programmer_quiz()
#     else:
#         print("Thanks for playing! Goodbye!")

# # Start the game
# programmer_quiz()

# 

# Get user inputs
Fnumber = input("Enter First Number: ")
Lnumber = input("Enter Last Number: ")

# Convert inputs to numbers
Fnumber = float(Fnumber)
Lnumber = float(Lnumber)

# Perform the addition
sum = Fnumber + Lnumber
subtraction = Fnumber - Lnumber
multiplication = Fnumber * Lnumber
division = Fnumber / Lnumber

# Display the result
print(f"The sum of {Fnumber} and {Lnumber} is {sum}")
print(f"The sum of {Fnumber} and {Lnumber} is {subtraction}")
print(f"The sum of {Fnumber} and {Lnumber} is {multiplication}")
print(f"The sum of {Fnumber} and {Lnumber} is {division}")
