from network import vpn_connection
from network.vpn_connection import api_request
from utils.validate_user_input import validate_input
from utils.dict_tools import  get_nested
from config.config import get_api

'''
获取兑换码列表，每次使用时新增一个兑换码，输出最后一页最后一个兑换码:
1、先通过get_code_use_info_url获取当前兑换码的具体情况，拿到总的兑换码数量和新增的兑换码个数
2、将上一步获取的数量传入add_coupon_code_url，设定新增1个兑换码
3、最后将第一步获取到的总数量得到最后一个code在第几页，使用get_activity_code_use_list_url直接查最后一页列表，直接拿到最后一个code
注：add的old_times = get_code_use_info_url 的times，都表示总的time数量
add的oldaddtimes = get_code_use_info_url add_times,表示后续新增数量
'''
def create_sub_code(pro_or_proplus =str , cookie=None):
    add_coupon_code_url,get_code_use_info_url,get_activity_code_use_list_url = get_api("add_coupon_code","get_code_use_info","get_activity_code_use_list",env="dev").values()
    pro_code_params={
        "activity_id": 871,
        "code_id": 725,
        "activity_type": "random"
    }
    proplus_code_params={
        "activity_id": 870,
        "code_id": 724,
        "activity_type": "random"
    }
    if pro_or_proplus == "pro":
        result = api_request(get_code_use_info_url,'get',params=pro_code_params,cookies=cookie).json()
        print(result)
        if get_nested(result,"code") == "000" :
            #拿到总共的数量和新增的数量
            total_times =  get_nested(result,"data","times") + get_nested(result,"data","times")
            add_times = get_nested(result,"data","add_times")
            # 传入add 接口
            params = {
                "code_id": pro_code_params["code_id"],
                "newTimes": 1,
                "oldTimes": times,
                "oldAddTimes": add_times,
                "codeType": "random"
            }
            # 新增兑换码
            result = api_request(add_coupon_code_url,'post',json=params,cookies=cookie).json()
            print(result)
            if get_nested(result,"code") =="000":
                # 拿总数得出最后个code在第几页
                page_size = 10
                last_page_num = times // page_size + 1
                last_code_num = times % page_size -1
                print(last_page_num)
                print(last_code_num)
                params = {
                    "activity_type": "random",
                    "code_id": pro_code_params["code_id"],
                    "activity_id": pro_code_params["activity_id"],
                    "pageNo":last_page_num ,
                    "pageSize" : page_size
                }
                result = api_request(get_activity_code_use_list_url,'get',params=params,cookies=cookie).json()
                print(result)
                last_code = get_nested(result,"data","list",last_code_num,"code")
                print(last_code)
                return last_code

    elif pro_or_proplus == "pro_plus":
        return



cookies = {
    "fotorAdmin.sid": "s%3A4Sy0QYmisRplDRX842xxveGwXFMuciJw.1Ox7vqGt66eNgQqWqul8b%2Bs098ZcCJii72Mt3uOwC18"
}

create_sub_code("pro",cookies)