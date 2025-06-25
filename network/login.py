from network.vpn_connection import api_request
from config.config import get_api



api_url = get_api("login","dev")
print(api_url)

payload = {
    "username": "wuzhipeng@everimaging.com",
    "password": "123456" # 表单形式所有值都会转为字符串
}


#登录方法，返回token
def login():
    request_login = api_request(api_url, method="POST", json=payload)
    return request_login.json()["data"]["accessToken"]