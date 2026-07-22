import requests
import pandas as pd
from datetime import datetime


def get_specification(url):
    res=requests.post(url).json().get("Object")
    df=pd.DataFrame(res)
    df_res=pd.DataFrame()
    df_res["部门名称"]=df["departmentName"]
    df_res["设备"]=df["sbid"]
    df_res["硫化机状态"]=df["bz"]
    df_res["类型"]=df["dso"]
    df_res["模号"]=df["mjbh"]
    df_res["胶囊编号"]=df["jnbh"]
    df_res["订单号"]=df["ddh"]
    df_res["物料名称"]=df["wlmc"]
    df_res["周期牌"]=df["dot"]
    df_res["连续生产总量(PLC)"]=df["dqjtcl"]
    df_res["胶囊计数(PLC)"]=df["jnjs"]
    df_res["模具类型(PLC)"]=df["hqdsmpd"]
    df_res["计划数"]=df["sl"]
    df_res["计数剩余数量"]=df["ys"]
    return df_res

def get_weekcard(url,st,et,factory):
    body={
        "startDate": st.strftime("%Y-%m-%d %H:%M:%S"), 
        "endDate": et.strftime("%Y-%m-%d %H:%M:%S")
    }
    print(body)


    res=requests.post(url,json=body)
    result=res.json().get("Object")
    print('weekcard_通了')
    print(res.status_code)
    
    df=pd.DataFrame(result)
    
    df_res=pd.DataFrame()

    df_res["机台"]=df["Sbid"]
    df_res["类型"]=df["Types"]
    df_res["工号"]=df["CreateUserid"]
    df_res["操作人"]=df["CreateName"]
    df_res["操作时间"]=df["CreateDate"]

    df_res["工厂"]=str(factory)
  
    return df_res

def get_moldstatus(url):
    
    
    res=requests.post(url,json={})
    result=res.json().get("Object")
    
    
    df=pd.DataFrame(result)
    df_res=pd.DataFrame()
    
    df_res["工厂"]=df["Gc"]
    df_res["机台"]=df["Jt"]
    df_res["规格左"]=df["Ggz"]
    df_res["规格右"]=df["Ggy"]
    df_res["模具左编号"]=df["Mjzbh"]
    df_res["左模具条数"]=df["Lts"]
    df_res["模具左交替时间"]=df["Mjzjtsj"]
    df_res["模具右编号"]=df["Mjybh"]
    df_res["右模具条数"]=df["Rts"]
    df_res["模具右交替时间"]=df["Mjyjtsj"]
    
    if url == 'http://10.3.10.62:18080/WebLhmjxk/Frm_iQuery':
        df_res["工厂"]='二分厂'
  
    return df_res


#------------------


def get_stopstatus_detail(url,st,et):

    
    body={
        "k_date": st.strftime("%Y-%m-%d %H:%M:%S"), 
        "e_date": et.strftime("%Y-%m-%d %H:%M:%S")
    }
    res=requests.post(url,json=body)
    result=res.json().get("Object")
    print('stopstatus_detail通了')
    print(res.status_code)
    df=pd.DataFrame(result)
    df_res=pd.DataFrame()
    df_res["工厂"]=df["gc"]
    df_res["机台"]=df["sbid"]
    df_res["停机原因"]=df["tjyyz"]
    df_res["停机分钟"]=df["tjfz"]
    df_res["统计分钟"]=df["tjtj"]
    df_res["停机比率"]=df["tjbl"]
    df_res["班组"]=df["bz"]
    df_res["班次"]=df["bc"]
    df_res["开始时间"]=df["createdate"]
    df_res["结束时间"]=df["enddate"]
    df_res["工作日期"]=df["gzrq"]
    df_res["操作人"]=df["userid"]
  
  
    return df_res
   

def get_stopstatus_shift(url,st,et):
    body={
        "k_date": st.strftime("%Y-%m-%d %H:%M:%S"), 
        "e_date": et.strftime("%Y-%m-%d %H:%M:%S")
    }

    res=requests.post(url,json=body)
    result=res.json().get("Object")
    print('stopstatus_shift通了')
    print(res.status_code)
    df=pd.DataFrame(result)
    df_res=pd.DataFrame()
    df_res["工厂"]=df["gc"]
    df_res["机台"]=df["sbid"]
    df_res["班组"]=df["bz"]
    df_res["停机分钟"]=df["tjfz"]
    df_res["统计分钟"]=df["tjtj"]
    df_res["停机比率"]=df["tjbl"]

  
  
    return df_res
   
def get_stopstatus_summary(url,st,et,factory):
    body={
        "k_date": st.strftime("%Y-%m-%d %H:%M:%S"), 
        "e_date": et.strftime("%Y-%m-%d %H:%M:%S")
    }

    res=requests.post(url,json=body)
    result=res.json().get("Object")
    print('stopstatus_summary通了')
    print(res.status_code)
    df=pd.DataFrame(result)
    df_res=pd.DataFrame()
    df_res["停机原因"]=df["tjyyz"]
    df_res["停机分钟"]=df["tjfz"]
    df_res["统计分钟"]=df["tjtj"]
    df_res["停机比率"]=df["tjbl"]
    df_res["分厂"]=factory

  
  
    return df_res
   


def get_stopstatus_machine(url,st,et):
    body={
        "k_date": st.strftime("%Y-%m-%d %H:%M:%S"), 
        "e_date": et.strftime("%Y-%m-%d %H:%M:%S")
    }

    
    res=requests.post(url,json=body)
    
    result=res.json().get("Object")
    print('stopstatus_machine通了')
    print(res.status_code)
    df=pd.DataFrame(result)
    df_res=pd.DataFrame()
    df_res["工厂"]=df["gc"]
    df_res["机台"]=df["sbid"]
    df_res["停机分钟"]=df["tjfz"]
    df_res["统计分钟"]=df["tjtj"]
    df_res["停机比率"]=df["tjbl"]
 
    
  
    return df_res
   








if __name__ == "__main__":


    st = datetime.fromisoformat(
    "2026-07-12T09:15:04.156+00:00"
)

    et = datetime.fromisoformat(
    "2026-07-14T09:15:04.156+00:00"
)
    df3=get_weekcard(" http://10.3.10.61:18080/Webjtzqhghjl/Frm_iQuery",st,et)
    

