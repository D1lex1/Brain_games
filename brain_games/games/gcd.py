import random
from math import gcd
from brain_games.game_launcher import start_game


def game_output():
    result = []
    for rounds in range(3):
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        question = f"{num1} {num2}"
        result.append((str(gcd(num1, num2)), question))
    return result


def run_gcd_game():
    start_game(game_output(), 2)
