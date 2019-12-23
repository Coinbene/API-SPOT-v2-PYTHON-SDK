import unittest

from exchange.ExchangeClient import ExchangeClient


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        apiid = 'XXX'
        secret = 'XXX'
        self.client = ExchangeClient(apiid, secret)

    def test_trade_pair_list(self):
        res = self.client.trade_pair_list()
        print(res)

    def test_trade_pair_one(self):
        res = self.client.trade_pair_one("BTC/USDT")
        print(res)

    def test_order_book(self):
        res = self.client.order_book("BTC/USDT", 10)
        print(res)

    def test_ticker_one(self):
        res = self.client.ticker_one("BTC/USDT")
        print(res)

    def test_market(self):
        res = self.client.ticker_one("BTC/USDT")
        print(res)

    def test_account_list(self):
        res = self.client.account_list()
        print(res)

    def test_account_one(self):
        res = self.client.account_one("USDT")
        print(res)

    def test_order_place(self):
        res = self.client.order_place("CONI/USDT", 1, 0, 0, 2, 0.2, "test")
        print(res)

    def test_order_cancel(self):
        res = self.client.order_cancel("1981349103082577920")
        print(res)

    def test_batch_cancel(self):
        res = self.client.batch_cancel(["1981349103082577920"])
        print(res)

    def test_open_orders(self):
        res = self.client.open_orders(None, None)
        print(res)

    def test_close_orders(self):
        res = self.client.close_orders(None, "1981349103082577920")
        print(res)
