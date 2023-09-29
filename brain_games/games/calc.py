from random import choice
from brain_games.core import get_answer_by_user, print_question
from operator import add, sub, mul
from brain_games.utils import get_random_number

game_rules = "What is the result of the expression?"
OPERATORS = {"+": add, "-": sub, "*": mul}


def get_expression_result(exp, first_number, second_number):
    result = 0
    match exp:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
    return result


def make_question():
    first_number, second_number = get_random_number(), get_random_number()
    expression = choice(list(OPERATORS.keys()))
    print_question(first_number, expression, second_number)
    user_answer = get_answer_by_user()
    correct_result = get_expression_result(expression,
                                           first_number,
                                           second_number)
    is_valid_answer = int(user_answer) == correct_result
    return is_valid_answer, user_answer, correct_result
