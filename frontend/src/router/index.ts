import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'
import Specification from '../views/mold/specification.vue'
import WeekcardChange from '../views/mold/weekcard_change.vue'
import MoldStatus from '../views/mold/mold_status.vue'
import StopStatus from '../views/mold/stop_status.vue'
import StopReport from '../views/mold/stop_report.vue'
import StockBase from '../views/mold/stock_base.vue'
import StockCorrespondence from '../views/mold/stock_correspondence.vue'
import StockShow from '../views/mold/stock_show.vue'



const router = createRouter({
  history: createWebHistory(),

  routes: [
    {
      path: '/',
      component: Home
    },

    {
      path: '/mold/specification',
      component: Specification
    },

    {
      path: '/mold/weekcard_change',
      component: WeekcardChange
    },

    {
      path: '/mold/mold_status',
      component: MoldStatus
    },

    {
      path: '/mold/stop_status',
      component: StopStatus
    },

    {
      path: '/mold/stop_report',
      component: StopReport
    },
	{
	  path: '/mold/stock_base',
	  component: StockBase
	},
	{
	  path: '/mold/stock_correspondence',
	  component: StockCorrespondence
	},
	{
	  path: '/mold/stock_show',
	  component: StockShow
	},
	
  ]
})

export default router