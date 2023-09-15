#!/usr/bin/env python3
import random
import prompt


def get_rules():
    return 'What number is missing in the progression?'


def get_answer():
    res = []
    res_str = ""
    first_number = random.randint(1, 30)
    second_number = random.randint(2, 9)
    empty_symbol = random.randint(0, 9)
    for i in range(first_number, 200, second_number):
        if len(res) == 9:
            break
        if len(res) == empty_symbol:
            result = i
            res.append("..")
            continue
        res.append(i)
    for i in res:
        res_str = f"{res_str} {i}"
    print(f'Question: {res_str}')
    answer = prompt.string('Your answer: ')
    is_true = int(answer) == result
    return is_true, answer, result
