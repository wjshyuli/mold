from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime,timedelta
import requests
from service import get_specification,get_weekcard,get_moldstatus
from service import get_stopstatus_detail,get_stopstatus_machine,get_stopstatus_shift,get_stopstatus_summary



from io import BytesIO
from fastapi.responses import StreamingResponse
import pandas as pd


app = FastAPI()

url_map={
    "一分厂":"http://10.3.10.61:18080/",
    "二分厂":"http://10.3.10.62:18080/",
    "三分厂PCR":"http://10.3.10.64:18080/",
    "三分厂TBR":"http://10.3.10.64:18081/",
}




class WeekcardRequest(BaseModel):
    st: datetime
    et: datetime
class StopStatus_detail(BaseModel):
    st: datetime
    et: datetime
class StopStatus_shift(BaseModel):
    
    st: datetime
    et: datetime
class StopStatus_summary(BaseModel):
    
    st: datetime
    et: datetime
class StopStatus_machine(BaseModel):
    
    st: datetime
    et: datetime


#-----------Home
@app.get("/")
def read_root():
    return {"message": "欢迎使用 FastAPI 项目！"}

#-----------硫化机规格设置

@app.post("/fastapi/export_specification")
def specification():
        
    try:    
        url_end="WebJtggsz/Frm_iQuery"
        df=pd.DataFrame()


        for k,v in url_map.items():
            url=v+url_end
     
            df2=get_specification(url)
            print(f"获取{k}分厂的数据成功")
            df=pd.concat([df,df2],ignore_index=True)
      
   
 
        output=BytesIO()

        df.to_excel(
            output,
            index=False,       # 不导出DataFrame的索引
            engine="openpyxl"
        )

        output.seek(0)    # 移动指针到开头位置

        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": "attachment; filename=specification.xlsx"
            }
        )

    except Exception as e:
        print(e)
        return {
            "error": str(e)
        }


#----------周转卡--
@app.post("/fastapi/export_weekcard")
def weekcard(req:WeekcardRequest):
        
    try:    
        url_end="Webjtzqhghjl/Frm_iQuery"
        df=pd.DataFrame()

        for k,v in url_map.items():
            url=v+url_end
            
            

            df2=get_weekcard(url,req.st,req.et,factory=k)
            
            print(f"获取{k}分厂的数据成功")
            df=pd.concat([df,df2],ignore_index=True)
        output=BytesIO()
        df.to_excel(
            output,
            index=False,       # 不导出DataFrame的索引
            engine="openpyxl"
        )
        output.seek(0)    # 移动指针到开头位置
        
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": "attachment; filename=weekcard.xlsx"
            }
        )

    except Exception as e:
        return {
            "error真的erroer了": str(e)
        }


#------------模具现状
@app.get("/fastapi/export_modlstatus")
def mold_status():
    print('这是moldstatus')
    
        
    try:    
        url_end="WebLhmjxk/Frm_iQuery"
        df=pd.DataFrame()

        for k,v in url_map.items():
            url=v+url_end
            print(url)
            df2=get_moldstatus(url)
            print(f"获取{k}分厂的数据成功")
            df=pd.concat([df,df2],ignore_index=True)
        output=BytesIO()
        df.to_excel(
            output,
            index=False,       # 不导出DataFrame的索引
            engine="openpyxl"
        )
        output.seek(0)    # 移动指针到开头位置
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": "attachment; filename=mold_status.xlsx"
            }
        )

    except Exception as e:
        return {
            "error": str(e)
        }

#----------停机状态--detail
@app.post("/fastapi/export_stopstatus_detail")
def ss_d(req:StopStatus_detail):
        
    try:    
        url_end="Weblhtjtj/Frm_iQuery"
        df=pd.DataFrame()

        for k,v in url_map.items():
            url=v+url_end
            df2=get_stopstatus_detail(url,req.st,req.et,)
            print(f"获取{k}分厂的数据成功")
            df=pd.concat([df,df2],ignore_index=True)
        output=BytesIO()
        df.to_excel(
            output,
            index=False,       # 不导出DataFrame的索引
            engine="openpyxl"
        )
        output.seek(0)    # 移动指针到开头位置
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": "attachment; filename=stopstatus_detail.xlsx"
            }
        )

    except Exception as e:
        return {
            "error": str(e)
        }


#----------停机状态--machine
@app.post("/fastapi/export_stopstatus_machine")
def ss_m(req:StopStatus_machine):
    
        
    try:    
        url_end="Weblhtjtj/findLhbListjt"
        df=pd.DataFrame()
        
        for k,v in url_map.items():
            url=v+url_end
            print(url)
            df2=get_stopstatus_machine(url,req.st,req.et)
            print(f"获取{k}分厂的数据成功")
            df=pd.concat([df,df2],ignore_index=True)
        output=BytesIO()
        df.to_excel(
            output,
            index=False,       # 不导出DataFrame的索引
            engine="openpyxl"
        )
        output.seek(0)    # 移动指针到开头位置
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": "attachment; filename=stopstatus_machine.xlsx"
            }
        )

    except Exception as e:
        return {
            "error": str(e)
        }


#----------停机状态--shift
@app.post("/fastapi/export_stopstatus_shift")
def ss_s(req:StopStatus_shift):
        
    try:    
        url_end="Weblhtjtj/findLhbListbz"
        df=pd.DataFrame()

        for k,v in url_map.items():
            url=v+url_end
            df2=get_stopstatus_shift(url,req.st,req.et)
            print(f"获取{k}分厂的数据成功")
            df=pd.concat([df,df2],ignore_index=True)
        output=BytesIO()
        df.to_excel(
            output,
            index=False,       # 不导出DataFrame的索引
            engine="openpyxl"
        )
        output.seek(0)    # 移动指针到开头位置
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": "attachment; filename=stopstatus_shift.xlsx"
            }
        )

    except Exception as e:
        return {
            "error": str(e)
        }


#----------停机状态--summary
@app.post("/fastapi/export_stopstatus_summary")
def ss_sum(req:StopStatus_summary):
        
    try:    
        url_end="Weblhtjtj/Frm_ziQuery"
        df=pd.DataFrame()

        for k,v in url_map.items():
            url=v+url_end
            df2=get_stopstatus_summary(url,req.st,req.et,factory=k)
            print(f"获取{k}分厂的数据成功")
            df=pd.concat([df,df2],ignore_index=True)
        output=BytesIO()
        df.to_excel(
            output,
            index=False,       # 不导出DataFrame的索引
            engine="openpyxl"
        )
        output.seek(0)    # 移动指针到开头位置
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": "attachment; filename=stopstatus_summary.xlsx"
            }
        )

    except Exception as e:
        return {
            "error": str(e)
        }






if __name__ == '__main__':
    specification()
