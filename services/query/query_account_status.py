from services.query.query_account_uid import query_account_uid
from network.vpn_connection import *
from config.config import get_api
from utils import get_nested
from utils import format_timestamp_ms



def isvip(uid_or_email: str,cookies = None):

    if "@" in uid_or_email:
        uid_or_email= query_account_uid(uid_or_email,cookies)
    # 获取查询用户的url
    base_url = get_api("isvip", "dev")
    # 拼接参数带入url
    full_url = f"{base_url}/{uid_or_email}"
    response = api_request(full_url, "get").json()

    # 返回展示的内容
    result_list = []
    if get_nested(response, "data", "amount") is not None:
        # 转换时间戳
        startDateMs = format_timestamp_ms(response["data"]["startDateMs"])
        expiresDateMs = format_timestamp_ms(response["data"]["expiresDateMs"])
        # 要展示的内容
        result_list.append(f"会员状态：{response['data']['vipStatus']}")
        result_list.append(f"订阅类型：{response['data']['planInterval']}")
        result_list.append(f"开始时间：{startDateMs}")
        result_list.append(f"结束时间：{expiresDateMs}")
        result_list.append(f"实际支付：{response['data']['amount']}{response['data']['currency']}")
        # print(result_list)

    return result_list



