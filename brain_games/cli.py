import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


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


def game(get_rules, get_answer):
    user_name = welcome_user()
    print(get_rules())
    i = 0
    while i < 3:
        is_true, answer, result = get_answer()
        if is_true:
            print('Correct!')
            i += 1
        else:
            print(error_message(answer, result))
            print(f"Let's try again, {user_name}!")
            break
    if i == 3:
        print(f'Congratulations, {user_name}!')
