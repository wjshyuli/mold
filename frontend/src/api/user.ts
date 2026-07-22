// 用户名
// 权限
// Token

import request from "@/utils/request"

export function login(body: any) {
    return request.post("api/login/", body)
}


export function csrf() {
    return request.get("api/csrf/")
}

export function me() {
    return request.get("api/me/")
}