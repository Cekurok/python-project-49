#!/usr/bin/env python3
import random
import prompt


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_answer():
    even_number = random.randint(1, 30)
    print(f'Question: {even_number}')
    answer = prompt.string('Your answer: ')
    result = is_prime(even_number)
    if result:
        result = "yes"
    else:
        result = "no"
    is_true = answer == result
    return is_true, answer, result
