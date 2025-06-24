from config.config import get_url
import requests



#获取环境地址
base_url = get_url()
VPN_config = {
    "vpn_host": "192.168.1.101",
    "vpn_port": 7890,
}

proxy_url = f"http://{VPN_config['vpn_host']}:{VPN_config['vpn_port']}"

proxies = {
    "http": proxy_url,
    "https": proxy_url,
}


response = requests.get(base_url, proxies=proxies ,timeout=10)
print(response.text)