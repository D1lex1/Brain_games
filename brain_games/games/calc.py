from random import choice

from brain_games.consts import CALC_INSTRUCTION
from brain_games.engine import engine
from brain_games.utilities import get_random_num


def get_random_math_sign_and_result(num1, num2):
    return choice([
        ('+', num1 + num2),
        ('-', num1 - num2),
        ('*', num1 * num2)
    ])


def get_math_question_and_result():
    num1, num2 = get_random_num(1, 100), get_random_num(1, 100)
    operation, correct_answer = get_random_math_sign_and_result(num1, num2)
    question = f'{num1} {operation} {num2}'
    return question, str(correct_answer)


def run_calc_game():
    engine(get_math_question_and_result, CALC_INSTRUCTION)
