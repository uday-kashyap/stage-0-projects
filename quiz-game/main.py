import requests
import html
import random
import time

# Game Header
print("Welcome to the Quiz Game!")
print("Total set of questions: 10")
print("Questions type: Multiple Choice Questions")
print("'+1' for each correct answer.")
print()

# Parse data
url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple"
response = requests.get(url)
data = response.json()
entries = data['results']

# Game Logic
points = 0

for entry in entries:
    question = html.unescape(entry['question'])
    category = html.unescape(entry['category'])

    print(f"Question: {question}")
    print(f"Category: {category}")
    print()

    correct_answer = entry['correct_answer']
    incorrect_answers = entry['incorrect_answers']

    incorrect_answers.extend([correct_answer])
    random.shuffle(incorrect_answers)

    options = incorrect_answers

    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
        
    print()

    choice = int(input("Choose the correct option: "))

    if options[choice - 1] == correct_answer:
        print("Congrats! Right answer.")
        points += 1
    
    else:
        print(f"Sorry, the correct answer is '{correct_answer}'.")
    
    print()

    time.sleep(1) # Wait before displaying next question

# Goodbye text
print("Game Over!")
print(f"You have guessed {points} / 10 questions correctly.")