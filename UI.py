import PySimpleGUI as sg
from services.query.query_account_status import isvip
from network.login import login_session




try:
    session_cookie = login_session()  # e.g. {'fotorAdmin.sid': 'xxx'}
except Exception as e:
    sg.popup_error("❌ 登录失败", str(e))
    exit(1)

sg.theme("Black")


# 假设的工具函数
def remove_member(user_id):
    return f"✅ 用户 {user_id} 的会员已被移除"


def query_status(user_id):
    return isvip(user_id,cookies = session_cookie)


def recharge(user_id):
    return f"💰 用户 {user_id} 成功充值 100 元"


# 布局
layout = [
    [sg.Text("请输入用户 ID:"), sg.InputText(key="user_id")],
    [sg.Button("移除会员"), sg.Button("查询状态"), sg.Button("充值")],
    [sg.Multiline("", size=(60, 30), key="result", disabled=True)]
]

# 创建窗口
window = sg.Window("🛠 自定义工具集合", layout)
# 事件循环
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    user_id = values["user_id"].strip()
    if not user_id:
        window["result"].update("⚠️ 请输入用户 ID！\n", append=True)
        continue

    if event == "移除会员":
        result = remove_member(user_id)
    elif event == "查询状态":
        result = query_status(user_id)
    elif event == "充值":
        result = recharge(user_id)
    else:
        result = "❓ 未知操作"

    if isinstance(result, list):
        result = "\n".join(str(item) for item in result)
    window["result"].update(result + "\n", append=True)

window.close()
