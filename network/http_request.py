import requests


class VPNConnection:
    def __init__(self, vpn_config):
        self.config = vpn_config
        self.session = requests.Session()
    def connect(self):
        proxy_a