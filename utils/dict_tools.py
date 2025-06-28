
'''字典操作工具，拿到字典中想要的数据'''

#常规写法：

def get_nested(d: dict, *keys) -> any:
    for key in keys:
        if not isinstance(d, dict):
            return None
        d = d.get(key)
    return d

#用法：传入文件，依次输入每层key : nickname = get_nested(response, "data", "user", "profile", "nickname")