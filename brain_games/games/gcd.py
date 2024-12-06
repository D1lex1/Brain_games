from math import gcd

from brain_games.consts import GCD_INSTRUCTION
from brain_games.engine import engine
from brain_games.utilities import get_random_num


def get_nums_pair_and_gcd():
    first_num, second_num = get_random_num(1, 100), get_random_num(1, 100)
    nums_pair = f'{first_num} {second_num}'
    correct_answer = gcd(first_num, second_num)
    return nums_pair, str(correct_answer)


def run_gcd_game():
    engine(get_nums_pair_and_gcd, GCD_INSTRUCTION)
