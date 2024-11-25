#!/usr/bin/env python3
from prompt import string
import sys


ITERATIONS = 3


def greet():
    print("Welcome to the Brain Games!")
    name = string('Can i have your name? ')
    print(f'Hello, {name}')
    return name


def engine(correct_answer, question, name):
    print(f"Question: {question}")
    user_answer = string("Your answer: ")
    if correct_answer == user_answer:
        print("Correct!")
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
        sys.exit()


def start_game(game):
    name = greet()
    print(game.START_QUESTION)
    for round in range(ITERATIONS):
        correct_answer, question = game.game_output()
        engine(correct_answer, question, name)
    print(f"Congratulations, {name}!")
