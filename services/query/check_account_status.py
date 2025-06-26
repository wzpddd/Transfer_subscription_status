from network.vpn_connection import api_request
from network.login import login_session
from config.config import get_api




def isvip(uid:str):
    # 获取查询用户的url
    base_url = get_api("isvip", "dev")
    full_url = f"{base_url}/{uid}"
    response = api_request(full_url,"get")
    return response.text








