from math import sqrt
from brain_games.core import get_answer_by_user
from brain_games.utils import get_random_number


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True


def make_question():
    even_number = get_random_number(start=2, finish=99)
    print(f'Question: {even_number}')
    answer = get_answer_by_user()
    result = is_prime(even_number)
    result = "yes" if result else "no"
    is_valid_answer = answer == result
    return is_valid_answer, answer, result
