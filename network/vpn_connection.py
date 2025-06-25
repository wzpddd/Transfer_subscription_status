"""VPN连接和方法，其他模块直接调用，设计中无需持久化"""
import requests

#添加VPN配置，和网页中的插件配置以相同，无需用户名密码
VPN_config = {
    "vpn_host": "192.168.1.101",
    "vpn_port": 7890,
    # "username": "user",  公司vpn中未设置链接账号和密码
    # "password": "pass"
}


#vpn链接方法
def vpn_connection():
    proxy_url = f"http://{VPN_config['vpn_host']}:{VPN_config['vpn_port']}"
    return  {"http": proxy_url, "https": proxy_url}



#调用方法请求url，拿到返回体
def api_request(url, method="GET",**kwargs):
    """带VPN代理的通用HTTP请求函数"""
    return requests.request(
        method=method,      # 请求方法(GET/POST等)
        url=url,            # 目标URL
        proxies=vpn_connection(), # 自动注入VPN代理配置
        timeout=kwargs.pop('timeout', 10),  # 默认10秒超时
        **kwargs            # 其他requests参数(headers/data等)
    )