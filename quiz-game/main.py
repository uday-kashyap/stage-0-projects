questions = {
    "Name the tallest buliding in the world.": "Burj Khalifa",
    "In which country the tallest statue of the world situated?": "India",
    "Name the protagonist in the movie franchise 'Dhurandhar'.": "Ranveer Singh",
    "How many countries are there in the world?": "195",
    "Name the world's busiest oil shipping route.": "Strait Of Hormuz"
}

points = 0
for question in questions:
    print("Question:", question)
    answer = input("Enter your answer: ").title()

    if answer == questions[question]:
        print("Congrats! You guessed it right.")
        points += 1

    else:
        print("Sorry! The correct answer is:", questions[question])
    
    print()

print(f"You answered {points} / {len(questions)} questions right.")