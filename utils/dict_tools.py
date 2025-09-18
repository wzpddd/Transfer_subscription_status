'''
    自动从嵌套结构中逐层取值，支持字典内有列表，列表里有字典。
    使用方法：get_nested(list,"xxx","xxx")
    如果有列表索引时，直接写出int代表：get_nested(list,"xxx","xxx",2)
    此方法只能取单个值，如果需要批量取值，可以使用三方库:glom
    示例
    origin_data = {
       "aa":{
       "bb":{
       "cc":{
       "dd":[xxx]
    }
    spec = {
    "xxx": "aa.bb.cc.dd",
    "......",
    }
    reslut = glom(origin_data, spec)
    返回结果为字典，直接取对应值即可
    get_item = reslut["xxx"]
'''


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
