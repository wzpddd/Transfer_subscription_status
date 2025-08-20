
#如果字典里
''''''
#常规写法：

def get_nested(d: dict, *keys) -> any:
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key)
        elif isinstance(d, list) and isinstance(key, int):
            if 0 <= key < len(d):
                d = d[key]
            else:
                return None
        else:
            return None
    return d

