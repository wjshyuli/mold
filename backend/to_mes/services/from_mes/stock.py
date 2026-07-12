

from to_mes.models import Correspondence
from to_mes.services.from_mes.mold import specification

def get_correspondence_dict():
    cor = Correspondence.objects.filter(capsule="205/55R16").first()
    return {
        item.capsule: item.clamp
        for item in Correspondence.objects.all()
    }


# def get_stock_show(factory):
#     now_list = specification(factory)
#
#     cor = get_correspondence_dict()
#
#     show_dic = {
#         "clamp":{},
#         "capsule":{},
#     }
#
#     for item in now_list:
#
#         capsule = item["jnbh"]
#         if capsule :
#             clamp = cor.get(capsule) or "未知夹盘"
#
#
#             # 胶囊数量
#             show_dic["capsule"][capsule] = show_dic["capsule"].get(capsule, 0) + 1
#
#             # 夹盘数量
#
#             show_dic["clamp"][clamp] = show_dic["clamp"].get(clamp, 0) + 1
#
#     show_dic["capsule"] = sort_dict_by_value(show_dic["capsule"])
#     show_dic["clamp"] = sort_dict_by_value(show_dic["clamp"])
#
#
#
#     capsule_dic = {}
#     clamp_dic = {}
#     capsule_list = list(capsule_dic.items())
#     clamp_list = list(clamp_dic.items())
#
#     result = []
#
#     max_len = max(len(capsule_list), len(clamp_list))
#
#     for i in range(max_len):
#
#         row = {}
#
#         if i < len(capsule_list):
#             row["capsule"] = capsule_list[i][0]
#             row["quantity1"] = capsule_list[i][1]
#         else:
#             row["capsule"] = ""
#             row["quantity1"] = ""
#
#         if i < len(clamp_list):
#             row["clamp"] = clamp_list[i][0]
#             row["quantity2"] = clamp_list[i][1]
#         else:
#             row["clamp"] = ""
#             row["quantity2"] = ""
#
#         result.append(row)
#
#     return result
#

def get_stock_show(factory):
    now_list = specification(factory)

    cor = get_correspondence_dict()

    capsule_dic = {}
    clamp_dic = {}

    # 统计数量
    for item in now_list:

        capsule = item["jnbh"]

        if not capsule:
            continue

        clamp = cor.get(capsule) or "未知夹盘"

        capsule_dic[capsule] = capsule_dic.get(capsule, 0) + 1
        clamp_dic[clamp] = clamp_dic.get(clamp, 0) + 1

    # 按数量排序
    capsule_dic = sort_dict_by_value(capsule_dic)
    clamp_dic = sort_dict_by_value(clamp_dic)

    capsule_list = list(capsule_dic.items())
    clamp_list = list(clamp_dic.items())

    result = []

    max_len = max(len(capsule_list), len(clamp_list))

    for i in range(max_len):

        row = {}

        if i < len(capsule_list):
            row["capsule"] = capsule_list[i][0]
            row["quantity1"] = capsule_list[i][1]
        else:
            row["capsule"] = ""
            row["quantity1"] = ""

        if i < len(clamp_list):
            row["clamp"] = clamp_list[i][0]
            row["quantity2"] = clamp_list[i][1]
        else:
            row["clamp"] = ""
            row["quantity2"] = ""

        result.append(row)

    return result



def sort_dict_by_value(dic):
    return dict(
        sorted(
            dic.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )



# import  requests
#-------- 1、硫化机规格设置
# def specification(factory):
#     factory_map = {
#         "1":get_specification_f1,
#         "2":get_specification_f2,
#         "30":get_specification_f3pcr,
#         "31":get_specification_f3tbr,
#         "4":get_specification_f4,
#     }
#     function = factory_map.get(factory)
#     if function:
#         return function()
#     else:
#         return {"result":"未知分厂"}
