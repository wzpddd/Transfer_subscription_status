import PySimpleGUI as sg

# UI部分

# 设置主题色为黑色，可修改
sg.theme("GrayGrayGray")
# 默认选项
options = ['vip', 'svip']

# 转移账号的固定展示文案内容
fixed_accounts = {
    "dev": "wzptestuser30@fotor.com",
    "prod": "wzpproduser30@fotor.com"
}

layout = [

    [sg.Text("当前环境:"),
     sg.Combo(["dev", "prod"], default_value="dev", key="-ENV-", readonly=True, enable_events=True)],
    # 用户 ID 输入框
    [sg.Text("请输入用户 ID:", size=(15, 1)),
     sg.InputText(key="user_id", size=(25, 1))],

    # 固定账号显示
    [sg.Text("默认转移账号为：", size=(15, 1)),
     sg.Input(default_text=fixed_accounts["dev"],
              disabled=True, key="fixed_uid", size=(25, 1), text_color='grey')],

    # 积分数量和充值相关控件
    [sg.Text("请输入积分数量：", size=(15, 1)),
     sg.InputText(key="credits_number", size=(8, 1), enable_events=True),
     sg.Button("充值")],

    # 下拉选择生成内容
    [sg.Text('生成会员兑换码：', size=(15, 1)),
     sg.Combo(options, key='-COMBO-', default_value=options[0], readonly=True, size=(6, 1)),
     sg.Button('确认')],

    # 功能按钮
    [sg.Button("移除订阅"), sg.Button("移除积分"),
     sg.Button("查询会员"), sg.Button("查询积分")],

    # 结果显示区域
    [sg.Multiline("", size=(50, 20), key="result", disabled=True)]
]
