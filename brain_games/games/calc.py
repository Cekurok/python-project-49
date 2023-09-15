#!/usr/bin/env python3
import random
import prompt
from brain_games.cli import expression_result


def get_rules():
    return 'What is the result of the expression?'


def get_answer():
    first_number = random.randint(1, 200)
    second_number = random.randint(1, 200)
    expression = ['-', '+', '*'][random.randint(0, 2)]
    print(f'Question: {first_number} {expression} {second_number}')
    answer = prompt.string('Your answer: ')
    result = expression_result(expression, first_number, second_number)
    is_true = int(answer) == result
    return is_true, answer, result
