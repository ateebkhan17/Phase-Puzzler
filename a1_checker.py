"""A simple checker for types of functions in puzzler_functions.py."""

from typing import Any, Dict
import unittest
import checker_generic
import puzzler_functions as pf

FILENAME = 'puzzler_functions.py'
PYTA_CONFIG = 'pyta/a1_pyta.txt'
TARGET_LEN = 79
SEP = '='

CONSTANTS = {
    'CONSONANT_POINTS': 1, 'VOWEL_PRICE': 1, 'CONSONANT_BONUS': 2,
    'PLAYER_ONE': 'Player One', 'PLAYER_TWO': 'Player Two',
    'CONSONANT': 'C', 'VOWEL': 'V', 'SOLVE': 'S', 'QUIT': 'Q',
    'HUMAN': 'H-', 'HUMAN_HUMAN': 'HH', 'HUMAN_COMPUTER': 'HC',
    'EASY': 'E', 'HARD': 'H',
    'ALL_CONSONANTS': 'bcdfghjklmnpqrstvwxyz', 'ALL_VOWELS': 'aeiou',
    'PRIORITY_CONSONANTS': 'tnrslhdcmpfygbwvkqxjz', 'HIDDEN': '^'
}


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    def test_is_win(self) -> None:
        """Function is_win."""

        self._check(pf.is_win, ['banana', 'banana'], bool)

    def test_is_game_over(self) -> None:
        """Function is_game_over."""

        self._check(pf.is_game_over, ['abc', 'abc', 'C'], bool)

    def test_is_one_player_game(self) -> None:
        """Function is_one_player_game."""

        self._check(pf.is_one_player_game, ['HC'], bool)

    def test_is_human(self) -> None:
        """Function is_human."""

        self._check(pf.is_human, ['Player One', 'HH'], bool)

    def test_current_player_score(self) -> None:
        """Function current_player_score."""

        self._check(pf.current_player_score, [1, 2, 'Player One'], int)

    def test_is_bonus_letter(self) -> None:
        """Function is_bonus_letter."""

        self._check(pf.is_bonus_letter, ['a', 'apple', '^^^le'], bool)

    def test_update_char_view(self) -> None:
        """"Function update_char_view."""

        self._check(pf.update_char_view, ['apple', '^^^le', 0, 'a'], str)

    def test_calculate_score(self) -> None:
        """Function calculate_score."""

        self._check(pf.calculate_score, [4, 3, 'C'], int)

    def test_next_player(self) -> None:
        """Function next_player."""

        self._check(pf.next_player, ['Player One', 0, 'HH'], str)

    def test_is_hidden(self) -> None:
        """Function is_hidden."""

        self._check(pf.is_hidden, [1, 'apple', '^^^le'], bool)

    def test_computer_chooses_solve(self) -> None:
        """Function computer_chooses_solve."""

        self._check(pf.computer_chooses_solve, ['a^^le', 'H', 'pgh'], bool)

    def test_erase(self) -> None:
        """Function erase."""

        self._check(pf.erase, ['abc', 1], str)

    def test_check_constants(self) -> None:
        """Values of constants."""

        print('\nChecking that constants refer to their original values')
        self._check_constants(CONSTANTS, pf)
        print('  check complete')

    def _check(self, func: callable, args: list, ret_type: type) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.

        """

        print('\nChecking {}...'.format(func.__name__))
        result = checker_generic.check(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        print('  check complete')

    def _check_constants(self, name2value: Dict[str, object], mod: Any) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in name2value.items():
            actual = getattr(mod, name)
            msg = 'The value of constant {} should be {} but is {}.'.format(
                name, expected, actual)
            self.assertEqual(expected, actual, msg)


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
unittest.main(exit=False)
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style')
print('  - checking type contract\n')
