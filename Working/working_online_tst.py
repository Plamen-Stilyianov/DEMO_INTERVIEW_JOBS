import pandas as pd


def pull_link(url):
    table = pd.read_html(url, header=0, flavor='bs4')
    rows = table[0].sort_values(['y-coordinate', 'x-coordinate'], ascending=[False, True])
    nl = ""  # newline when x returns to 0
    for i, row in rows.iterrows():
        if row['x-coordinate'] == 0:
            print(end=nl)
            nl = '\n'
        print(row['Character'], end="")
    print()


print(pull_link(
    'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'))
