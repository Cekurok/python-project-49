from brain_games.core import get_answer_by_user, print_question
from brain_games.utils import get_random_number


game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even_str(num):
    return "yes" if num % 2 == 0 else "no"


def make_question():
    even_number = get_random_number(finish=20)
    print_question(even_number)
    user_answer = get_answer_by_user()
    correct_result = is_number_even_str(even_number)
    is_valid_answer = user_answer == correct_result
    return is_valid_answer, user_answer, correct_result
