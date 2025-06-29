import PySimpleGUI as sg
from services.query.query_account_status import isvip
from network.login import login_session
from services.remove_status.remove_vip import remove_status
import json
import threading

#线程执行函数，避免未响应
def threaded_remove_vip(user_id, window):
    result = remove_vip(user_id)
    window.write_event_value("-VIP_DONE-", result)

try:
    session_cookie = login_session()  # e.g. {'fotorAdmin.sid': 'xxx'}
except Exception as e:
    sg.popup_error("❌ 登录失败", str(e))
    exit(1)

sg.theme("Black")


# 假设的工具函数
def remove_vip(user_id):
    return remove_status(user_id, cookies=session_cookie)


def query_status(user_id):
    return isvip(user_id, cookies=session_cookie)


def recharge(user_id):
    return f"💰 用户 {user_id} 成功充值 100 元"

def threaded_task(action, user_id, window):
    if action == "remove":
        result = remove_vip(user_id)
        window.write_event_value("-REMOVE_DONE-", result)
    elif action == "query":
        result = query_status(user_id)
        window.write_event_value("-QUERY_DONE-", result)
    elif action == "recharge":
        result = recharge(user_id)
        window.write_event_value("-RECHARGE_DONE-", result)

# 布局
layout = [
    [sg.Text("请输入用户 ID:"), sg.InputText(key="user_id")],
    [sg.Text("默认转移账号为："),sg.Input(default_text="wzptestuser30@fotor.com", disabled=True, key="fixed_uid", size=(40, 1),
              text_color='grey')],
    [sg.Button("移除订阅"), sg.Button("查询会员"), sg.Button("充值")],
    [sg.Multiline("", size=(60, 30), key="result", disabled=True)]
]

# 创建窗口
window = sg.Window("🛠 自定义工具集合", layout)
# 事件循环
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    # 清空屏幕
    window["result"].update("")
    user_id = values["user_id"].strip()
    if not user_id:
        window["result"].update("⚠️ 请输入用户 ID！\n", append=True)
        continue

    if event == "移除订阅":
        window["result"].update("⏳ 正在移除订阅，请稍候...\n")
        threading.Thread(target=threaded_task, args=("remove", user_id, window), daemon=True).start()
    elif event == "查询会员":
        window["result"].update("⏳ 正在查询会员信息...\n")
        threading.Thread(target=threaded_task, args=("query", user_id, window), daemon=True).start()
    elif event == "充值":
        window["result"].update("⏳ 正在充值...\n")
        threading.Thread(target=threaded_task, args=("recharge", user_id, window), daemon=True).start()
    elif event in ("-REMOVE_DONE-", "-QUERY_DONE-", "-RECHARGE_DONE-"):
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
