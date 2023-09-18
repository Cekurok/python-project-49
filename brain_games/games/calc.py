from random import choice
from brain_games.core import expression_result
from brain_games.core import get_answer_by_user
from operator import add, sub, mul
from brain_games.utils import get_random_number


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul
}


def make_question():
    first_number = get_random_number()
    second_number = get_random_number()
    expression = choice(list(OPERATORS.keys()))
    print(f'Question: {first_number} {expression} {second_number}')
    answer = get_answer_by_user()
    result = expression_result(expression, first_number, second_number)
    is_valid_answer = int(answer) == result
    return is_valid_answer, answer, result
