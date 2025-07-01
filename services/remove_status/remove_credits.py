from config import get_api,target_account
from network.vpn_connection import api_request
from services.query import query_account_uid
from utils import validate_input
import logging

logging.basicConfig(level=logging.DEBUG)
def remove_account_credits(uid_or_email: str, cookies: None):
    # 先对输入账号进行合法判断，邮箱则返回uid
    uid = validate_input(uid_or_email, cookies=cookies)
    if "@" in uid_or_email:
        uid = query_account_uid(uid_or_email, cookies)
        # print(uid)
        if not uid:
            return f"❌ 查询失败，该邮箱：{uid_or_email}无效或不存在"
    else:
        uid = uid_or_email
    # 判断UID位数
    if len(uid) not in (32, 33):
        return f"❌ 查询失败，UID: {uid}无效"

    #先进行积分判断，没有积分的不执行下一步
    get_credits_details_api = get_api("user_payment",'dev')
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
    get_remove_credits_api = get_api('transfer_credits', 'dev')
    print(get_remove_credits_api)
    params = {
        "fromUid":uid,
        "toUid":target_account
    }
    print(uid,target_account)
    results = api_request(get_remove_credits_api,"post", json=params,cookies=cookies).json()

    if results["code"] == "000":

        return "积分转移成功"



