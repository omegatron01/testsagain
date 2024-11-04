
quiz_questions = {
    "What is the capital of France?": {
        "A": "Berlin",
        "B": "Paris",
        "C": "London",
        "D": "Rome",
        "Answer": "B"
    },
    "Who painted the Mona Lisa?": {
        "A": "Leonardo da Vinci",
        "B": "Michelangelo",
        "C": "Raphael",
        "D": "Caravaggio",
        "Answer": "A"
    },
    "What is the largest planet in our solar system?": {
        "A": "Earth",
        "B": "Saturn",
        "C": "Jupiter",
        "D": "Uranus",
        "Answer": "C"
    }
}

def display_question(question):
    print(question)
    for option, value in quiz_questions[question].items():
        if option != "Answer":
            print(f"{option}: {value}")

def check_answer(question, user_answer):
    correct_answer = quiz_questions[question]["Answer"]
    if user_answer.upper() == correct_answer:
        return True
    else:
        return False

def quiz():
    """Main quiz function"""
    score = 0
    for question in quiz_questions:
        display_question(question)
        user_answer = input("Choose your answer: ")
        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {quiz_questions[question]['Answer']}.")
    print(f"\nQuiz finished! Your final score is {score}/{len(quiz_questions)}")

    if score >= len(quiz_questions) * 0.8:
        print("Excellent! You're a master!")
    elif score >= len(quiz_questions) * 0.6:
        print("Well done! You're on the right track!")
    else:
        print("Keep practicing! You've got this!")


quiz()