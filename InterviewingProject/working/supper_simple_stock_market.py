import numpy as np
from datetime import datetime, timedelta


class Stock():
    """ Stock class used for calculating dividend yield and P/E ratio"""

    def __init__(self, symbol, par_value, type, last_dividend, fixed_dividend=None):
        self.symbol = symbol
        self.par_value = par_value
        self.type = type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend

    def get_dividend_yield(self, price):
        """ Calculate the dividend yield, given any price as input. """
        if price is None or price < 1:
            raise ValueError("Price must be greater than 0")
        if self.fixed_dividend is None or self.fixed_dividend <= 0:
            return 0
        dividend_yield = (self.fixed_dividend * self.par_value) / price \
            if self.type == 'Preferred' else self.last_dividend / price
        return dividend_yield

    def get_pe_ratio(self, price):
        """ Calculate the P/E Ratio, given any price as input. """

        if price is None or price < 1:
            raise ValueError("Price must be greater than 0")
        pe_ratio = price / self.fixed_dividend
        return pe_ratio


class Trade:
    """ Trade class used to store trade records """
    def __init__(self, symbol, timestamp, quantity, buy_or_sell, price):
        self.symbol = symbol
        self.timestamp = timestamp
        self.quantity = quantity
        self.buy_or_sell = buy_or_sell
        self.price = price


class StockMarket:
    """ StockMarket class used to book trades and calculate Volume Weighted Stock Price """
    __trades = []

    def __init__(self):
        self._trades = StockMarket.__trades

    @staticmethod
    def book_trade(symbol, quantity, buy_or_sell, price):
        """ Record a trade, with timestamp, quantity, buy or sell indicator and price. """

        if quantity < 1 or price < 1:
            raise ValueError("Price and Quantity must be greater than 0")

        timestamp = datetime.now()
        trade = Trade(symbol, timestamp, quantity, buy_or_sell, price)
        record = (trade.timestamp, trade)
        StockMarket.__trades.append(record)

    @staticmethod
    def calculate_VWSP(symbol, minutes=5):
        """ Calculate Volume Weighted Stock Price based on trades in past 5 minutes. """

        if len(StockMarket.__trades) == 0:
            raise ValueError("No trades booked for this market")

        if minutes > 0:
            timestamp = datetime.now() - timedelta(minutes=minutes)
            trades = [trade[1] for trade in reversed(StockMarket.__trades) if
                      trade[0] >= timestamp and trade[1].symbol == symbol]
        else:
            trades = [trade[1] for trade in StockMarket.__trades if trade[1].symbol == symbol]

        price_qty = sum([trade.price * trade.quantity for trade in trades])
        sum_qty = sum([trade.quantity for trade in trades])
        return price_qty / sum_qty


class GlobalBeverageCorporationExchange(StockMarket):
    """ The Global Beverage Corporation Exchange is a new stock market trading in drinks companies """

    def __init__(self):
        super().__init__()

    def all_stock_index(self):
        """ All Share Index using the geometric mean of the Volume Weighted Stock Price for all stocks """
        
        prices = [self.calculate_VWSP(trade.symbol, 0) for trade in self._trades]
        prod = np.prod(np.array(prices), axis=0)
        return prod**(1 / len(prices))