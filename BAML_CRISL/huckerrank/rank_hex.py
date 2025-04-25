def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def validate_format(w):
    ends = [';', ')', '}', ']', ',', ':', '.', '?']
    if w[-1] in ends:
        w = w[:-1]
        cr = hex_to_rgb(w)
        if list(filter(lambda x: True if 0 < x <= 255 else False, cr)):
            print(w)
    else:
        pass



def run(text):
    for line in text:
        if '#' in line:
            for _ in range(line.count('#')):
                idx = line.index('#')
                word = line[idx:idx + 7]
                line = line[idx + 7:]
                validate_format(word)
        else:
            continue


if __name__ == "__main__":
    N = input()
    lines = []
    for _ in range(int(N)):
        line = input()
        lines.append(line)

    run(lines)

data = """11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}"""
