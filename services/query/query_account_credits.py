'''直接通过接口查询目标账号积分'''
from config.config import get_api
from network.vpn_connection import api_request
from services.query import query_account_uid
from utils.validate_user_input import validate_input

def query_account_credits(uid_or_email:str, cookies=None):
    #先对输入账号进行合法判断，邮箱则返回uid
    uid = validate_input(uid_or_email, cookies=cookies)

    if uid == "invalid":
        return f"❌ 查询失败，该邮箱：{uid_or_email}无效或错误"

    get_score_api = get_api('get_score',env='dev')
    full_api = f'{get_score_api}/{uid}'
    print(full_api)
    results = api_request(full_api,cookies=cookies).json()

    return f'当前账号积分为：{results["data"]["subScore"]}'


# print(query_account_credits("525960dca5b1448d880c347080030f99"))