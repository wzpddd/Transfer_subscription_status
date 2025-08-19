from network import vpn_connection
from network.vpn_connection import api_request
from utils.validate_user_input import validate_input
from utils.dict_tools import  get_nested
from config.config import get_api

'''
获取兑换码列表，每次使用时新增一个兑换码，输出最后一页最后一个兑换码:
1、先通过getCodeUseInfo获取当前兑换码的具体情况，拿到总的兑换码数量和新增的兑换码个数
2、将上一步获取的数量传入addCouponCodeTime，设定新增1个兑换码
3、最后将第一步获取到的总数量得到最后一个code在第几页，使用getActivityCodeUseList直接查最后一页列表，直接拿到最后一个code
'''
def create_sub_code(pro_or_proplus, cookie=None):
    add_coupon_code_api,get_code_use_info_api,get_code_use_info_api = get_api("add_coupon_code","get_code_use_info","get_activity_code_use_list","dev").values()
    activity_id_pro = 863
    if pro_or_proplus == "pro":
        params:{
            "activity_id": 863,
            "code_id":717,
            "activity_type":"random"
        }
    elif pro_or_proplus == "pro_plus":
        params:{
            "activity_id": 870,
            "code_id": 724,
            "activity_type": "random"
        }


    return