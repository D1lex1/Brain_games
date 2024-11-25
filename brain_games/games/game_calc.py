import random


START_QUESTION = 'What is the result of the expression?'


def calc():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    return num1, num2, operation


def game_output():
    num1, num2, operation = calc()
    question = (f"{max(num1, num2)} {operation} {min(num1, num2)}")
    correct_answer = str(eval(question))
    return correct_answer, question
