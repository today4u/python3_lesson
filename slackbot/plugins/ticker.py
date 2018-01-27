from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import requests
import json

BF_api_url = 'https://api.bitflyer.jp/v1'
CC_api_url = 'https://coincheck.com/api'
ZF_api_url = 'https://api.zaif.jp/api/1'

def BF_get_api_call(path):
    method = 'GET'
    request_data = requests.get(
        BF_api_url + path,
        headers = {}
    )
    return request_data

def CC_get_api_call(path):
    method = 'GET'
    request_data = requests.get(
        CC_api_url + path,
        headers = {}
    )
    return request_data

def ZF_get_api_call(path):
    method = 'GET'
    request_data = requests.get(
        ZF_api_url + path,
        headers = {}
    )
    return request_data




@respond_to('bitflyer', re.IGNORECASE)
def mention_func(message):
    message.reply('現在のbitflyerのticker')
    data = BF_get_api_call('/getticker').json()
    message.reply('最終取引価格:' + str(data['ltp']) + ' 最高値:' + str(data['best_bid']) + ' 最低値:' + str(data['best_ask']))


@respond_to('coincheck', re.IGNORECASE)
def mention_func(message):
    message.reply('現在のcoincheckのticker')
    data = CC_get_api_call('/ticker').json()
    message.reply('最終取引価格:' + str(data['last']) + ' 最高値:' + str(data['bid']) + ' 最低値:' + str(data['ask']))

@respond_to('zaif', re.IGNORECASE)
def mention_func(message):
    message.reply('現在のZAIFのticker')
    data = ZF_get_api_call('/ticker/btc_jpy').json()
    message.reply('最終取引価格:' + str(data['last']) + ' 最高値:' + str(data['bid']) + ' 最低値:' + str(data['ask']))






