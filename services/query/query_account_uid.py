'''查询邮箱的UID'''
import requests
from config.config import get_api
from network.vpn_connection import api_request
from utils import get_nested


def query_account_uid(account_uid: str, cookies = None):
    url = get_api("user_info", "dev")
    params = {
        "appleName=":"",
        "pageNo=1":'1',
        "pageSize=":"10",
        "type": "email",
        "value": account_uid
    }
    response = api_request(url, params=params,cookies=cookies,timeout=10).json()
    print(response)
    return get_nested(response, "data", "uid")
