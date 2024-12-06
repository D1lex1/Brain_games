from brain_games.consts import EVEN_INSTRUCTION
from brain_games.engine import engine
from brain_games.utilities import get_random_num


def is_even(number):
    return number % 2 == 0


def get_problem_number_and_answer():
    problem_num = get_random_num(1, 100)
    correct_answer = 'yes' if is_even(problem_num) else 'no'
    return problem_num, correct_answer


def run_even_game():
    engine(get_problem_number_and_answer, EVEN_INSTRUCTION)
