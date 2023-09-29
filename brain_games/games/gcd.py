import math
from brain_games.core import get_answer_by_user, print_question
from brain_games.utils import get_random_number


game_rules = "Find the greatest common divisor of given numbers."


def make_question():
    first_number = get_random_number()
    second_number = get_random_number()
    print_question(first_number, second_number)
    user_answer = get_answer_by_user()
    correct_result = math.gcd(first_number, second_number)
    is_valid_answer = int(user_answer) == correct_result
    return is_valid_answer, user_answer, correct_result
