import re
from services.query import query_account_uid


"""验证用户输入是否符合邮箱或UID格式"""


def validate_input(input_str: str,cookies=None) -> str:
    #去除前后空格
    input_str = input_str.strip()

    # 判断是否是合法邮箱
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(email_pattern, input_str):
        # 将输入的邮箱查询UID
        uid = query_account_uid(input_str, cookies=cookies)
        return uid

    # 判断是否是合法 UID：32位、只包含字母和数字
    uid_pattern = r'^[a-zA-Z0-9]{32}$'
    if re.match(uid_pattern, input_str):
        return input_str

    return "invalid"
