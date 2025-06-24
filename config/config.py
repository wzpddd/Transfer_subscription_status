import os
from dotenv import load_dotenv

load_dotenv()

# 设置当前默认环境地址，APP_ENV为系统环境，pord为默认值
ENV = os.getenv("APP_ENV", "dev").lower()  # 不区分大小写

# 设置测试和正式环境地址
BASE_API_URLS = {
    "dev": "https://test-admin-fomsv2.everimaging.com/",
    "prod": "https://admin-fomsv2.everimaging.com/"
}


# 获取URL
def get_url(env: str = None):
    env = env or ENV  # 不传参则使用默认值ENV=dev
    if env not in BASE_API_URLS:
        raise ValueError(f"无效的环境参数:{env}")
    return BASE_API_URLS[env]
