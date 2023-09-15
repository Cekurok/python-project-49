#!/usr/bin/env python3
import random
import prompt


def is_number_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_answer():
    even_number = random.randint(1, 20)
    print(f'Question: {even_number}')
    answer = prompt.string('Your answer: ')
    result = is_number_even(even_number)
    is_true = answer == result
    return is_true, answer, result
