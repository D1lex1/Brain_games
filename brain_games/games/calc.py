import random
from brain_games.game_launcher import start_game


def calc():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    return num1, num2, operation


def game_output():
    result = []
    for rounds in range(3):
        num1, num2, operation = calc()
        question = (f"{num1} {operation} {num2}")
        if operation == "+":
            result.append((str(num1 + num2), question))
        elif operation == "-":
            result.append((str(num1 - num2), question))
        else:
            result.append((str(num1 * num2), question))
    return result


def run_calc_game():
    start_game(game_output(), 0)
