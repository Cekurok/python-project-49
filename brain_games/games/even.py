from brain_games.core import get_answer_by_user
from brain_games.utils import get_random_number


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(num):
    return "yes" if num % 2 == 0 else "no"


def make_question():
    even_number = get_random_number(finish=20)
    print(f'Question: {even_number}')
    answer = get_answer_by_user()
    result = is_number_even(even_number)
    is_valid_answer = answer == result
    return is_valid_answer, answer, result
