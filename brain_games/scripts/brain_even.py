#!/usr/bin/env python3
import random
import prompt
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        even_number = random.randint(1, 20)
        print(f'Question: {even_number}')
        answer = prompt.string('Your answer: ')
        is_even = is_number_even(even_number)
        if answer == is_even:
            print('Correct!')
            i += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {is_even}.")
            break
    if i == 3:
        print(f'Congratulations, {user_name}!')


def is_number_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


if __name__ == '__main__':
    main()
