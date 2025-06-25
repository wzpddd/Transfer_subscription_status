from network.vpn_connection import api_request
from network.login import login_session
from config.config import get_api

# 设置查询用户的url
api_url = get_api("user_info", "dev")
print(api_url)

# 获取界面中输入的uid
# uid = input()
uid = "447fbc23af2a49c19ff470934815fe35"

#拼接url带参
url = f"{api_url}?key=subscription&value={uid}&pageNo=1&pageSize=100&status=1&pageSize=100"


def query_uid():
    cookie = login_session()
    query_url = api_request(url, method="get", cookies=cookie)
    print(query_url.text)
    return query_url


query_url = query_uid()
