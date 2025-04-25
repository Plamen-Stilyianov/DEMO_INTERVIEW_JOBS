def anagram_distance_arr(a, b):
    return [anagram_distance_between(tpl[0], tpl[1]) for tpl in zip(a, b)]


def anagram_distance_between(str1, str2):
    if len(str1) != len(str2):
        return -1
    distance = 0
    for letter in str1:
        if letter in str2:
            str2 = str2.replace(letter, '', 1)
        else:
            distance += 1
    return distance


# tests
import unittest


class AnagramDistanceTestCase(unittest.TestCase):
    def test_distance(self):
        test_suite = (
            (
                ['aad', 'cat', 'kf', 'qwer'],
                ['aaa', 'dog', 'fk', 'qwe'],
                [1, 3, 0, -1]
            ),
            (
                ['aaa', 'cat', 'aaaa'],
                ['aab', 'dag', 'aazz'],
                [1, 2, 2]
            ),
            (
                ['aadd', 'bbb', 'kfkl', 'qwer'],
                ['aaaa', 'cdc', 'fklk', 'qwesadf'],
                [2, 3, 0, -1]
            ),
        )
        for suite in test_suite:
            self.assertEqual(anagram_distance_arr(suite[0], suite[1]), suite[2])


if __name__ == '__main__':
    unittest.main()
