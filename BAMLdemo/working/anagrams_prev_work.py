# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest
import threading


class Anagrams:

    def __init__(self):
        word = [item.rstrip(item[-1:]) for item in open('words.txt').readlines()]
        word.sort(key=len, reverse=False)
        self.words = tuple(word)
        self.lock = threading.RLock()

    def get_anagrams(self, word):
        self.lock.acquire()
        try:
            anagrams = list()
            for w in [words for words in self.words if len(words) == len(word)]:
                if sorted(w) == sorted(word):
                    anagrams.append(w)
        finally:
            self.lock.release()
        return anagrams


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEquals(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])
        self.assertEquals(anagrams.get_anagrams('nameless'), ['lameness', 'maleness', 'nameless', 'salesmen'])
        self.assertEquals(anagrams.get_anagrams('trainers'), ['restrain', 'retrains', 'strainer', 'terrains', 'trainers'])
        self.assertEquals(anagrams.get_anagrams('caters'), ['caster', 'caters', 'crates', 'reacts', 'recast', 'traces'])
        self.assertEquals(anagrams.get_anagrams('pears'), ['pares', 'parse', 'pears', 'rapes', 'reaps', 'spare', 'spear'])


if __name__ == '__main__':
    unittest.main()
