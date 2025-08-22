import PySimpleGUI as sg

options = ['pro', 'pro+']

# layout = [
#     [sg.Text("请输入用户 ID:", size=(15, 1)),
#      sg.InputText(key="user_id", size=(35, 1))],
#
#     [sg.Text("默认转移账号为：", size=(15, 1)),
#      sg.Input(default_text="wzptestuser30@fotor.com",
#               disabled=True, key="fixed_uid", size=(35, 1),
#               text_color='grey')],
#     # 启动事件（方便后续代码监听该事件变化）
#     [sg.Text("请输入积分数量：", size=(15, 1)),
#      sg.InputText(key="credits_number", size=(8, 1), enable_events=True),
#      sg.Button("充值")],
#
#     [sg.Button("移除订阅"), sg.Button("移除积分"),
#      sg.Button("查询会员"), sg.Button("查询积分")],
#
#     [sg.Multiline("", size=(60, 30), key="result", disabled=True)]
# ]
# sg.theme_previewer()
sg.theme("GrayGrayGray")
layout = [
    # 用户 ID 输入框
    [sg.Text("请输入用户 ID:", size=(15, 1)),
     sg.InputText(key="user_id", size=(25, 1))],

    # 固定账号显示
    [sg.Text("默认转移账号为：", size=(15, 1)),
     sg.Input(default_text="wzptestuser30@fotor.com",
              disabled=True, key="fixed_uid", size=(25, 1), text_color='grey')],

    # 积分数量和充值相关控件
    [sg.Text("请输入积分数量：", size=(15, 1)),
     sg.InputText(key="credits_number", size=(8, 1), enable_events=True),
     sg.Button("充值")],

    # 会员兑换码选择框和确认按钮
    [sg.Text('生成会员兑换码：', size=(15, 1)),
     sg.Combo(options, key='-COMBO-', default_value='pro', readonly=True, size=(6, 1)),
     sg.Button('确认')],

    # 功能按钮
    [sg.Button("移除订阅"), sg.Button("移除积分"),
     sg.Button("查询会员"), sg.Button("查询积分")],

    # 结果显示区域
    [sg.Multiline("", size=(50, 20), key="result", disabled=True)]
]

# 创建窗口
window = sg.Window("自定义工具集合 🛠", layout)
while True:
    values = window.read()
window.close()