from typing import Optional
import PySimpleGUI as sg
from services.query.query_account_status import isvip
from network.login import login_session
from services.remove_status.remove_vip import remove_status
from services.query.query_account_credits import query_account_credits
from services.remove_status.remove_credits import remove_account_credits
import json
import threading
from services.recharge.recharge_account_credits import recharge_account_credits


# 线程执行函数，避免未响应
def threaded_remove_vip(user_id, window):
    result = remove_vip(user_id)
    window.write_event_value("-VIP_DONE-", result)


try:
    session_cookie = login_session()  # e.g. {'fotorAdmin.sid': 'xxx'}
except Exception as e:
    sg.popup_error("❌ 登录失败", str(e))
    exit(1)

sg.theme("Black")


# 弹窗确认，不传值时使用预设文案，当选择yes返回true
def confirm_action(message="你确定要继续吗？"):
    return sg.popup_yes_no(message) == "Yes"


# 调用的工具函数
def remove_vip(user_id):
    return remove_status(user_id, cookies=session_cookie)


def query_status(user_id):
    return isvip(user_id, cookies=session_cookie)


def remove_credits(user_id: object) -> Optional[str]:
    return remove_account_credits(user_id, cookies=session_cookie)


def query_credits(user_id):
    return query_account_credits(user_id, cookies=session_cookie)


def recharge_credits(user_id,credits_num):
    return recharge_account_credits(user_id, credits_num,cookies=session_cookie)


def threaded_task(action, user_id, window,credits_number=None):
    if action == "remove_vip":
        result = remove_vip(user_id)
        window.write_event_value("-REMOVE_VIP_DONE-", result)
    elif action == "query_vip":
        result = query_status(user_id)
        window.write_event_value("-QUERY_VIP_DONE-", result)
    elif action == "remove_credits":
        result = remove_credits(user_id)
        window.write_event_value("-REMOVE_CREDITS_DONE-", result)
    elif action == "query_credits":
        result = query_credits(user_id)
        window.write_event_value("-QUERY_CREDITS_DONE-", result)
    elif action == "recharge_credits":
        result = recharge_credits(user_id,credits_number)
        window.write_event_value("-RECHARGE_CREDITS_DONE-", result)


# 布局
layout = [
    [sg.Text("请输入用户 ID:", size=(15, 1)),
     sg.InputText(key="user_id", size=(35, 1))],

    [sg.Text("默认转移账号为：", size=(15, 1)),
     sg.Input(default_text="wzptestuser30@fotor.com",
              disabled=True, key="fixed_uid", size=(35, 1),
              text_color='grey')],
    # 启动事件（方便后续代码监听该事件变化）
    [sg.Text("请输入积分数量：", size=(15, 1)),
     sg.InputText(key="credits_number", size=(8, 1), enable_events=True),
     sg.Button("充值")],

    [sg.Button("移除订阅"), sg.Button("移除积分"),
     sg.Button("查询会员"), sg.Button("查询积分")],

    [sg.Multiline("", size=(60, 30), key="result", disabled=True)]
]

# 创建窗口
window = sg.Window("自定义工具集合 🛠", layout)
# 事件循环
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    # 清空屏幕
    window["result"].update("")
    user_id = values["user_id"].strip()
    credits_number= values["credits_number"].strip()
    if not user_id:
        window["result"].update("⚠️ 请输入用户 ID！\n", append=True)
        continue

    # 监听输入的credits数量，只能是4个字符内的数字
    if event == "credits_number":
        val = values["credits_number"]
        # 过滤非法字符（非数字）
        filtered = ''.join(filter(str.isdigit, val))
        # 限制最大长度为4
        if len(filtered) > 4:
            filtered = filtered[:4]
        # 如果修正了内容，更新输入框
        if val != filtered:
            window["credits_number"].update(filtered)

    elif event == "移除订阅":
        if confirm_action("确认移除订阅吗？"):
            # 返回为true时执行
            window["result"].update("⏳ 正在移除订阅...\n")
            threading.Thread(target=threaded_task, args=("remove_vip", user_id, window), daemon=True).start()

    elif event == "查询会员":
        window["result"].update("⏳ 正在查询会员信息...\n")
        threading.Thread(target=threaded_task, args=("query_vip", user_id, window), daemon=True).start()

    elif event == "移除积分":
        # 增加二次确认
        if confirm_action("确认移除积分吗？"):
            # 返回为true时执行
            window["result"].update("⏳ 正在移除积分...\n")
            threading.Thread(target=threaded_task, args=("remove_credits", user_id, window), daemon=True).start()

    elif event == "查询积分":
        window["result"].update("⏳ 正在查询积分...\n")
        threading.Thread(target=threaded_task, args=("query_credits", user_id, window), daemon=True).start()

    elif event == "充值":
        # 如果没有输入数字就提示
        if not credits_number:
            window["result"].update("⚠️ 请输入想要充值的积分数量...\n",append=True)
            continue
        window["result"].update("⏳ 正在充值积分...\n")
        threading.Thread(target=threaded_task, args=("recharge_credits", user_id,window,credits_number), daemon=True).start()

    elif event in ("-REMOVE_VIP_DONE-", "-QUERY_VIP_DONE-", "-QUERY_CREDITS_DONE-", "-REMOVE_CREDITS_DONE-",
                   "-RECHARGE_CREDITS_DONE-"):
        result = values[event]


        def format_result(result):
            # 登录失效特判
            if isinstance(result, dict) and result.get("code") == "001":
                return "❌ 登录失效，请重新登录"

            # 是 dict，格式化输出
            if isinstance(result, dict):
                return json.dumps(result, ensure_ascii=False, indent=2)

            # 是 list，拼成换行字符串
            if isinstance(result, list):
                return "\n".join(str(item) for item in result)

            # 其他情况直接转字符串
            return str(result)


        window["result"].update(format_result(result) + "\n", append=True)
        window["result"].Widget.see("end")
window.close()
