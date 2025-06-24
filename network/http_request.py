import requests
from config.vpn_connection import VPN_config
from config.config import get_url

proxy_url = f"http://{VPN_config['vpn_host']}:{VPN_config['vpn_port']}"

proxies = {
    "http": proxy_url,
    "https": proxy_url,
}

base_url = get_url()
response = requests.get(base_url, proxies=proxies ,timeout=10)
print(response.text)