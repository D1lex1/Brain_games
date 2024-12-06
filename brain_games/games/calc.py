from random import choice

from brain_games.consts import CALC_INSTRUCTION
from brain_games.engine import engine
from brain_games.utilities import get_random_num


def get_random_nums():
    num1, num2 = get_random_num(1, 100), get_random_num(1, 100)
    return num1, num2


def get_random_math_sign_and_result(num1, num2):
    return choice([
        ('+', num1 + num2),
        ('-', num1 - num2),
        ('*', num1 * num2)
    ])


def game_output():
    num1, num2 = get_random_nums()
    operation, correct_answer = get_random_math_sign_and_result(num1, num2)
    question = f'{num1} {operation} {num2}'
    return question, str(correct_answer)


def run_calc_game():
    engine(game_output, CALC_INSTRUCTION)
