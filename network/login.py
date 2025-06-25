import requests
from config.vpn_connection import api_request
from config.config import get_api



api_url = get_api("login","dev")
print(api_url)

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://test-admin-fomsv2.everimaging.com",
    "Referer": "https://test-admin-fomsv2.everimaging.com/"
}

payload = {
    "username": "wuzhipeng@everimaging.com",
    "password": "123456" # 表单形式所有值都会转为字符串
}


request_login=api_request(api_url,method="POST", json=payload)

print(type(request_login))