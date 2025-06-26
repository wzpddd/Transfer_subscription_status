import PySimpleGUI as sg
from services.query.check_account_status import query_order

sg.theme("Black")


# 假设的工具函数
def remove_member(user_id):
    return f"✅ 用户 {user_id} 的会员已被移除"


def query_status(user_id):
    return query_order(user_id)


def recharge(user_id):
    return f"💰 用户 {user_id} 成功充值 100 元"


# 布局
layout = [
    [sg.Text("请输入用户 ID:"), sg.InputText(key="user_id")],
    [sg.Button("移除会员"), sg.Button("查询状态"), sg.Button("充值")],
    [sg.Multiline("", size=(50, 10), key="result", disabled=True)]
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

    window["result"].update(result + "\n", append=True)

window.close()
