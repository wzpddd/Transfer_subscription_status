from network.vpn_connection import api_request
from config.config import get_api


#获取查询用户的url
api_url = get_api("user_info","dev")
print(api_url)
#获取本地
uid = input()

url = f"{api_url}?key=subscription&value={uid}&pageNo=1&pageSize=100"

def query_uid():
    query_url = api_request(api_url, method="get")
    print(query_url.json())
    return query_url

query_url = query_uid()