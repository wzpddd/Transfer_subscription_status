'''转换时间戳'''

import datetime


def format_timestamp_ms(timestamp_ms):
    if not timestamp_ms:
        return "无效时间"
    try:
        return datetime.datetime.fromtimestamp(timestamp_ms / 1000).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return "解析失败"