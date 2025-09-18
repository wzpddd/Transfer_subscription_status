from config.config import get_api,get_account
from network.vpn_connection import api_request
from utils.timestamp import format_timestamp_ms
from utils.validate_user_input import validate_input


'''订阅列表还是通过UID查询的，所以先调用接口查询UID'''


# 获取账号的订阅列表
def remove_status(uid_or_email, cookies=None):
    #先对输入账号进行合法判断，邮箱则返回uid
    uid = validate_input(uid_or_email, cookies=cookies)

    if uid == "invalid":
        return f"❌ 查询失败，该邮箱：{uid_or_email}无效或错误"

    # 返回uid正确时，进行请求判断
    url = get_api("user_payment", env="dev")
    params = {
        "key": "subscription",
        "value": uid,
        "status": "",
        "pageNo": "1",
        "pageSize": "200",
        "payState": ""
    }
    try:
        results = api_request(url, "get", cookies=cookies, params=params).json()
        print(results)
        # 登录失效或请求失败直接返回
        if results.get("code") != "000":
            return f"❌ 请求失败：{results.get('message')}"
        '''
            根据接口分析：
            如果账号有误，那么返回的"data"为列表 eg: {'code': '000', 'message': '成功！', 'data': []}
            如果账号正确，那么返回的"data"为字典 eg: {'code': '000', 'message': '成功！', 'data': {}}
            这样可以区分输入错误和输入正确但确实无订阅的情况
        '''

        data = results.get("data")
        if isinstance(data, list) and not data:
            return "❌ 查询账号有误，请检查。"
        if isinstance(data, dict) and not data:
            return "📭 当前账号无订阅"

        # 提取list字典
        subscriptions = data.get("list", [])
        # 如果返回的"data"中有list，但list为空，就再加一种情况判断
        if not subscriptions:
            return "📭 当前账号无订阅"
        # 仅提取其中的id,订阅类型和生效时间
        result = []
        for item in subscriptions:
            _id = item.get("id", "N/A")
            _desc = item.get("description", "无")
            ts = item.get("create_time")
            dt = format_timestamp_ms(ts)
            result.append(f"🆔 套餐ID：{_id}\n📅 创建时间：{dt}\n📝 订阅类型：{_desc}\n" + "-" * 50)

    # 设置默认转移账号,一般不会更改
        tansfer_url = get_api("transfer_subscribe", env="dev")
        headers = {
            "x-app-id" : "app-fotor-web"
        }
        for item in subscriptions:
            params = {
                "ids" : [item.get("id")],
                "toUid":get_account("test")
            }

            tansfer_respones = api_request(tansfer_url,"post",cookies=cookies, headers=headers,json=params).json()
        if tansfer_respones.get("code") != "000":
            return "转移失败"
        return "\n".join(result) + "\n✅ 转移成功"

    except Exception as e:
        return f"❌ 请求异常：{str(e)}"
