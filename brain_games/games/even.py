#!/usr/bin/env python3
import random
import prompt
from brain_games.cli import is_number_even


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_answer():
    even_number = random.randint(1, 20)
    print(f'Question: {even_number}')
    answer = prompt.string('Your answer: ')
    result = is_number_even(even_number)
    is_true = answer == result
    return is_true, answer, result
