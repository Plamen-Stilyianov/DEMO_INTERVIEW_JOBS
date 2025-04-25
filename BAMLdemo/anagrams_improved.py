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
from concurrent.futures import ThreadPoolExecutor


class Anagrams(object):
    """ Anagram class """
    __text = ''

    @classmethod
    def __get_text(cls):
        with open('words.txt') as f:
            text = tuple(line.rstrip(line[-1:]) for line in f.readlines())
            return text

    def __init__(self):
        self.lock = threading.RLock()

    def __new__(cls, *args, **kwargs):
        instance = super(Anagrams, cls).__new__(cls)
        cls.__text = cls.__get_text() if not cls.__text else cls.__text
        instance._text = cls.__text
        return instance

    def get_anagrams(self, word):
        """ Method which gets a word as a parameter and returns anagram combination of words
            Thread safe and optimised by sorted and words length restriction of the collection iteration
        """
        with self.lock:
            sorted_word = sorted(word)
            len_word = len(word)
            anagrams = [words for words in self._text if len(words) == len_word and sorted(words) == sorted_word]
            # anagrams = map(lambda words: words, filter(lambda words: (len(words) == len_word and sorted(words) == sorted_word), self.text))
            return anagrams


class TestAnagrams(unittest.TestCase):

    def setUp(self):
        self.anagrams = Anagrams()

    def test_anagrams(self):
        """" Testing anagram logic """
        self.assertEqual(self.anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(self.anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])
        self.assertEqual(self.anagrams.get_anagrams('nameless'), ['lameness', 'maleness', 'nameless', 'salesmen'])
        self.assertEqual(self.anagrams.get_anagrams('trainers'),
                         ['restrain', 'retrains', 'strainer', 'terrains', 'trainers'])
        self.assertEqual(self.anagrams.get_anagrams('caters'),
                         ['caster', 'caters', 'crates', 'reacts', 'recast', 'traces'])
        self.assertEqual(self.anagrams.get_anagrams('pears'),
                         ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])

    def test_thread_safety(self):
        """ Testing thread safety of the methods of the anagram class instance """

        test_cases = {'pears': ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'],
                      'caters': ['caster', 'caters', 'crates', 'reacts', 'recast', 'traces'],
                      'trainers': ['restrain', 'retrains', 'strainer', 'terrains', 'trainers'],
                      'nameless': ['lameness', 'maleness', 'nameless', 'salesmen'],
                      'eat': ['ate', 'eat', 'tea'],
                      # 'plates': ['palest', 'pastel', 'petals', 'plates', 'staple'],
                      }
        with ThreadPoolExecutor(max_workers=6) as pool:
            for test in test_cases.items():
                future = pool.submit(self.anagrams.get_anagrams, test[0])
                self.assertEqual(test[1], future.result())


if __name__ == '__main__':
    unittest.main()
