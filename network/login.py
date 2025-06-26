from network.vpn_connection import api_request, vpn_connection
from config.config import get_api
import requests

api_url = get_api("login", "dev")
# print(api_url)

payload = {
    "username": "wuzhipeng@everimaging.com",
    "password": "123456"
}



# 登录方法，返回session_token
def login_session():
    session = requests.Session()  # 持久化链接
    session.proxies = vpn_connection()
    response = session.post(api_url,json=payload)
    if response.status_code == 200:
        # 从返回体头获取 Cookie 值
        session_cookie = response.cookies.get_dict()
        # print(session_cookie)
        return session_cookie
login_session()
