import prompt
import sys


ITERATIONS = 3


def greet():
    name = prompt.string("Welcome to the Brain Games!\n"
                         "Can i have your name? ")
    print(f'Hello, {name}')
    return name


def engine(correct_answer, question, name):
    print(f"Question: {question}")
    user_answer = prompt.string("Your answer: ")
    if correct_answer == user_answer:
        print("Correct!")
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
        sys.exit()


def start_game(correct_answer, question):
    name = greet()
    for round in range(ITERATIONS):
        engine(correct_answer, question, name)
    print(f"Congratulations, {name}!")
