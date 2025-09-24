import PySimpleGUI as sg
from utils.resource_path import get_resource_path
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
# 默认选项
options = ['vip', 'svip']
layout = [

    [sg.Text("当前环境："),
     sg.Combo(["dev", "prod"], default_value="dev", key="-ENV-", readonly=True, enable_events=True),
     sg.Push(),
     sg.Button("", key="-REFRESH-", image_filename=get_resource_path("assets/refresh(17x17).png"), image_size=(17, 17),
               border_width=1,
               pad=(0, 0))
     ],
    # 用户 ID 输入框
    [sg.Text("请输入用户 ID：", size=(15, 1)),
     sg.InputText(key="-USER_ID-", size=(25, 1))],

    # 固定账号显示
    [sg.Text("默认转移账号为：", size=(15, 1)),
     sg.Input(default_text="wzptestuser30@fotor.com",
              disabled=True, key="-FIXED_UID-", size=(25, 1))],

    # 积分数量和充值相关控件
    [sg.Text("请输入积分数量：", size=(15, 1)),
     sg.InputText(key="-CREDITS_NUMBER-", size=(8, 1), enable_events=True),
     sg.Button("充值")],

    # 下拉选择生成内容
    [sg.Text('生成会员兑换码：', size=(15, 1)),
     sg.Combo(options, key='-COMBO-', default_value=options[0], readonly=True, size=(6, 1)),
     sg.Button('确认')],

    # 功能按钮
    [sg.Button("移除订阅"), sg.Button("移除积分"),
     sg.Button("查询会员"), sg.Button("查询积分")],

    # 结果显示区域
    [sg.Multiline("", size=(50, 20), key="-RESULT-", disabled=True)]
]

# 创建窗口
window = sg.Window("自定义工具集合 🛠", layout)
while True:
    values = window.read()
window.close()
