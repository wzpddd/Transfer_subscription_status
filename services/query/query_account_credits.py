'''直接通过接口查询目标账号积分'''
from config import get_api
from network.vpn_connection import api_request
from utils import validate_input

def query_account_credits(uid:str, cookies=None):
    uid = validate_input(uid)
    get_score_api = get_api('get_score','prod')
    full_api = f'{get_score_api}/{uid}'
    results = api_request(full_api,cookies=cookies).json()

    return f'当前账号积分为：{results["data"]["subScore"]}'


print(query_account_credits("525960dca5b1448d880c347080030f99"))