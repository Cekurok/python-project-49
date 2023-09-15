#!/usr/bin/env python3
import random
import prompt
from brain_games.cli import error_message, expression_result, welcome_user


def main():
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        first_number = random.randint(1, 200)
        second_number = random.randint(1, 200)
        expression = ['-', '+', '*'][random.randint(0, 2)]
        print(f'Question: {first_number} {expression} {second_number}')
        answer = prompt.string('Your answer: ')
        result = expression_result(expression, first_number, second_number)
        if int(answer) == result:
            print('Correct!')
            i += 1
        else:
            print(error_message(answer, result))
            print(f"Let's try again, {user_name}!")
            break
    if i == 3:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
