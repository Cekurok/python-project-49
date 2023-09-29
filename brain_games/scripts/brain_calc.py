from brain_games.core import start_game
from brain_games.games.calc import game_rules, make_question


def main():
    start_game(game_rules, make_question)


if __name__ == '__main__':
    main()
