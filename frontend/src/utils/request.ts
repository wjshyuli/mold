

import axios from 'axios'

const request = axios.create({
  // Django 地址
  baseURL: '/',

  // 超时时间（毫秒）
	timeout: 60000, 
  
      // 允许浏览器携带 Cookie
	withCredentials: true,
  
      // 告诉 Axios CSRF Cookie 和 Header 的名称
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFToken",
})

request.interceptors.request.use(config => {


    const csrfToken = document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken="))
        ?.split("=")[1]


    if(csrfToken){

        config.headers["X-CSRFToken"] = csrfToken

    }


    return config

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
