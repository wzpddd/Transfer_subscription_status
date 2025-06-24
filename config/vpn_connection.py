"""VPN连接和方法"""

import requests
from network.http_request import base_url

#添加VPN配置，和网页中的插件配置以相同，无需用户名密码
VPN_config = {
    "vpn_host": "192.168.1.101",
    "vpn_port": 7890,
    # "username": "user",
    # "password": "pass"
}

proxy_url = f"http://{VPN_config['vpn_host']}:{VPN_config['vpn_port']}"

proxies = {
    "http": proxy_url,
    "https": proxy_url,
}


response = requests.get(base_url, proxies=proxies ,timeout=10)#这里接着写，将URL换成测试环境的登录接口
