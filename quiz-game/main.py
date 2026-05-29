import requests
import html
import random
import time

# Constants
TOTAL_QUESTIONS = 10
QUESTION_TYPE = "Multiple Choice"
POINTS_PER_QUESTION = 1

# Game Header
print("Welcome to the Quiz Game!")
print(F"Total set of questions: {TOTAL_QUESTIONS}")
print(F"Questions type: {QUESTION_TYPE}")
print(f"'+{POINTS_PER_QUESTION}' for each correct answer.")
print()

# Parse data
url = f"https://opentdb.com/api.php?amount={TOTAL_QUESTIONS}&difficulty=easy&type=multiple"
response = requests.get(url, timeout=5)

if response.status_code != 200:
    print("Server Error! Data could not be fetched.")
    exit()

data = response.json()

if data['response_code'] != 0:
    print("API returned an invalid response.")
    exit()

entries = data['results']

# Game Logic
points = 0

for entry in entries:
    question = html.unescape(entry['question'])
    category = html.unescape(entry['category'])

    print(f"Question: {question}")
    print(f"Category: {category}")
    print()

    correct_answer = html.unescape(entry['correct_answer'])
    incorrect_answers = [html.unescape(incorrect_answer) for incorrect_answer in entry['incorrect_answers']]

    incorrect_answers.extend([correct_answer])
    random.shuffle(incorrect_answers)

    options = incorrect_answers

    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
        
    print()

    while True:

        try:
            choice = int(input("Choose the correct option: "))

            if choice not in range(1, 5):
                print("Please enter a valid option.")
                print()
                continue
        
            break # Exit loop on valid input

        except ValueError:
            print(f"Invalid Input! Options must be integers.")
            print()
            

    if options[choice - 1] == correct_answer:
        print("Congrats! Right answer.")
        points += POINTS_PER_QUESTION
    
    else:
        print(f"Sorry, the correct answer is '{correct_answer}'.")
    
    print()

    time.sleep(1) # Wait before displaying next question

# Goodbye text
print("Game Over!")
print(f"You have guessed {points} / 10 questions correctly.")