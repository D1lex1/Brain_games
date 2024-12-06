from brain_games.consts import PRIME_INSTRUCTION
from brain_games.engine import engine
from brain_games.utilities import get_random_num


def is_prime(num):
    return False if num < 2 else all(
        num % i != 0 for i in range(2, int(num**0.5) + 1)
    )


def get_problem_number_and_answer():
    problem_num = get_random_num(1, 100)
    correct_answer = 'yes' if is_prime(problem_num) else 'no'
    return problem_num, correct_answer


def run_prime_game():
    engine(get_problem_number_and_answer, PRIME_INSTRUCTION)
