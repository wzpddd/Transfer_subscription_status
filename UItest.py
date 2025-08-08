import PySimpleGUI as sg

layout = [
    [sg.Text("请输入用户 ID:", size=(15, 1)),
     sg.InputText(key="user_id", size=(35, 1))],

    [sg.Text("默认转移账号为：", size=(15, 1)),
     sg.Input(default_text="wzptestuser30@fotor.com",
              disabled=True, key="fixed_uid", size=(35, 1),
              text_color='grey')],

    [sg.Text("请输入积分数量：", size=(15, 1)),
     sg.InputText(
         key="credit_amount",
         size=(8, 1),
         enable_events=True
     ),
     sg.Button("确定", key="submit_credit")],

    [sg.Button("移除订阅"), sg.Button("移除积分"),
     sg.Button("查询会员"), sg.Button("查询积分")],

    [sg.Multiline("", size=(60, 30), key="result", disabled=True)]
]

# 创建窗口
window = sg.Window("🛠 自定义工具集合", layout)
window.read()
