#!/usr/bin/env python3
import random
import prompt


def gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return second_number


def get_rules():
    return 'Find the greatest common divisor of given numbers.'


def get_answer():
    first_number = random.randint(1, 200)
    second_number = random.randint(1, 200)
    print(f'Question: {first_number} {second_number}')
    answer = prompt.string('Your answer: ')
    result = gcd(first_number, second_number)
    is_true = int(answer) == result
    return is_true, answer, result
