import pytest
import pandas as pd
from typing import List, Union, SupportsFloat, SupportsInt


def extract_share_prices(data: Union[List, SupportsFloat, SupportsInt]) -> List:
    prices = []
    if isinstance(data, (SupportsInt, SupportsFloat)):
        prices.append(data)
    elif isinstance(data, List):
        for item in data:
            prices.extend(extract_share_prices(item))

    return prices

def get_prices(stock_data) -> List:
        prices = extract_share_prices(stock_data)
        prices = set(prices)
        sorted_prices = sorted(prices)
        return sorted_prices


@pytest.fixture(scope='module')
def stock_data():
        return pd.DataFrame.from_dict({'APPL':{'17-5-2025': [211.26],               # len = 9(9)
                                               '18-5-2025': [[207.56, 210]],
                                               '19-5-2025': [[[232.18, 229.05, 231, 228.08, 230, 232.30]]]
                                               },
                                       'MS': {'17-5-2025': [[132.18]],              # len = 7(9)
                                                '18-5-2025': [[128.23, 129.05]],
                                                '19-5-2025': [[[132.18, 129.05, 131, 128.08, 130, 132.30]]]
                                                },
                                       'JPM': {'17-5-2025': [[261.26, 259.05, ' ', None]],     # len 8(10)
                                                '18-5-2025': [[[[267.56, 259.05]]]],
                                                '19-5-2025': [[[262.18, 259.05, 261, 258.08, 250, 252.30]]]
                                                },
                                       'DUMMY': {'17-5-2025': [[]]}

                                   })

@pytest.fixture(scope='module')
def stock_tree_data():
        return pd.DataFrame.from_dict({'APPL':{'17-5-2025': [211.26],               # len = 9(9)
                                               '18-5-2025': [[207.56, 210], [207.56, 210, 209.98]],
                                               '19-5-2025': [[[232.18, 229.05, 231, 228.08, 230, 232.30, None], [229.05, 231, 228.08, 230], []]],
                                               '20-5-2025': [[[[232.18, 229.05, 231, 228.08, 230, 232.30], [229.05, 231, 228.08, 230], [207.56, 210, 209.98], [217.56, 220, 219.98]]]],
                                               }})


@pytest.mark.parametrize("symbol, expected", [('APPL',9),
                                             ('MS', 7),
                                             ('JPM', 8),
                                             ('DUMMY', 0),])
def test_extract_share_prices(symbol, expected, stock_data):
    prices = []
    for stock in stock_data[symbol].values.tolist():
        if not isinstance(stock, List):
            continue
        else:
            prices.extend(extract_share_prices(stock))
    prices = set(prices)
    assert len(prices) == expected

@pytest.mark.parametrize("symbol, expected", [('APPL',[207.56, 210, 211.26, 228.08, 229.05, 230, 231, 232.18, 232.3]),
                                             ('MS', [128.08, 128.23, 129.05, 130, 131, 132.18, 132.3]),
                                             ('JPM',[250, 252.3, 258.08, 259.05, 261, 261.26, 262.18, 267.56]),
                                             ('DUMMY', []),])
def test_get_prices(symbol, expected, stock_data):
    prices = []
    for stock in stock_data[symbol].values.tolist():
        if not isinstance(stock, List):
            continue
        else:
            prices.extend(extract_share_prices(stock))

    assert get_prices(prices) == expected


@pytest.mark.parametrize("symbol, expected", [('APPL',[207.56, 209.98, 210, 211.26, 217.56, 219.98, 220, 228.08, 229.05, 230, 231, 232.18, 232.3] ),])
def test_get_prices_tree(symbol, expected, stock_tree_data):
    prices = []
    for stock in stock_tree_data[symbol].values.tolist():
        if not isinstance(stock, List):
            continue
        else:
            prices.extend(extract_share_prices(stock))

    assert get_prices(prices) == expected