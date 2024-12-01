from brain_games.engine import engine, greet


START_QUESTIONS = ['What is the result of the expression?',
                   'Answer "yes" if the number is even, otherwise answer "no".',
                   'Find the greatest common divisor of given numbers.',
                   'Answer "yes" if given number is prime.'
                   ' Otherwise answer "no".',
                   'What number is missing in the progression?']


ITERATIONS = 3


def start_game(game_values, start_idx):
    name = greet()
    print(START_QUESTIONS[start_idx])
    for round in range(ITERATIONS):
        correct_answer, question = game_values[round]
        status = engine(name, correct_answer, question)
        if status:
            return
    print(f"Congratulations, {name}!")
