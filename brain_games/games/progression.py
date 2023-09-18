from random import randint
from brain_games.core import get_answer_by_user
from brain_games.utils import get_random_number


DESCRIPTION = 'What number is missing in the progression?'


def make_question():
    res = []
    initial_number = get_random_number(start=0, finish=50)
    difference = get_random_number(start=0, finish=50)
    length = 10
    for index in range(length):
        initial_number += difference
        res.append(initial_number)
    random_index = randint(0, 9)
    correct_answer = str(res[random_index])
    res[random_index] = ".."
    res = " ".join(str(i) for i in res)
    print(f'Question: {res}')
    user_answer = get_answer_by_user()
    is_valid_answer = user_answer == correct_answer
    return is_valid_answer, user_answer, correct_answer
