import random
from math import gcd


START_QUESTION = 'Find the greatest common divisor of given numbers.'


def game_output():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = gcd(num1, num2)
    question = f"{num1} {num2}"
    return str(correct_answer), question
