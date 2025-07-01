from services.query.query_account_uid import query_account_uid
from network.vpn_connection import *
from config.config import get_api
from utils import get_nested
from utils import format_timestamp_ms

'''直接通过isvip接口查询账号状态'''


def isvip(uid_or_email: str, cookies=None):
    # 先判断是否为邮箱，是邮箱就先获取UID
    if "@" in uid_or_email:
        uid = query_account_uid(uid_or_email, cookies=cookies)
        if not uid:
            return f"❌ 查询失败，该邮箱：{uid_or_email}无效或不存在"
    else:
        uid = uid_or_email
    # 判断UID位数
    if len(uid) not in (32, 33):
        return f"❌ 查询失败，UID: {uid}无效"

    # 通过isvip获取账号订阅状态
    base_url = get_api("isvip", "dev")
    # 拼接参数带入url
    full_api = f"{base_url}/{uid}"

    # 查询报错时的异常处理
    try:
        response = api_request(full_api, "get", cookies=cookies).json()
    except Exception:
        return f"❌ 查询失败，UID: {uid}无效或不存在"

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
    else:
        return ("❌ 未查询到当前账号订阅信息")
