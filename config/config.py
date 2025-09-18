'''记录全部的接口地址，模块间直接调用'''
import os
from dotenv import load_dotenv

load_dotenv()

# 设置当前默认环境地址，APP_ENV为系统环境，pord为默认值
ENV = os.getenv("APP_ENV", "dev").lower()  # 不区分大小写

# 默认接收的UID,"wzptestuser30@fotor.com"
target_account ={
    # 测试环境默认接收的UID,"wzptestuser30@fotor.com"
    "test":"6dd0933c2a774c52a435eabdb53966bd",
    # 测试环境默认接收的UID,"wzpproduser30@fotor.com"
    "prod":"c5a6ec07f4154b6e85720dde1ea3d147"
}

# 设置测试和正式环境地址
API_ENDPOINTS = {
    "dev": {
        # 运营后台
        "base_url": "https://test-admin-fomsv2.everimaging.com/",
        # 登录
        "login": "https://test-admin-fomsv2.everimaging.com/api/admin/login",
        # 通过邮箱查询UID
        "user_info": "https://test-admin-fomsv2.everimaging.com/api/user_info",
        # 转移订阅
        "transfer_subscribe": "https://test-admin-fomsv2.everimaging.com/api/userInfo/transReading",
        # 会员查询
        "isvip": "https://test-www.fotor.com/pay/service/en/payment/check/isvip",
        # 账号订阅查询
        "user_payment": "https://test-admin-fomsv2.everimaging.com/api/userInfoForPayment",
        # 转移积分
        "transfer_credits": "https://test-admin-fomsv2.everimaging.com/api/userInfo/transferCredit",
        # 积分查询（路径参数）
        "get_score": "https://test-www.fotor.com/api/create/test/score/fotor",
        # 新增兑换码
        "add_coupon_code":"https://test-admin-fomsv2.everimaging.com/api/activity/addCouponCodeTime",
        # 查询兑换码个数
        "get_code_use_info":'https://test-admin-fomsv2.everimaging.com/api/activity/getCodeUseInfo',
        # 获取兑换码列表（查询参数）
        "get_activity_code_use_list":"https://test-admin-fomsv2.everimaging.com/api/activity/getActivityCodeUseList",
        # 给对应账号发送积分
        "send_credits" :"https://test-admin-fomsv2.everimaging.com/api/userInfo/sendCredit"
    },
    "prod": {
        "base_url": "https://admin-fomsv2.everimaging.com/",
        # 登录
        "login": "https://admin-fomsv2.everimaging.com/api/admin/login",
        # 通过邮箱查询UID
        "user_info": "https://admin-fomsv2.everimaging.com/api/user_info",
        # 转移订阅
        "transfer_subscribe": "https://admin-fomsv2.everimaging.com/api/userInfo/transReading",
        # 会员查询
        "isvip": "https://www.fotor.com/pay/service/en/payment/check/isvip",
        # 账号订阅查询
        "user_payment": "https://admin-fomsv2.everimaging.com/api/userInfoForPayment",
        # 转移积分
        "transfer_credits": "https://admin-fomsv2.everimaging.com/api/userInfo/transferCredit",
        # 积分查询（路径参数）
        "get_score": "https://www.fotor.com/api/create/test/score/fotor",
        # 新增兑换码
        "add_coupon_code":"https://admin-fomsv2.everimaging.com/api/activity/addCouponCodeTime",
        # 查询兑换码个数
        "get_code_use_info":'https://admin-fomsv2.everimaging.com/api/activity/getCodeUseInfo',
        # 获取兑换码列表（查询参数）
        "get_activity_code_use_list":"https://admin-fomsv2.everimaging.com/api/activity/getActivityCodeUseList",
        # 给对应账号发送积分
        "send_credits" :"https://admin-fomsv2.everimaging.com/api/userInfo/sendCredit"
    }
}


# 获取URL，使用时先传url名，再传哪个环境
def get_api(*apis: str, env: str = None):  # 必选项写在前面，可选项写在后面，且支持一次传入多个参数
    env = (env or ENV).lower()  # 不传参则使用默认值ENV=dev
    if env not in API_ENDPOINTS:
        raise ValueError(f"无效的环境参数:{env}")

    # 只传一个参数，直接返回字符串
    if len(apis) == 1:
        api = apis[0]
        if api not in API_ENDPOINTS[env]:
            raise ValueError(f"接口:{api} 不存在于 {env} 环境")
        return API_ENDPOINTS[env][api]

    # 传多个参数，返回 dict
    urls = {}
    for api in apis:
        if api not in API_ENDPOINTS[env]:
            raise ValueError(f"接口:{api} 不存在于 {env} 环境")
        urls[api] = API_ENDPOINTS[env][api]
    return urls

def get_account(env: str = None) -> str:
    env = (env or ENV).lower()
    if env not in target_account:
        raise ValueError(f"无效的环境参数: {env}")
    return target_account[env]