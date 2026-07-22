import  requests
from django.utils.dateparse import postgres_interval_re


#-------- 1、硫化机规格设置
def specification(factory):
    factory_map = {
        "1":get_specification_f1,
        "2":get_specification_f2,
        "30":get_specification_f3pcr,
        "31":get_specification_f3tbr,
        "4":get_specification_f4,
    }
    function = factory_map.get(factory)
    if function:
        return function()
    else:
        return {"result":"未知分厂"}




#------------2、周期牌更话
def weekcard(body):
    factory=str(body.get('factory',1))
    st=str(body.get('st'))
    et=str(body.get('et'))
    print(factory,st,et)
    req={
        "factory":factory,
        "startDate":st,
        "endDate":et,
    }
    factory_map = {
        "1": get_weekcard_f1,
        "2": get_weekcard_f2,
        "30": get_weekcard_f3pcr,
        "31": get_weekcard_f3tbr,
        "4": get_weekcard_f4,
    }
    function = factory_map.get(factory)
    print(function)
    print(function.__name__)
    print(req)
    if function:
        return function(req)
    else:
        return {"result": "未知分厂"}
#------------3、模具状态
def mold_status(body):
    factory = str(body.get('factory', 1))
    req={}
    factory_map = {
        "1": mold_status_f1,
        "2": mold_status_f2,
        "30": mold_status_f3pcr,
        "31": mold_status_f3tbr,
        "4": mold_status_f4,
    }
    function = factory_map.get(factory)
    print('执行'+factory+'分厂的获取模具状态函数程序')
    print(req)

    if function:

        return function(req)
    else:
        return {"result": "未知分厂"}
#------------3、停机统计
def stop_status(body):
    factory = str(body.get("factory", "1"))
    query_type = body.get("type", "detail")
    st=str(body.get('st'))
    et=str(body.get('et'))
    print(factory,st,et)
    req={

        "k_date":st,
        "e_date":et,
    }

    function_map = {
        "1": {
            "detail": stop_status_f1_detail,
            "summary": stop_status_f1_summary,
            "machine": stop_status_f1_machine,
            "shift": stop_status_f1_shift,
        },
        "2": {
            "detail": stop_status_f2_detail,
            "summary": stop_status_f2_summary,
            "machine": stop_status_f2_machine,
            "shift": stop_status_f2_shift,
        },
        "30": {
            "detail": stop_status_f3pcr_detail,
            "summary": stop_status_f3pcr_summary,
            "machine": stop_status_f3pcr_machine,
            "shift": stop_status_f3pcr_shift,
        },
        "31": {
            "detail": stop_status_f3tbr_detail,
            "summary": stop_status_f3tbr_summary,
            "machine": stop_status_f3tbr_machine,
            "shift": stop_status_f3tbr_shift,
        },
        "4": {
            "detail": stop_status_f4_detail,
            "summary": stop_status_f4_summary,
            "machine": stop_status_f4_machine,
            "shift": stop_status_f4_shift,
        },
    }

    function = function_map.get(factory, {}).get(query_type)

    print(f"分厂：{factory}")
    print(f"类型：{query_type}")

    if function:
        return function(req)

    return {
        "result": "未知分厂或查询类型"
    }

#------------4、停机报表
def stop_report(factory):
    if factory == "1":
        return stop_report_f1()
    elif factory == "2":
        return stop_report_f2()
    elif factory == "31":
        return stop_report_f3pcr()
    elif factory == "32":
        return stop_report_f3tbr()
    elif factory == "33":
        return stop_report_f4()
    else:
        return {"result":"未知分厂，结果错误"}






#-----------------具体子函数
def get_specification_f1():
    url="http://10.3.10.61:18080/WebJtggsz/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    body = {}
    response = requests.post( url=url, headers=headers, json=body)
    data=response.json().get('Object')

    return data
def get_specification_f2():
    url="http://10.3.10.62:18080/WebJtggsz/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    body = {}
    response = requests.post( url=url, headers=headers, json=body)
    data=response.json().get('Object')

    return data
def get_specification_f3pcr():
    url="http://10.3.10.64:18080/WebJtggsz/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    body = {}
    response = requests.post( url=url, headers=headers, json=body)
    data=response.json().get('Object')
    return data
def get_specification_f3tbr():
    url="http://10.3.10.64:18081/WebJtggsz/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    body = {}
    response = requests.post( url=url, headers=headers, json=body)
    data=response.json().get('Object')

    return data
def get_specification_f4():
    return {
        "factory_no":4,
        "result":"sifencshuju"
    }

#-----------------
def get_weekcard_f1(body):
    url="http://10.3.10.61:18080/Webjtzqhghjl/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }



    response = requests.post( url=url, headers=headers, json=body)
    data=response.json().get('Object')

    return data
def get_weekcard_f2(body):
    url="http://10.3.10.62:18080/Webjtzqhghjl/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }

    response = requests.post( url=url, headers=headers, json=body)
    data=response.json().get('Object')
    return data
def get_weekcard_f3pcr(body):
    url="http://10.3.10.64:18080/Webjtzqhghjl/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    response = requests.post( url=url, headers=headers, json=body)
    data=response.json().get('Object')
    return data
def get_weekcard_f3tbr(body):


    url="http://10.3.10.64:18081/Webjtzqhghjl/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    response = requests.post( url=url, headers=headers, json=body)
    data=response.json().get('Object')
    return data
def get_weekcard_f4():
    return {
        "factory_no":4,
        "result":"sifencshuju"
    }

#-----------------mold_status
def mold_status_f1(body):

    url = "http://10.3.10.61:18080/WebLhmjxk/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    response = requests.post(url=url, headers=headers, json=body)
    data = response.json().get('Object')
    return data
def mold_status_f2(body):
    url = "http://10.3.10.62:18080/WebLhmjxk/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    response = requests.post(url=url, headers=headers, json=body)
    data = response.json().get('Object')
    return data
def mold_status_f3pcr(body):
    url = "http://10.3.10.64:18080/WebLhmjxk/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    response = requests.post(url=url, headers=headers, json=body)
    data = response.json().get('Object')
    return data
def mold_status_f3tbr(body):

    url = "http://10.3.10.64:18081/WebLhmjxk/Frm_iQuery"
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    response = requests.post(url=url, headers=headers, json=body)
    data = response.json().get('Object')
    return data
def mold_status_f4():
    return {
        "factory_no":4,
        "result":"sifencshuju"
    }

#-----------------
def post_stop_status(url, body):
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }

    response = requests.post(url=url, headers=headers, json=body)
    data = response.json().get('Object')
    return data


def stop_status_f1_detail(body):
    return  post_stop_status("http://10.3.10.61:18080/Weblhtjtj/Frm_iQuery", body)


def stop_status_f1_summary(body):
    return post_stop_status("http://10.3.10.61:18080/Weblhtjtj/Frm_ziQuery", body)


def stop_status_f1_machine(body):
    return post_stop_status("http://10.3.10.61:18080/Weblhtjtj/findLhbListjt", body)


def stop_status_f1_shift(body):
    return post_stop_status("http://10.3.10.61:18080/Weblhtjtj/findLhbListbz", body)


def stop_status_f2_detail(body):
    return post_stop_status("http://10.3.10.62:18080/Weblhtjtj/Frm_iQuery", body)


def stop_status_f2_summary(body):
    return post_stop_status("http://10.3.10.62:18080/Weblhtjtj/Frm_ziQuery", body)


def stop_status_f2_machine(body):
    return post_stop_status("http://10.3.10.62:18080/Weblhtjtj/findLhbListjt", body)


def stop_status_f2_shift(body):
    return post_stop_status("http://10.3.10.62:18080/Weblhtjtj/findLhbListbz", body)


def stop_status_f3pcr_detail(body):
    return post_stop_status("http://10.3.10.64:18080/Weblhtjtj/Frm_iQuery", body)


def stop_status_f3pcr_summary(body):
    return post_stop_status("http://10.3.10.64:18080/Weblhtjtj/Frm_ziQuery", body)


def stop_status_f3pcr_machine(body):
    return post_stop_status("http://10.3.10.64:18080/Weblhtjtj/findLhbListjt", body)


def stop_status_f3pcr_shift(body):
    return post_stop_status("http://10.3.10.64:18080/Weblhtjtj/findLhbListbz", body)


def stop_status_f3tbr_detail(body):
    return post_stop_status("http://10.3.10.64:18081/Weblhtjtj/Frm_iQuery", body)


def stop_status_f3tbr_summary(body):
    return post_stop_status("http://10.3.10.64:18081/Weblhtjtj/Frm_ziQuery", body)


def stop_status_f3tbr_machine(body):
    return post_stop_status("http://10.3.10.64:18081/Weblhtjtj/findLhbListjt", body)


def stop_status_f3tbr_shift(body):
    return post_stop_status("http://10.3.10.64:18081/Weblhtjtj/findLhbListbz", body)


def stop_status_f4_detail(body):
    return post_stop_status("F4_DETAIL_URL", body)


def stop_status_f4_summary(body):
    return post_stop_status("F4_SUMMARY_URL", body)


def stop_status_f4_machine(body):
    return post_stop_status("F4_MACHINE_URL", body)


def stop_status_f4_shift(body):
    return post_stop_status("F4_shift_URL", body)














#-----------------
def stop_report_f1():
    return {
        "factory_no":1,
        "result":"yifencshuju"

    }
def stop_report_f2():
    return {
        "factory_no":2,
        "result":"erfencshuju"
    }
def stop_report_f3pcr():
    return {
        "factory_no":31,
        "result":"sanpcrfencshuju"
    }
def stop_report_f3tbr():


    return {
        "factory_no":32,
        "result":"santbrfencshuju"
    }
def stop_report_f4():
    return {
        "factory_no":4,
        "result":"sifencshuju"
    }

if __name__ == "__main__":
    get_specification_f2()

