<template>
	<div class="top">
		<div class="topleft" >
			<h2 style="border: ;">周期牌更换记录</h2>
		
			<el-date-picker
			v-model="timeRange"
			type="datetimerange"
			range-separator="至"
			start-placeholder="开始时间"
			end-placeholder="结束时间"
			value-format="YYYY-MM-DD HH:mm:ss"
			
			
			/>
			</div>
		<div class="topright">
			<el-button
			  type="primary"
			  @click="fetchData"
			>
			  查询
			</el-button>
			<el-button
			  type="primary"
			  @click="refresh"
			>
			  刷新
			</el-button>
			<el-button
			  type="success"
			  @click="exportExcel"
			>
			  导出Excel
			</el-button>
		</div>
	</div>


<el-table
    :data="tableData"
    border
    stripe
    style="width:100%"
	height="750"
	
	
  >

    <el-table-column
      prop="Sbid"
      label="机台"
	  width="120"
      
    />

	<el-table-column
      prop="Types"
      label="类型"
	  width="120"
    />
	<el-table-column
	  prop="Zqp"
	  label="周期号"
	  width="120"
	/>
	<el-table-column
	  prop="CreateUserid"
	  label="操作人"
	  width="180"
	/>
	<el-table-column
	  prop="CreateDate"
	  label="操作时间"
	  width="180"
	/>




</el-table>


</template>
  
  
  
  
  <script setup lang="ts">
	import { useFactoryStore } from "@/stores/factory"
	import { ref } from "vue"
	import { onMounted } from "vue"
	import { WeekCard } from "@/api/mold"
	import { ElMessage } from "element-plus"
	
	  
	const factory_store =useFactoryStore()
	console.log(factory_store.factory)
	
	const loading = ref(false)
	  
	const tableData = ref<any[]>([])
	
	
	const timeRange = ref<any[]>([])
	const formatDate = (date: Date) => {
	    const pad = (n: number) => String(n).padStart(2, "0")
	
	    return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())} ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`
	}

	  
	  // 时间范围


	
  
	const fetchData = async () => {
		console.log(timeRange.value)
		
		if(!timeRange.value||timeRange.value.length !== 2  ){
		        ElMessage.warning("请选择时间范围")
		        return
		    }

		loading.value=true
	 
		const body = {
			 factory: factory_store.factory,
			 st: timeRange.value[0],
			 et: timeRange.value[1],
		 }
		console.log(body)
		try{
			const res=await WeekCard(body)
			tableData.value = res.data
		}
		catch (error) {
		
			ElMessage.error("网络异常，请稍后重试")
			console.log(error)
		
		} finally {
			loading.value = false
		}
		
		 
	 } 
  
	const exportExcl =() =>{}
  
  
	const initTimeRange = () => {
	
	    const today = new Date()
	
	    // 今天07:00
	    const end = new Date(today)
	    end.setHours(7, 0, 0, 0)
	
	    // 昨天07:00
	    const start = new Date(end)
	    start.setDate(start.getDate() - 1)
	
	    timeRange.value = [
	        formatDate(start),
			formatDate(end)
			
	        
	    ]
		console.log('我要输出时间了')
		console.log(timeRange.value)
	}
  
	const refresh = async()=>{
	
	    initTimeRange()
	
	    await fetchData()
	
	}
	

	  
	onMounted(() => {
	  
		  initTimeRange()
	  
	  })
  
  
  
import * as XLSX from "xlsx"	
import { saveAs } from "file-saver"
const exportExcel = () => {
	
  const exportData = tableData.value.map(item => ({
    "部门名称": factory_store.factory,
	
    "机台": item.Sbid,
    
    "类型": item.Types,

    "周期牌": item.Zqp,

    "操作人": item.CreateUserid,
    "操作时间": item.CreateDate,
  }))
  
 console.log(tableData.value)
 console.log(factory_store.factory)
 
 
	tableData.value.forEach(item => {
	console.log('yifen shuju ');
	  console.log(item)
	})

  // 1. 把 JSON 转成 sheet
  const worksheet = XLSX.utils.json_to_sheet(exportData)

  // 2. 创建 workbook
  const workbook = XLSX.utils.book_new()

  // 3. 把 sheet 放进 workbook
  XLSX.utils.book_append_sheet(workbook, worksheet, "周期牌")

  // 4. 生成二进制
  const excelBuffer = XLSX.write(workbook, {
    bookType: "xlsx",
    type: "array"
  })

  // 5. 生成 Blob
  const blob = new Blob([excelBuffer], {
    type: "application/octet-stream"
  })

  // 6. 下载
  saveAs(blob, "周期牌.xlsx")
}

  
  </script>
  
  
  
  
  
  
  
  
  
  
  
  
  <style >
	  .topleft{
		  display: flex;
		  justify-content: space-between;
		  width: 700px;
		  align-items: center;
		  gap: 20px;
	  }
	  .top,.topright{
		  display: flex;
		  align-items: center;
		  gap: 20px;
	  }
	  
  </style>
  