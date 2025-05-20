import pytest
import pandas as pd
from typing import List, Union, SupportsFloat, SupportsInt, Any


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


def extract_prices(data: Union[List, SupportsFloat, SupportsInt]) -> List[Any]:
    prices = []
    if isinstance(data, (SupportsInt, SupportsFloat)):
        prices.append(data)


    if isinstance(data, List):
        for item in data:
            prices.extend(extract_prices(item))

    return prices

@pytest.mark.parametrize("symbol, expected",[('APPL',9),
                                             ('MS', 7),
                                             ('JPM', 8),
                                             ('DUMMY', 0),])
def test_extract_prices(symbol, expected, stock_data):
    prices = []
    for stock in stock_data[symbol].values.tolist():
        if not isinstance(stock, List):
            continue
        else:
            prices.extend(extract_prices(stock))
    prices  = set(prices)
    sorted_prices = sorted(prices)
    assert len(sorted_prices) == expected