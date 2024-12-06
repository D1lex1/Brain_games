import prompt

from brain_games.consts import ROUNDS_NUMBER


def engine(game_values, start_question):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{start_question}')

    for round in range(ROUNDS_NUMBER):
        question, correct_answer = game_values()
        user_answer = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
