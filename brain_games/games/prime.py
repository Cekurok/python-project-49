from brain_games.core import get_answer_by_user, print_question
from brain_games.utils import get_random_number


game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def make_question():
    even_number = get_random_number(start=2, finish=99)
    print_question(even_number)
    answer = get_answer_by_user()
    result = "yes" if is_prime(even_number) else "no"
    is_valid_answer = answer == result
    return is_valid_answer, answer, result
