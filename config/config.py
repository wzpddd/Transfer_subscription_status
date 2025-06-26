'''记录全部的接口地址，模块间直接调用'''

import os
from dotenv import load_dotenv

load_dotenv()

# 设置当前默认环境地址，APP_ENV为系统环境，pord为默认值
ENV = os.getenv("APP_ENV", "dev").lower()  # 不区分大小写

# 设置测试和正式环境地址
API_ENDPOINTS = {
    "dev": {
        "base_url": "https://test-admin-fomsv2.everimaging.com/",
        "login": "https://test-admin-fomsv2.everimaging.com/api/admin/login",
        "user_info": "https://test-admin-fomsv2.everimaging.com/api/userInfoForPayment",
        "transfer": "https://test-admin-fomsv2.everimaging.com/api/userInfo/transReading",
        "isvip":"https://test-www.fotor.com/pay/service/en/payment/check/isvip"
    },
    "prod": {
        "base_url": "https://admin-fomsv2.everimaging.com/",
        "login": "https://admin-fomsv2.everimaging.com/api/admin/login",
        "user_info": "https://admin-fomsv2.everimaging.com/api/userInfoForPayment",
        "transfer": "https://admin-fomsv2.everimaging.com/api/userInfo/transReading",
        "isvip":"https://www.fotor.com/pay/service/en/payment/check/isvip"
    }
}


# 获取URL，使用时先传url名，再传哪个环境
def get_api(api: str, env: str = None):  # 必选项写在前面，可选项写在后面
    env = (env or ENV).lower()  # 不传参则使用默认值ENV=dev
    if env not in API_ENDPOINTS:
        raise ValueError(f"无效的环境参数:{env}")
    if api not in API_ENDPOINTS[env]:
        raise ValueError(f"接口:{env}不存在于{env}环境")
    return API_ENDPOINTS[env][api]
