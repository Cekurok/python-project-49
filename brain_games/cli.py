import prompt


def welcome_user():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def is_number_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def error_message(you_text, correct_text):
    text = f"{you_text} is wrong answer ;(. Correct answer was {correct_text}."
    return text


def expression_result(exp, first_number, second_number):
    result = 0
    if exp == '+':
        result = first_number + second_number
    elif exp == '-':
        result = first_number - second_number
    elif exp == '*':
        result = first_number * second_number
    return result
