import prompt


def greet():
    print("Welcome to the Brain Games!")
    name = prompt.string('Can i have your name? ')
    print(f'Hello, {name}')
    return name


def engine(name, correct_answer, question):
    print(f"Question: {question}")
    user_answer = prompt.string("Your answer: ")
    if correct_answer == user_answer:
        print("Correct!")
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}!")
        return True
