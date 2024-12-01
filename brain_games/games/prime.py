import random
from brain_games.game_launcher import start_game


def is_prime(num):
    return False if num < 2 else all(
        num % i != 0 for i in range(2, int(num**0.5) + 1)
    )


def game_output():
    result = []
    for rounds in range(3):
        question = random.randint(1, 100)
        if is_prime(question):
            result.append(('yes', question))
        else:
            result.append(('no', question))
    return result


def run_prime_game():
    start_game(game_output(), 3)
