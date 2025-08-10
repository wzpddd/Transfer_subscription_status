from config.config import get_api
from network.vpn_connection import api_request
from utils.dict_tools import get_nested
from utils.validate_user_input import validate_input

cookies = {'fotorAdmin.sid': 's%3ASAtFnGUyJ2RJTwXkDSYPIi94PKvis8hH.Z4hyBDrVHReJMsgEvGRtfG0nFcxtqZLrv2SnIiz4QEA'}
def recharge_account_credits(uid_or_email ,credits_num , cookies=None):
    # 先对输入账号进行合法判断，邮箱则返回uid
    uid = validate_input(uid_or_email, cookies=cookies)

    if uid == "invalid":
        return f"❌ 查询失败，该邮箱：{uid_or_email}无效或错误"

    #将参数传递给接口
    send_credits_api  = get_api("send_credits", env="dev")
    params = {
        "uid" : uid ,
        "credits" : {
            "num" : credits_num,
            "duration": 1,
            "cycle" : "month",
            "type":"activity",
            "reason":"快速充值"
        }
    }
    result = api_request(send_credits_api, "post",json=params, cookies=cookies).json()
    print(result)
    if get_nested(result,"msg") == "success":
        return  f"✅ {uid_or_email}已充值{credits_num}credits"
    return "❌ 充值失败"

recharge_account_credits("b71a145478b642f38265041357bb73aa",2,cookies)

import json



# debug_print("cookies", cookies)
# debug_print("uid", uid)
# debug_print("credits_num", credits_num)