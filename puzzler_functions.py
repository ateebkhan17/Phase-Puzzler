"""CSC108/CSCA08: Fall 2020 -- Assignment 1: Phrase Puzzler

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Mario Badr, Jennifer Campbell, Tom Fairgrieve,
Diane Horton, Michael Liut, Jacqueline Smith, and Anya Tafliovich.

"""

from constants import (CONSONANT_POINTS, VOWEL_PRICE, CONSONANT_BONUS,
                       PLAYER_ONE, PLAYER_TWO, CONSONANT, VOWEL,
                       SOLVE, QUIT, HUMAN, HUMAN_HUMAN,
                       HUMAN_COMPUTER, EASY, HARD, ALL_CONSONANTS,
                       ALL_VOWELS, PRIORITY_CONSONANTS, HIDDEN)


# We provide this function as an example.
def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle and view are a winning
    combination. That is, if and only if puzzle and view are the same.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    >>> is_win('apple', 'app')
    False
    """

    return puzzle == view


# We provide this function as an example of using a function as a helper.
def is_game_over(puzzle: str, view: str, move: str) -> bool:
    """Return True if and only if puzzle and view are a winning
    combination or move is QUIT.

    >>> is_game_over('apple', 'a^^le', 'V')
    False
    >>> is_game_over('apple', 'a^^le', 'Q')
    True
    >>> is_game_over('apple', 'apple', 'S')
    True
    """

    return move == QUIT or is_win(puzzle, view)

def is_one_player_game(current_player: str) -> bool:
    """Return True if and only if current_player is a one-player game.

    >>> is_one_player_game('H-')
    True
    >>> is_one_player_game('HH')
    False
    >>> is_one_player_game('HC')
    False
    """

    return current_player == HUMAN


# We provide the header and docstring of this function as an example
# of where and how to use constants in the docstring.
def is_human(current_player: str, game_type: str) -> bool:
    """Return True if and only if current_player represents a human in a
    game of type game_type.

    current_player is PLAYER_ONE or PLAYER_TWO.
    game_type is HUMAN, HUMAN_HUMAN, or HUMAN_COMPUTER.

    In a HUMAN game or a HUMAN_HUMAN game, a player is always
    human. In a HUMAN_COMPUTER game, PLAYER_ONE is human and
    PLAYER_TWO is computer.

    >>> is_human('Player One', 'H-')
    True
    >>> is_human('Player One', 'HH')
    True
    >>> is_human('Player Two', 'HH')
    True
    >>> is_human('Player One', 'HC')
    True
    >>> is_human('Player Two', 'HC')
    False
    """

    if game_type == HUMAN or game_type == HUMAN_HUMAN:
        return True
    elif game_type == HUMAN_COMPUTER:
        return current_player == PLAYER_ONE
    return None

def current_player_score(score_player_one: int, score_player_two: int,
                         current_player: str) -> int:
    """Returns the score of the current player whose turn it is.
    score_player_one represents the score of PLAYER_ONE and score_player_two
    represets the score of PLAYER_TWO."

    >>> current_player_score (1,5,'Player One')
    1
    >>> current_player_score (1,5,'Player Two')
    5
    """
    if current_player == PLAYER_ONE:
        return score_player_one
    else:
        return score_player_two

def is_bonus_letter(letter: str, puzzle: str, view: str) -> bool:
    """Return True if and only if the first arguement (letter) is a bonus
    letter. Bonus letters are consonants that are HIDDEN. If letter
    is not True and in puzzle then return False.

    >>> is_bonus_letter ('a','ball','^a^^')
    False
    >>> is_bonus_letter ('m','mall','^all')
    True
    """
    return letter not in view and letter in puzzle


def update_char_view(puzzle: str, view: str, char_index: int, guess:
                     str) -> str:
    """Returns the updated view of what the character should be. When the
    player guesses the character right, then the new character is revealed.
    However, if the guess is wrong, then the view stays the same.

    >>> update_char_view ('leafs', 'l^afs', 1, 'e')
    'e'
    >>> update_char_view ('maple', '^^ple', 1, 'c')
    '^'
    """
    if puzzle[char_index] == guess:
        return guess
    else:
        return view[char_index]

def calculate_score(current_score: int, num_of_occurences: int, current_move:
                    str) -> int:
    """Returns the new updated current_score. Note that only when the player
    guesses a consonant that their score increases by CONSONANT_POINTS,
    depending on how many letters are guessed. However, buying a vowel
    decreases the score by VOWEL_PRICE.

    >>> calculate_score(1,2,'C')
    3
    >>> calculate_score(1,1,'V')
    0
    >>> calculate_score(2,0,'C')
    2
    """
    if current_move == CONSONANT:
        return current_score + num_of_occurences
    else:
        return current_score - VOWEL_PRICE

def next_player(current_player: str, num_of_occurences: int, type_of_game:
                str) -> str:
    """Returns which player plays next turn, either PLAYER_ONE or PLAYER_TWO.
    If current_player guesses a CONSONANT or VOWEL then they get to play again.
    However, if they guess incorrectly, then it's the next player's turn.

    >>> next_player('Player One', 0, 'H-')
    'Player One'
    >>> next_player('Player One', 1, 'H-')
    'Player One'
    >>> next_player('Player One', 1, 'HH')
    'Player One'
    >>> next_player('Player One', 0, 'HH')
    'Player Two'
    >>> next_player('Player Two', 0, 'HH')
    'Player One'
    >>> next_player('Player Two', 5, 'HH')
    'Player Two'
    """
    if num_of_occurences > 0 or type_of_game == HUMAN:
        return current_player
    elif current_player == PLAYER_ONE:
        return PLAYER_TWO
    return PLAYER_ONE


def is_hidden(char_index: int, puzzle: str, view: str) -> bool:
    """Returns True if and only if the character at char_index is currently
    HIDDEN in puzzle. A hidden character cannot be revealed at any location in
    the view.

    >>> is_hidden(4,'maple','ma^^^')
    True
    >>> is_hidden(4,'maple','^^ple')
    False
    """
    return puzzle[char_index] not in view


def computer_chooses_solve(view: str, difficulty: str, unguess_consonants:
                           str) -> bool:
    """Returns True if and only if the computer decides to solve the puzzle.
    For difficulty HARD, half of the view must be revealed or
    unguess_consonants must be 0. For difficulty EASY, the computer chooses
    to solve if there are no unguess_consonants to choose from.

    Precondition: Assume function is only called in a human-computer game.

    >>> computer_chooses_solve('mapl^','H','')
    True
    >>> computer_chooses_solve('m^^^^','H','rghtjkvd')
    False
    >>> computer_chooses_solve('mapl^','E','')
    True
    >>> computer_chooses_solve('m^^^^','E','rghtjkvd')
    False
    """
    if (difficulty == HARD) and (unguess_consonants == '' or
                                 view == half_revealed(view)):
        return True
    elif difficulty == EASY and unguess_consonants == '':
        return True
    return False


# Helper.
def half_revealed(view: str) -> bool:
    """Return True if and only if at least half of the alphabetic
    characters in view are revealed.

    >>> half_revealed('')
    True
    >>> half_revealed('x')
    True
    >>> half_revealed('^')
    False
    >>> half_revealed('a^,^c!')
    True
    >>> half_revealed('a^b^^e ^c^d^^d')
    False
    """

    num_hidden = view.count(HIDDEN)
    num_alphabetic = 0
    for char in view:
        if char.isalpha():
            num_alphabetic += 1
    return num_alphabetic >= num_hidden

def erase(letters: str, index: int) -> str:
    """Returns the given letters with the character at the given index removed,
    if the index is a valid index for that string of letters. Otherwise, it
    should return the original string of letters unchanged.

    >>> erase('maple', 3)
    'mape'
    >>> erase('maple',6)
    'maple'
    """
    if 0 <= index <= len(letters):
        return letters[0:index] + letters[1 + index:len(letters)]
    return letters

if __name__ == '__main__':
    import doctest
    doctest.testmod()
