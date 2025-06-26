'''调用登录获取登录状态'''

# def query_order(uid: str):
#
#
#     params = {
#         "key": "subscription",  # 类型为订阅
#         "pageNo": 1,
#         "pageSize": 100,  # 设置大一点全都传过来，默认为10
#         "type": input_type,  # 输入的内容类型
#         "value": uid,  # 想要查询UID
#         "status": 1  # 状态为1的，即订阅中，但后端将>0的都返回了，这条无效
#     }
#
#     # 使用登录方法获取session_cookie
#     cookie = login_session()
#     # 获取输入账号的订阅清单
#     order_list = api_request(api_url, "get", params=params, cookies=cookie)  # 调用接口
#
#     try:
#         order_list = order_list.json()  # 转换返回值为json文件
#     except Exception as e:
#         return("响应解析失败:", e)
#
#     # 查询status为1的
#     subscriptions = order_list.get("data", {}).get("list", [])
#     has_active = False
#     result_list = []
#     for sub in subscriptions:
#         if sub.get("status") == 1:
#             result_list.append("🔹 当前生效的订阅：")
#             result_list.append(f"  订阅名：{sub.get('name')}")
#             result_list.append(f"  金额：{sub.get('subscription_amount') / 100:.2f} {sub.get('subscription_currency')}")
#             result_list.append(f"  平台状态：{sub.get('platform_status')}")
#             result_list.append("-" * 30)
#             has_active = True
#             return result_list
#
#     if not has_active:
#         return ("没有生效的订阅")
