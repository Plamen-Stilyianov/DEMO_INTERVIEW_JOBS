# Write a function that, for a given input string, returns all
# anagrams found in the words file.
#
# Requirements:
# 1. Efficient implementation of get_anagrams().
# 2. Additional unit test coverage (with unittest or other framework).

import time
import unittest
from unittest.mock import patch, mock_open
from typing import Any, Generator, Callable


def profile(func) -> Callable:
    def wrapper(*args, **kwargs) -> None:
        print(func.__name__)
        s = time.time()
        func(*args, **kwargs)
        e = time.time()
        print("cost: {0}".format(e - s))

    return wrapper


class Anagrams:
    ''''Class for anagrams'''

    def __init__(self, words_file_path: str) -> None:
        self.words = self._get_words(words_file_path)

    def _get_words(self, words_file: str) -> Generator[tuple[str, ...], Any, None]:
        ''' Method which read a file and returns sorted by word length tuple collection.
        '''
        try:
            with open(words_file) as f:
                words = [item.rstrip(item[-1:]) for item in f.readlines()]
                words.sort(key=len, reverse=False)
                # return tuple(words)
                yield tuple(words)
        except IOError as ex:
            raise ex

    def get_anagrams(self, word: str) -> list:
        ''''Getting an anagrams collection for a specific word
        '''
        anagrams = []
        for w in [words for words in next(self.words) if len(words) == len(word)]:
            if sorted(w) == sorted(word):
                anagrams.append(w)
        return anagrams


class TestAnagrams(unittest.TestCase):

    def setUp(self) -> None:
        self.anagrams = Anagrams('ms_words.txt')
        self.file_content = mock_open(
            read_data=(
                'firstline\n'
                'secondline\n'
                'thirdline\n'
            )
        )

    @profile
    def test__get_words(self):
        ''' Testing get_words method using mock file '''
        with patch('builtins.open', self.file_content):
            expected = ('firstline', 'thirdline', 'secondline')
            actual = self.anagrams._get_words("dummy.txt")
            self.assertEqual(expected, next(actual))

    @profile
    def test_anagrams_dictionary(self):
        self.assertEqual(
            self.anagrams.get_anagrams('dictionary'),
            ['dictionary', 'indicatory']
        )

    @profile
    def test_anagrams_plates(self):
        self.assertEqual(self.anagrams.get_anagrams('plates'),
                         ['palest', 'palets', 'pastel', 'petals', 'plates', 'pleats', 'septal', 'staple', 'tepals'])

    @profile
    def test_anagrams_eat(self):
        self.assertEqual(self.anagrams.get_anagrams('eat'), ['aet', 'ate', 'eat', 'eta', 'tae', 'tea'])


if __name__ == '__main__':
    unittest.main()
