import request from "@/utils/request"


// ------硫化机规格-------
// 查询
export function getSpecification(factory:Number	) {

    return request.get("/mold/specification",{
		params:{factory}
	})

}

//-----weekcard 周转卡
export function WeekCard(body:any){
	return request.post("/mold/weekcard",body)
}

// 新增
export function getStockBase(){

    return request.post("/stock/stockbase")

}

// 修改
export function updateSpecification(id:number,data:any){

    return request.put(`/mold/a/${id}`,data)

}

// 删除
export function deleteSpecification(id:number){

    return request.delete(`/mold/a/${id}`)

}


//-----模具现状
export function getMoldStatus(body:any){
	return request.post("/mold/mold_status",body)
}

export function getStopStatus(body:any){
	return request.post("/mold/stop_status",body)
}