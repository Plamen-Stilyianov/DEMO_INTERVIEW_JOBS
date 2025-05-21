import pytest


def reversed_string(s: str) -> str:
    if "." in s:
        l_words = []
        words = s.split('. ')
        for word in list(reversed(words)):
            rev_word = str(word).split(' ')[::-1]
            l_words.extend(rev_word)
        return ' '.join(l_words)
    else:
        words = s.split(' ')
        rev_words = list(reversed(words))
        return ' '.join(rev_words)


@pytest.mark.parametrize("s, expected",
                         [("Hello Python. Hello Java", "Java Hello Python Hello"), ("Hello World", "World Hello"), ])
def test_reversed_string(s: str, expected: str) -> None:
    assert reversed_string(s) == expected


if __name__ == '__main__':
    pytest.main([__file__])
