import prompt


def print_question(*values):
    text = "Question:"
    for va in values:
        text = f"{text} {va}"
    print(text)


def get_user_name_and_print_welcome():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name


def print_error_message(you_text, correct_text):
    text = f"{you_text} is wrong answer ;(. Correct answer was {correct_text}."
    return text


def get_answer_by_user():
    answer = prompt.string("Your answer: ")
    return answer


def start_game(description, load_game):
    user_name = get_user_name_and_print_welcome()
    print(description)
    for _ in range(3):
        is_true_str, answer, result = load_game()
        if is_true_str:
            print("Correct!")
        else:
            print(print_error_message(answer, result))
            print(f"Let's try again, {user_name}!")
            break
        print(f"Congratulations, {user_name}!")
