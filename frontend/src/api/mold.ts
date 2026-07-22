import request from "@/utils/request"


// ------硫化机规格-------
// 查询
export function getSpecification(factory:Number	) {

    return request.get("api/specification",{
		params:{factory}
	})

}
export function export_Specification(body:any){
	return request.post('/fastapi/export_specification',body,  {
      responseType: "blob",
    })
}


//-----weekcard 周转卡
export function WeekCard(body:any){
	return request.post("api/weekcard",body)
}

export function export_WeekCard(body: any) {
    return request.post(
        "/fastapi/export_weekcard",
        body,
        {
            responseType: "blob"
        }
    )
}

//-----模具现状
export function getMoldStatus(body:any){
	return request.post("api/mold_status",body)
}

export function export_MoldStatus(){
	return true
}

//------停机状态 Django
export function getStopStatus(body:any){
	return request.post("api/stop_status",body)
}
//-------fastapi
export function export_StopStatus_detail(body:any){
	return request.post("/fastapi/export_stopstatus_detail",body,  {
      responseType: "blob",
    })
}
export function export_StopStatus_summary(body:any){
	return request.post('/fastapi/export_stopstatus_summary',body,  {
      responseType: "blob",
    })
}
export function export_StopStatus_shift(body:any){
	return request.post('/fastapi/export_stopstatus_shift',body,  {
      responseType: "blob",
    })
}
export function export_StopStatus_machine(body:any){
	return request.post('/fastapi/export_stopstatus_machine',body,  {
      responseType: "blob",
    })
}
