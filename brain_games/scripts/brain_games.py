#!/usr/bin/env python3
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('Can i have your name? ')
    print(f'Hello, {name}')


if __name__ == '__main__':
    main()
