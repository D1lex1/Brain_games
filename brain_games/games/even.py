import random
from brain_games.game_launcher import start_game


def is_even(number):
    return True if number % 2 == 0 else False


def game_output():
    result = []
    for rounds in range(3):
        question = random.randint(1, 100)
        if is_even(question):
            result.append(('yes', question))
        else:
            result.append(('no', question))
    return result


def run_even_game():
    start_game(game_output(), 1)
