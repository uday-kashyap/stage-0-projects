import requests
import html
import random
import time

# Constants
TOTAL_QUESTIONS = 10
QUESTION_TYPE = "Multiple Choice"
POINTS_PER_QUESTION = 1

def fetch_quiz_data():
    '''
    Parse and validate data.
    '''
    
    url = f"https://opentdb.com/api.php?amount={TOTAL_QUESTIONS}&difficulty=easy&type=multiple"

    try:
        response = requests.get(url, timeout=5)
    
    except requests.RequestException:
        print("Unable to connect to the server.")
        return

    if response.status_code != 200:
        print("Server Error! Data could not be fetched.")
        return

    data = response.json()

    if data['response_code'] != 0:
        print("API returned an invalid response.")
        return

    return data


def game_header():
    '''
    Display game header on the game session initialization.
    '''

    print("Welcome to the Quiz Game!")
    print(f"Total set of questions: {TOTAL_QUESTIONS}")
    print(f"Questions type: {QUESTION_TYPE}")
    print(f"'+{POINTS_PER_QUESTION}' for each correct answer.")
    print()


def user_input():
    '''
    Obtain and validate user input.
    '''
    
    while True:

        try:
            choice = int(input("Choose the correct option: "))

            if choice not in range(1, 5):
                print("Please enter a valid option.")
                print()
                continue
        
            return choice # Exit loop on valid input

        except ValueError:
            print(f"Invalid Input! Options must be integers.")
            print()


def run_quiz(raw_data):
    '''
    Main game logic.
    '''

    entries = raw_data['results']

    points = 0

    for entry in entries:
        question = html.unescape(entry['question'])
        category = html.unescape(entry['category'])

        print(f"Question: {question}")
        print(f"Category: {category}")
        print()

        correct_answer = html.unescape(entry['correct_answer'])
        incorrect_answers = [html.unescape(incorrect_answer) for incorrect_answer in entry['incorrect_answers']]

        incorrect_answers.append(correct_answer)
        random.shuffle(incorrect_answers)

        options = incorrect_answers

        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
            
        print()

        choice = user_input()

        if options[choice - 1] == correct_answer:
            print("Congrats! Right answer.")
            points += POINTS_PER_QUESTION
        
        else:
            print(f"Sorry, the correct answer is '{correct_answer}'.")
        
        print()

        time.sleep(1) # Wait before displaying next question

    return points


def goodbye_screen(score):
    '''
    Display goodbye text.
    '''

    print("Game Over!")
    print(f"You have guessed {score} / {TOTAL_QUESTIONS} questions correctly.")


def main():

    game_header()
    raw_data = fetch_quiz_data()

    if raw_data is None:
        return
    
    total_points = run_quiz(raw_data)
    goodbye_screen(total_points)


if __name__ == '__main__':
    main()