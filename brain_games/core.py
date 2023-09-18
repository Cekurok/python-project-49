import prompt
from brain_games.cli import welcome_user


def error_message(you_text, correct_text):
    text = f"{you_text} is wrong answer ;(. Correct answer was {correct_text}."
    return text


def get_answer_by_user():
    answer = prompt.string('Your answer: ')
    return answer


def expression_result(exp, first_number, second_number):
    result = 0
    if exp == '+':
        result = first_number + second_number
    elif exp == '-':
        result = first_number - second_number
    elif exp == '*':
        result = first_number * second_number
    return result


def start_game(game):
    user_name = welcome_user()
    print(game.DESCRIPTION)
    COUNTER = 0
    while COUNTER < 3:
        is_true, answer, result = game.make_question()
        if is_true:
            print('Correct!')
            COUNTER += 1
        else:
            print(error_message(answer, result))
            print(f"Let's try again, {user_name}!")
            break
    if COUNTER == 3:
        print(f'Congratulations, {user_name}!')
