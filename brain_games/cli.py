import prompt


def user_name():
    name = prompt.string('May I have your name? ')
    return name


def welcome_user():
    name = user_name()
    print(f'Hello, {name}')
