#!/usr/bin/env python3
from brain_games.cli import game
from brain_games.games.progression import get_answer, get_rules


def main():
    game(get_rules, get_answer)


if __name__ == '__main__':
    main()
