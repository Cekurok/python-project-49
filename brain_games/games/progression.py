#!/usr/bin/env python3
from random import randint
import prompt


def get_rules():
    return 'What number is missing in the progression?'


def get_answer():
    res = []
    initial_number, difference = randint(0, 50), randint(0, 50)
    length = 10
    for index in range(length):
        initial_number += difference
        res.append(initial_number)
    random_index = randint(0, 9)
    correct_answer = str(res[random_index])
    res[random_index] = ".."
    res = " ".join(str(i) for i in res)
    print(f'Question: {res}')
    answer = prompt.string('Your answer: ')
    is_true = answer == correct_answer
    return is_true, answer, correct_answer
