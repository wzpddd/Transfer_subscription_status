from http.client import responses

from config.config import get_api
import requests
from network import login
from network.vpn_connection import api_request
# url = "https://test-admin-fomsv2.everimaging.com/api/userInfoForPayment"
# params = {
#     "key":"subscription",
#     "pageNo": 1,
#     "pageSize": 10,
#     "type": "uid",
#     "value": "447fbc23af2a49c19ff470934815fe35",
#     "status": 1
# }
# headers = {
#     "Cookie": "fotorAdmin.sid=s%3Ae0lcUheZy886X9-U25-H-4tBZuS47HMi.zh1B7qLD7U8%2FV%2FbmBoQtAQWiS4Hi9s3%2FksJRLNvhuu0"
# }
# proxies = {
#     "http": "http://192.168.1.101:7890",
#     "https": "http://192.168.1.101:7890"
# }
#
# cookie = {'fotorAdmin.sid': 's%3Av4zRulG8PaIqsBdp4RWojPipEinHwRKT.R1a9LKjFRIpXcBjkMZnc1LETzMJEMAEfcvFmvlO4erc'}
# respons = requests.get(url,params=params,cookies=cookie)
# print(respons.json())

# cookie = login.login_session()
# print(cookie)
# responses = api_request(url,"get",params=params,cookies=cookie)
# print(responses.json())
