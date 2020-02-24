from exchange.util import *

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class ExchangeClient:
    """
        client for CoinBene exchange ,include functions of  account ,market ,trade operations
        """

    def __init__(self, apiid, secret):
        self.apiid = apiid
        self.secret = secret
        self.base_url = 'http://openapi-exchange.coinbene.com'

    def _gen_parameter(self):
        """
        gen common info for sign
        :return:
        """
        dic = {'apiid': self.apiid, 'secret': self.secret}
        return dic

    def trade_pair_list(self):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/market/tradePair/list"
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_nosign_get(url, dic)

    def trade_pair_one(self, symbol):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/market/tradePair/one"
        dic['requestURI'] = requrl
        dic['symbol'] = symbol
        url = self.base_url + requrl
        return request_nosign_get(url, dic)

    def order_book(self, symbol, depth):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/market/orderBook"
        dic['requestURI'] = requrl
        dic['symbol'] = symbol
        dic['depth'] = depth
        url = self.base_url + requrl
        return request_nosign_get(url, dic)

    def ticker_one(self, symbol):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/market/ticker/one"
        dic['requestURI'] = requrl
        dic['symbol'] = symbol
        url = self.base_url + requrl
        return request_nosign_get(url, dic)

    def market_trades(self, symbol):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/market/trades"
        dic['requestURI'] = requrl
        dic['symbol'] = symbol
        url = self.base_url + requrl
        return request_nosign_get(url, dic)

    def account_list(self):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/account/list"
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def account_one(self, asset):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/account/one"
        dic['requestURI'] = requrl
        dic['asset'] = asset
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def order_place(self, symbol, direction, price, quantity, orderType, notional, clientId):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/order/place"
        dic['requestURI'] = requrl
        dic['symbol'] = symbol
        dic['direction'] = direction
        if price is not None:
            dic['price'] = price
        if quantity is not None:
            dic['quantity'] = quantity
        dic['orderType'] = orderType
        if notional is not None:
            dic['notional'] = notional
        if clientId is not None:
            dic['clientId'] = clientId
        url = self.base_url + requrl
        return request_sign_post(url, dic)

    def open_orders(self, symbol, latestOrderId):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/order/openOrders"
        dic['requestURI'] = requrl
        if symbol is not None:
            dic['symbol'] = symbol
        if latestOrderId is not None:
            dic['latestOrderId'] = latestOrderId;
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def close_orders(self, symbol, latestOrderId):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/order/closedOrders"
        dic['requestURI'] = requrl
        if symbol is not None:
            dic['symbol'] = symbol
        if latestOrderId is not None:
            dic['latestOrderId'] = latestOrderId;
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def order_info(self, orderId):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/order/info"
        dic['requestURI'] = requrl
        dic['orderId'] = orderId
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def trade_fills(self, orderId):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/order/trade/fills"
        dic['requestURI'] = requrl
        dic['orderId'] = orderId
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def order_cancel(self, orderId):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/order/cancel"
        dic['requestURI'] = requrl
        dic['orderId'] = orderId
        url = self.base_url + requrl
        return request_sign_post(url, dic)

    def batch_cancel(self, orderIds):
        dic = self._gen_parameter()
        requrl = "/api/exchange/v2/order/batchCancel"
        dic['requestURI'] = requrl
        dic['orderIds'] = orderIds
        url = self.base_url + requrl
        return request_sign_post(url, dic)
