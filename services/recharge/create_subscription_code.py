from network import vpn_connection
from network.vpn_connection import api_request
from utils.validate_user_input import validate_input
from utils.dict_tools import get_nested
from config.config import get_api

'''
获取兑换码列表，每次使用时新增一个兑换码，输出最后一页最后一个兑换码:
1、先通过get_code_use_info_url获取当前兑换码的具体情况，拿到总的兑换码数量和新增的兑换码个数
2、将上一步获取的数量传入add_coupon_code_url，设定新增1个兑换码
3、最后将第一步获取到的总数量得到最后一个code在第几页，使用get_activity_code_use_list_url直接查最后一页列表，直接拿到最后一个code
注：add_coupon_code 的 old_times = get_code_use_info_url 的times，都表示总的time数量
    add_coupon_code 的 oldaddtimes = get_code_use_info_url add_times， 表示后续新增数量
'''

vip_params = {
    "activity_id": 871,
    "code_id": 725,
    "activity_type": "random"
}
svip_params = {
    "activity_id": 870,
    "code_id": 724,
    "activity_type": "random"
}


def create_sub_code(vip_or_svip_params: dict, cookie=None) -> dict:
    add_coupon_code_url, get_code_use_info_url, get_activity_code_use_list_url = get_api("add_coupon_code",
                                                                                         "get_code_use_info",
                                                                                         "get_activity_code_use_list",
                                                                                         env="dev").values()

    result = api_request(get_code_use_info_url, 'get', params=vip_or_svip_params, cookies=cookie).json()
    if get_nested(result, "code") == "000":
        # 拿到总共的数量和新增的数量
        old_times = get_nested(result, "data", "times")
        old_add_times = get_nested(result, "data", "add_times")
        # 传入add 接口
        params = {
            "code_id": vip_or_svip_params["code_id"],
            "newTimes": 1,
            "oldTimes": old_times,
            "oldAddTimes": old_add_times,
            "codeType": "random"
        }
        # 新增兑换码
        result = api_request(add_coupon_code_url, 'post', json=params, cookies=cookie).json()
        if get_nested(result, "code") == "000":
            '''拿总数算出最后个code在第几页'''
            # 请求一页10个
            page_size = 10
            # 因为先执行查询，再添加，所以新的总数需要在老的数量上+1
            new_total_times = old_times + 1
            last_page_num = new_total_times // page_size + 1
            last_code_num = new_total_times % page_size - 1

            params = {
                "activity_type": "random",
                "code_id": vip_or_svip_params["code_id"],
                "activity_id": vip_or_svip_params["activity_id"],
                "pageNo": last_page_num,
                "pageSize": page_size
            }
            result = api_request(get_activity_code_use_list_url, 'get', params=params, cookies=cookie).json()
            last_code = get_nested(result, "data", "list", last_code_num, "code")
            return last_code
    return "❌ 新增兑换码失败"


def get_coupon_list(vip_or_svip=str, cookie=None):
    if vip_or_svip == "vip":
        return create_sub_code(vip_params, cookie)
    elif vip_or_svip == "svip":
        return create_sub_code(svip_params, cookie)
    return "出现未知错误"