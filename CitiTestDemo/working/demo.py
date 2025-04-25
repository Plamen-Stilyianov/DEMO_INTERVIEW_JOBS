from itertools import chain


def multi_string(s):
    #word = [[s[kv]] * int(s[kv + 1]) for kv in range(0, len(s), 2)]
    #new_word = chain(*word)
    new_word = [s[kv] * int(s[kv + 1]) for kv in range(0, len(s), 2)]
    # new_word = chain(*word)
    return ''.join(list(new_word))


def test_multi_string():
    expected_string = 'zzztxxxxx'
    temp_s = 'z3t1x5'
    assert multi_string(temp_s) == expected_string


if __name__ == '__main__':
    test_multi_string()
