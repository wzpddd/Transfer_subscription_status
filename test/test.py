from config.config import get_api
import requests



#获取环境地址
base_url = get_api("login","prod")

print(base_url)
VPN_config = {
    "vpn_host": "192.168.1.101",
    "vpn_port": 7890,
}

