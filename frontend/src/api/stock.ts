import request from "@/utils/request"


// 获取库存基础数据
export function getStockBase(){

    return request.get("api/stock_base/")

}


export function addStockBase(data:any){

    return request.post(
        "api/stock_base/",
        data
    )

}


export function deleteStockBase(id:number){

    return request.delete(
        `api/stock_base/${id}/`
    )

}

export function updateStockBase(id:number,body:any){

    return request.put(
        `api/stock_base/${id}/`,
		body
    )

}





// 获取库存基础数据-------------------------
export function getStockCor(){

    return request.get("api/stock_Cor/")

}


export function addStockCor(data:any){

    return request.post(
        "api/stock_Cor/",
        data
    )

}


export function deleteStockCor(id:number){

    return request.delete(
        `api/stock_Cor/${id}/`
    )

}

export function updateStockCor(id:number,body:any){

    return request.put(
        `api/stock_Cor/${id}/`,
		body
    )

}

// ----库存展示-----

export function showStock(body:any){
	return request.post(
	"api/stock_show/",
	body
	)
}