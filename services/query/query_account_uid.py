from config.config import get_api
from network.vpn_connection import api_request

'''查询邮箱的UID'''
def query_account_uid(env,email, cookies=None):
        url = get_api("user_info", env=env)
        params = {
            "appleName": "",
            "pageNo": '1',
            "pageSize": "10",
            "type": "email",
            "value": email
        }
        try:
            response = api_request(url, params=params, cookies=cookies, timeout=10).json()
            data =  response.get("data", [{}])[0].get('uid')
            return data or None
        except Exception:
            return None
