from brain_games.core import get_answer_by_user
from brain_games.utils import get_random_number


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def make_question():
    even_number = get_random_number(finish=30)
    print(f'Question: {even_number}')
    answer = get_answer_by_user()
    result = is_prime(even_number)
    if result:
        result = "yes"
    else:
        result = "no"
    is_valid_answer = answer == result
    return is_valid_answer, answer, result
