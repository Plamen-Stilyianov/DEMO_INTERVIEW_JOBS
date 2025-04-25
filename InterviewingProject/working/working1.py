import pytest


def get_data():
    lines = []
    with open(file='demo.txt', mode='r') as fl:
        for line in fl:
            lines.append(line)

    text = "".join(lines)
    return clean_lines(text)


def clean_lines(line):
    new_line = line.lower().replace('.', ' ').replace('"', ' ').replace(';', ' ').replace('  ', ' ')
    text = " ".join([str.lstrip(word).rstrip() for word in new_line.split(' ') if
                     word not in ['after', 'out', 'on', 'as', 'he', 'gb', 'and', 'to', 'him', 'a', 'the']])
    return text


def test_get_data():
    assert isinstance(get_data(), str)


if __name__ == '__main__':
    pytest.main([__file__])
