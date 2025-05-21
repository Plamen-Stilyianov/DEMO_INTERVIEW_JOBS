# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval - Done!
#   - Write more tests - Done!
#   - Thread safe implementation - Done!

import threading
import unittest
from unittest.mock import patch, mock_open
from multiprocessing.pool import ThreadPool


class Anagrams(object):
    """ Anagram class """
    def __init__(self):
        self.lock = threading.RLock()
        self.words = self._get_words('words.txt')

    def _get_words(self, words_file):
        """ Method which read a file and returns sorted by word length tuple collection.
            Thread safe and optimized for next stage.
        """
        with open(words_file) as f:
            words = [item.rstrip() for item in f.readlines()]
            words.sort(key=len, reverse=False)
            return tuple(words)

    def get_anagrams(self, word):
        """ Method which gets a word as a parameter and returns anagram combination of words
            Thread safe and optimised by sorted and words length restriction of the collection iteration
        """
        with self.lock:
            anagrams = list()
            sorted_word = sorted(word)
            length_word = len(word)
            for w in [words for words in self.words if len(words) == length_word]:
                if sorted(w) == sorted_word:
                    anagrams.append(w)
            return anagrams


class TestAnagrams(unittest.TestCase):

    def setUp(self):
        self.anagrams = Anagrams()
        self.file_content = mock_open(
            read_data=(
                'firstline\n'
                'secondline\n'
                'thirdline\n'
            )
        )

    def test__get_words(self):
        """ Testing get_words method using mock file """
        with patch('builtins.open', self.file_content):
            expected = ('firstline', 'thirdline', 'secondline')
            actual = self.anagrams._get_words("dummy.txt")
            self.assertEqual(expected, actual)

    def test_anagrams(self):
        """ Testing anagram logic """
        self.assertEqual(self.anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(self.anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])
        self.assertEqual(self.anagrams.get_anagrams('nameless'), ['lameness', 'maleness', 'nameless', 'salesmen'])
        self.assertEqual(self.anagrams.get_anagrams('trainers'),
                          ['restrain', 'retrains', 'strainer', 'terrains', 'trainers'])
        self.assertEqual(self.anagrams.get_anagrams('caters'),
                          ['caster', 'caters', 'crates', 'reacts', 'recast', 'traces'])
        self.assertEqual(self.anagrams.get_anagrams('pears'),
                          ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])

    def test_anagrams_thread_safety(self):
        """ Testing thread safety of the methods of the anagram class instance """
        pool = ThreadPool(processes=5)
        async_result_pears = pool.apply_async(self.anagrams.get_anagrams, ('pears',))
        self.assertEqual(['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'], async_result_pears.get())

        async_result_caters = pool.apply_async(self.anagrams.get_anagrams, ('caters',))
        self.assertEqual(['caster', 'caters', 'crates', 'reacts', 'recast', 'traces'], async_result_caters.get())

        async_result_trainers = pool.apply_async(self.anagrams.get_anagrams, ('trainers',))
        self.assertEqual(['restrain', 'retrains', 'strainer', 'terrains', 'trainers'], async_result_trainers.get())

        async_result_nameless = pool.apply_async(self.anagrams.get_anagrams, ('nameless',))
        self.assertEqual(['lameness', 'maleness', 'nameless', 'salesmen'], async_result_nameless.get())

        async_result_eat = pool.apply_async(self.anagrams.get_anagrams, ('eat',))
        self.assertEqual(['ate', 'eat', 'tea'], async_result_eat.get())


if __name__ == '__main__':
    unittest.main()
