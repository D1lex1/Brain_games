from brain_games.consts import PROGRESSION_INSTRUCTION
from brain_games.engine import engine
from brain_games.utilities import get_random_num


def progression():
    progression_step = get_random_num(1, 5)
    progression_lenght = get_random_num(5, 10)
    progression_list = []
    progression_start = get_random_num(0, 25)
    while progression_lenght != 0:
        progression_list.append(progression_start)
        progression_start += progression_step
        progression_lenght -= 1
    progression_str = ' '.join([str(num) for num in progression_list])
    return progression_list, progression_str


def game_output():
    progression_list, progression_str = progression()
    correct_answer = progression_list[
        get_random_num(0, len(progression_list) - 1)
    ]
    question = progression_str.replace(str(correct_answer), '..', 1)
    return question, str(correct_answer)


def run_progression_game():
    engine(game_output, PROGRESSION_INSTRUCTION)
