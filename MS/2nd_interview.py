import pytest
from typing import Dict, Union, Tuple

@pytest.fixture(scope='module')
def portfolios() -> Dict[str, Union[int | float]]:
    port_data = {'APPL':20,
                 'GOOG':-2,
                 'subporfolio':{'GOOG':10,
                                'JPM': -8},
                 'subportfolio1':{'MSFT':10},
                 'MSFT':8}
    return port_data


def get_positions(portfolios: Dict[str, Union[int | float]]) -> Dict[str, Union[int | float]]:
    positions = {}

    for symbol, portfolio in portfolios.items():
        if not isinstance(portfolio, Dict):
            if symbol not in positions:
                positions[symbol] = portfolio
            else:
                positions[symbol] += portfolio
        elif isinstance(portfolio, Dict):
            innerportfolio = get_positions(portfolio)
            for sym_inner, pos_inner in innerportfolio.items():
                if sym_inner not in positions:
                    positions[sym_inner] = pos_inner
                elif sym_inner in positions:
                    positions[sym_inner] += pos_inner

    return positions

def get_second_position(portfolios: Dict[str, Union[int | float]]) -> Tuple[str, Union[int | float]]:
    positions = get_positions(portfolios)
    sorted_positions = sorted(positions.items(), key=lambda x: abs(x[1]))
    second_position = sorted_positions[1]
    return second_position


def test_get_positions(portfolios: Dict[str, Union[int | float]]) -> None:
    expected ={'APPL': 20, 'GOOG': 8, 'JPM': -8, 'MSFT': 18}
    positions = get_positions(portfolios)
    assert positions == expected

def test_get_second_position(portfolios: Dict[str, Union[int | float]]) -> None:
    second_position = get_second_position(portfolios)
    expected = ('JPM', -8)
    assert second_position == expected

if __name__ == "__main__":
    pytest.main([__file__])