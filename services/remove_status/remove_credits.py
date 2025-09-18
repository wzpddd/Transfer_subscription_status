from config.config import get_api,get_account
from network.vpn_connection import api_request
from utils.validate_user_input import validate_input
import logging

logging.basicConfig(level=logging.DEBUG)
def remove_account_credits(uid_or_email: str, cookies: None):
    # 先对输入账号进行合法判断，邮箱则返回uid
    uid = validate_input(uid_or_email, cookies=cookies)

    if uid == "invalid":
        return f"❌ 查询失败，该邮箱：{uid_or_email}无效或错误"

    #先进行积分判断，没有积分的不执行下一步
    get_credits_details_api = get_api("user_payment",env='dev')
    params = {
        "key": "creditPoints",
        "value":uid,
        "status":"",
        "pageNo" :"1",
        "pageSize":"10",
        'payState':""
    }
    result = api_request(get_credits_details_api,'get',cookies=cookies,params=params).json()
    if not result.get("data", {}).get("list"):
        return "❌ 当前账号无积分可转移"

    #转移积分
    get_remove_credits_api = get_api('transfer_credits', env='dev')
    params = {
        "fromUid":uid,
        "toUid":get_account("test")
    }
    results = api_request(get_remove_credits_api,"post", json=params,cookies=cookies).json()

    if results["code"] == "000":

        return "✅ 积分转移成功"



