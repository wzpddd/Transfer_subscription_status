from typing import Optional
import PySimpleGUI as sg

from UI import fixed_accounts
from services.query.query_account_status import isvip
from network.login import login_session
from services.remove_status.remove_vip import remove_status
from services.query.query_account_credits import query_account_credits
from services.remove_status.remove_credits import remove_account_credits
import json
import threading
from services.recharge.recharge_account_credits import recharge_account_credits
from services.recharge.create_subscription_code import get_coupon_list
import UI


current_env = "dev"
try:
    session_cookie = login_session(current_env)  # e.g. {'fotorAdmin.sid': 'xxx'}
except Exception as e:
    sg.popup_error("❌ 请检查网络", str(e))
    exit(1)


# 弹窗确认，不传值时使用预设文案，当选择yes返回true
def confirm_action(message="你确定要继续吗？"):
    return sg.popup_yes_no(message) == "Yes"

# 调用工具函数
def remove_vip(user_id):
    return remove_status(current_env,user_id,cookies=session_cookie)

def query_status(user_id):
    return isvip(current_env,user_id,cookies=session_cookie)

def remove_credits(user_id: object) -> Optional[str]:
    return remove_account_credits(current_env,user_id,cookies=session_cookie)

def query_credits(user_id):
    return query_account_credits(current_env,user_id,cookies=session_cookie)

def recharge_credits(user_id,credits_number):
    return recharge_account_credits(current_env,user_id, credits_number,cookies=session_cookie)

def create_sub_code(vip_or_svip):
    return get_coupon_list(current_env,vip_or_svip, cookie=session_cookie)

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
    elif action == "create_sub_code":
        result = create_sub_code(user_id)
        window.write_event_value("-CREATE_SUB_CODE_DONE-", result)
    elif action == "change_env":
        try:
            session_cookie = login_session(user_id)  # 这里 user_id 就传 chosen_env
            window.write_event_value("-CHANGE_ENV_DONE-", (user_id, session_cookie))
        except Exception as e:
            window.write_event_value("-CHANGE_ENV_DONE-", (user_id, e))


# main
# 创建窗口
window = sg.Window("自定义工具集合 🛠", UI.layout)
# 事件循环
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    # 清空屏幕
    window["result"].update("")
    user_id = values["user_id"].strip()
    credits_number= values["credits_number"].strip()

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

    # 监听按钮事件名
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
        if confirm_action("⚠️ 确认移除积分吗？"):
            # 返回为true时执行
            window["result"].update("⏳ 正在移除积分...\n")
            threading.Thread(target=threaded_task, args=("remove_credits", user_id, window), daemon=True).start()

    elif event == "查询积分":
        window["result"].update("⏳ 正在查询积分...\n")
        threading.Thread(target=threaded_task, args=("query_credits", user_id, window), daemon=True).start()

    elif event == "充值":
        if not user_id:
            window["result"].update("⚠️ 请输入用户 ID！\n", append=True)
            continue
        # 如果没有输入数字就提示
        if not credits_number:
            window["result"].update("⚠️ 请输入想要充值的积分数量...\n",append=True)
            continue
        window["result"].update("⏳ 正在充值积分...\n")
        threading.Thread(target=threaded_task, args=("recharge_credits", user_id,window,credits_number), daemon=True).start()

    elif event == "确认":
        vip_status = values["-COMBO-"]
        window["result"].update("⏳ 正在生成会员兑换码...\n")
        threading.Thread(target=threaded_task, args=("create_sub_code", vip_status , window), daemon=True).start()

    elif event == "-ENV-":
        chosen_env = values["-ENV-"]

        if chosen_env == "prod":
            if not confirm_action("⚠️ 确认切换到正式环境吗？"):
                window["-ENV-"].update(current_env)
                continue

        window["result"].update(f"⏳ 正在切换到 {chosen_env} 环境...\n")

        threading.Thread(
            target=threaded_task,
            args=("change_env", chosen_env, window),
            daemon=True
        ).start()

    elif event == "-CHANGE_ENV_DONE-":
        chosen_env, result = values[event]
        if isinstance(result, dict):  # 登录成功，拿到了 cookie
            session_cookie = result
            # 在成功拿到cookie后才更新当前环境
            current_env = chosen_env
            window["result"].update(f"✅ 已切换到 {current_env} 环境\n", append=True)
            # 刷新默认转移账号文案
            window["fixed_uid"].update(fixed_accounts[current_env])
            # 将输入框内的文案清空
            window["user_id"].update("")
            window["credits_number"].update("")
        else:  # 登录失败
            window["-ENV-"].update(current_env)  # 回到原来的环境
            window["result"].update(f"❌ 切换环境失败: {result}\n", append=True)



    elif event in ("-REMOVE_VIP_DONE-", "-QUERY_VIP_DONE-", "-QUERY_CREDITS_DONE-", "-REMOVE_CREDITS_DONE-",
                   "-RECHARGE_CREDITS_DONE-","-CREATE_SUB_CODE_DONE-","-CHANGE_ENV_DONE-"):
        result = values[event]



    # 处理返回结果文案
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

    # 在界面上输出更新内容
        window["result"].update(format_result(result) + "\n", append=True)
        window["result"].Widget.see("end")
window.close()
