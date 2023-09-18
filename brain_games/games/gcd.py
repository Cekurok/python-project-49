from brain_games.core import get_answer_by_user
from brain_games.utils import get_random_number


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return second_number


def make_question():
    first_number = get_random_number()
    second_number = get_random_number()
    print(f'Question: {first_number} {second_number}')
    answer = get_answer_by_user()
    result = gcd(first_number, second_number)
    is_valid_answer = int(answer) == result
    return is_valid_answer, answer, result
