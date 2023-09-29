from brain_games.core import get_answer_by_user, print_question
from brain_games.utils import get_random_number


game_rules = "What number is missing in the progression?"
length = 10

def make_question():
    res = []
    initial_number = get_random_number(start=0, finish=50)
    difference = get_random_number(start=0, finish=50)
    for _ in range(length):
        initial_number += difference
        res.append(initial_number)
    random_index = get_random_number(start=0, finish=9)
    correct_answer = str(res[random_index])
    res[random_index] = ".."
    res = " ".join(str(i) for i in res)
    print_question(res)
    user_answer = get_answer_by_user()
    is_valid_answer = user_answer == correct_answer
    return is_valid_answer, user_answer, correct_answer
