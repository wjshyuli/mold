import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from "@/stores/user"

import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Specification from '../views/mold/specification.vue'
import WeekcardChange from '../views/mold/weekcard_change.vue'
import MoldStatus from '../views/mold/mold_status.vue'
import StopStatus from '../views/mold/stop_status.vue'
import GoF4 from '../views/mold/goF4.vue'
import StockBase from '../views/mold/stock_base.vue'
import StockCorrespondence from '../views/mold/stock_correspondence.vue'
import StockShow from '../views/mold/stock_show.vue'




const router = createRouter({

  history: createWebHistory(),

  routes: [

    {
      path: '/',
      name: 'home',
      component: Home,
      meta:{
        requiresAuth:true
      }
    },


    {
      path: '/login',
      name: 'login',
      component: Login
    },


    {
      path: '/mold/specification',
      name:'specification',
      component: Specification,
      meta:{
        requiresAuth:true
      }
    },


    {
      path: '/mold/weekcard_change',
      name:'weekcard_change',
      component: WeekcardChange,
      meta:{
        requiresAuth:true
      }
    },


    {
      path: '/mold/mold_status',
      name:'mold_status',
      component: MoldStatus,
      meta:{
        requiresAuth:true
      }
    },


    {
      path: '/mold/stop_status',
      name:'stop_status',
      component: StopStatus,
      meta:{
        requiresAuth:true
      }
    },


    {
      path: '/mold/goF4',
      name:'goF4',
      component: GoF4,
      meta:{
        requiresAuth:true
      }
    },


    {
      path: '/mold/stock_base',
      name:'stock_base',
      component: StockBase,
      meta:{
        requiresAuth:true
      }
    },


    {
      path: '/mold/stock_correspondence',
      name:'stock_correspondence',
      component: StockCorrespondence,
      meta:{
        requiresAuth:true
      }
    },


    {
      path: '/mold/stock_show',
      name:'stock_show',
      component: StockShow,
      meta:{
        requiresAuth:true
      }
    },


  ]

})




// 全局路由守卫
router.beforeEach(async (to) => {

    const userStore = useUserStore()

    // 登录页
    if (to.path === "/login") {

        if (userStore.isLogin) {
            return "/"
        }

        return true
    }

    // 不需要登录验证
    if (!to.meta.requiresAuth) {
        return true
    }

    // Pinia 已经有用户信息
    if (userStore.isLogin) {
        return true
    }

    // 请求后端，根据 Session 判断是否登录
    const success = await userStore.getUser()

    if (success) {
        return true
    }

    return "/login"
})


export default router