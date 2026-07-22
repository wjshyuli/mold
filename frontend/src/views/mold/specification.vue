<template>

  <!-- 页面标题 -->
  <div class="page-header">
	<div class="toolbar">
		<h2>硫化机规格设置</h2>
		<el-button
		  type="primary"
		  @click="fetchData"
		>
		  刷新
		</el-button>
		
	</div>
    
	

    <div class="toolbar">



      <el-button
        type="success"
		@click="exportExcel"
      >
        导出 Excel
      </el-button>

    </div>

  </div>

  <!-- 表格 -->

  <el-table
    :data="tableData"
	v-loading="loading"
    border
    stripe
    style="width:100%"
	height="750"
  >

    <el-table-column
      prop="departmentName"
      label="部门名称"
	  width="90"
      
    />

	<el-table-column
      prop="sbid"
      label="设备"
	  width="80"
    />

	<el-table-column label="硫化机状态" width="130">
	  <template #default="{ row }">
		<div
		  :style="{
			backgroundColor: row.color,
			color: '#000',
			textAlign: 'center',
			borderRadius: '4px',
			padding: '4px 0',
			width:'100px'
		  }"
		>
		  {{ row.bz }}
		</div>
	  </template>
	  
	</el-table-column>

<!-- 	<el-table-column
      prop="lhjlxzt"
      label="硫化断网情况"
    /> -->
	<el-table-column
	  prop="dso"
	  label="类型"
	  width="80"
	/>
	<el-table-column
	  prop="mjbh"
	  label="模号"
	  width="60"
	/>
	<el-table-column
	  prop="jnbh"
	  label="胶囊编号"
	  width="100"
	/>
	<el-table-column
      prop="ddh"
      label="订单号"
	  width="140"
    />
	<el-table-column
      prop="wlmc"
      label="物料名称"
	  width="480"
	  show-overflow-tooltip
    />
<!-- 	<el-table-column
      prop="bc_code"
      label="硫化中条码"
    /> -->
	<el-table-column
      prop="dot"
      label="周期牌"
    />
	<el-table-column
      prop="dqjtcl"
      label="连续生产总量(PLC)"
    />
	<el-table-column
      prop="jnjs"
      label="胶囊计数(PLC)"
    />
	<el-table-column
      prop="hqdsmpd"
      label="模具类型(PLC)"
    />
	<el-table-column
      prop="sl"
      label="计划数"
    />
	<el-table-column
      prop="ys"
      label="计数剩余数量"
    />
	
	
	







  </el-table>

</template>

<script setup lang="ts">
import { ref, watch} from "vue"
import { downloadBlob } from "@/utils/download"

import { getSpecification, export_Specification } from "@/api/mold"
import { ElMessage } from "element-plus"


import { useFactoryStore } from "@/stores/factory"
import { storeToRefs } from "pinia"

const factoryStore = useFactoryStore()
const { factory } = storeToRefs(factoryStore)



const loading = ref(false)
const tableData = ref<any[]>([])



// ----------
import { ElLoading } from "element-plus"
const exportExcel = async() => {

	
	const loading = ElLoading.service({
	    lock: true,
	    text: "文件正在生成，请稍候……",
	    background: "rgba(0,0,0,0.5)"
	  })
	console.log("开始导出")
	
	try {
	  console.log("开始请求后端")
	
	
	const res = await export_Specification({})
	downloadBlob(res.data, "specification.xlsx")
	
	  console.log("下载完成")
	} catch (e) {
	  console.error(e)
	  ElMessage.error("导出失败")
	} finally {
	  console.log("finally")
	
	  
	loading.close()
	}
	
	
	
	
	
	
}




//--------------
const fetchData = async () => {

    loading.value = true

    try {

        const res = await getSpecification(factory.value)
		console.log('这是几分厂：   '+factory.value)
		

        
            tableData.value = res.data
			console.log("请求成功",tableData.value[0])
    

    } catch (error) {

        ElMessage.error("网络异常，请稍后重试")
		console.log(error)

    } finally {

        loading.value = false

    }

}



//-------

watch(factory, fetchData, {
    immediate: true
})

//---------

</script>

<style scoped>

.page-header{

  display:flex;

  justify-content:space-between;

  align-items:center;

  margin-bottom:18px;

}

.page-header h2{

  margin:0;

}

.toolbar{

  display:flex;

  gap:10px;

}

:deep(.el-table .cell) {
  white-space: nowrap;      /* 不换行 */
  overflow: hidden;         /* 超出隐藏 */
  text-overflow: ellipsis;  /* 显示 ... */
}
</style>