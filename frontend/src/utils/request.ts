// src/utils/request.ts

import axios from 'axios'

const request = axios.create({
  // Django 地址
  baseURL: '/api/',

  // 超时时间（毫秒）
  timeout: 25000,
})

// 导出
export default request

//相应超时拦截器
// request.interceptors.response.use(

//     response => response,

//     error => {

//         if (error.code === "ECONNABORTED") {

//             ElMessage.error("请求超时")

//         }

//         return Promise.reject(error)
//     }

// )
