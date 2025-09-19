from network.vpn_connection import api_request, vpn_connection
from config.config import get_api,login_account
import requests



# 登录方法，返回session_token
def login_session(env):
    # 根据环境获取登录账号，拿到cookie
    api_url = get_api("login",env=env)
    session = requests.Session()  # 持久化链接
    session.proxies = vpn_connection()
    response = session.post(api_url, json=login_account[env])
    print(login_account[env])
    response.raise_for_status()
    if response.status_code == 200:
        # 从返回体头获取 Cookie 值
        session_cookie = response.cookies.get_dict()
        print(session_cookie)
        return session_cookie
    else:
        raise Exception("登录失败")

