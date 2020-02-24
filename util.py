import datetime
import hashlib
import hmac
import json
import urllib
import requests

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)



def request_nosign_get(url, dic):
    header_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko", \
                   "Content-Type": "application/json;charset=utf-8", "Connection": "keep-alive", \
                   "Cookie": "locale=zh_CN"}
    return http_request(url, data=dic, header_dict=header_dict, reqtype='GET')


def request_sign_get(url, dic):
    header_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko", \
                   "Content-Type": "application/json;charset=utf-8", "Connection": "keep-alive", \
                   "Cookie": "locale=zh_CN"}
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    header_dict['ACCESS-KEY'] = dic['apiid']
    header_dict['ACCESS-TIMESTAMP'] = timestamp
    requestURI = dic['requestURI']
    secret = dic['secret']
    del dic['requestURI']
    del dic['secret']
    del dic['apiid']
    method = 'GET'
    data = ""
    if len(dic) > 0:
        data = "?" + urllib.parse.urlencode(dic)
    message = timestamp + method + requestURI + data
    mysign = sign(message=message, secret=secret)
    header_dict['ACCESS-SIGN'] = mysign

    url = url + data
    return http_request(url, data=None, header_dict=header_dict, reqtype='GET')


def request_sign_post(url, dic):
    header_dict = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko", \
                   "Content-Type": "application/json;charset=utf-8", "Connection": "keep-alive", \
                   "Cookie": "locale=zh_CN"}
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    header_dict['ACCESS-KEY'] = dic['apiid']
    header_dict['ACCESS-TIMESTAMP'] = timestamp
    requestURI = dic['requestURI']
    secret = dic['secret']
    del dic['requestURI']
    del dic['secret']
    del dic['apiid']
    method = 'POST'
    data = json.dumps(dic)
    message = timestamp + method + requestURI + data
    mysign = sign(message=message, secret=secret)
    header_dict['ACCESS-SIGN'] = mysign
    return http_request(url, data=dic, header_dict=header_dict)


def http_request(url, data, header_dict, reqtype='POST'):
    if reqtype == 'GET':
        reponse = requests.get(url, params=data, headers=header_dict)
    else:
        reponse = requests.post(url, data=json.dumps(data), headers=header_dict)
    try:
        if reponse.status_code == 200:
            return json.loads(reponse.text)
        else:
            return None
    except Exception as e:
        print('http failed : %s' % e)
        return None


def sign(message, secret):
    """
    这里进行签名
    :param message: message wait sign
    :param secret:  secret key
    :return:
    """
    secret = secret.encode('utf-8')
    message = message.encode('utf-8')
    sign = hmac.new(secret, message, digestmod=hashlib.sha256).hexdigest()
    return sign



