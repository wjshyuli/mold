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
	import { storeToRefs } from "pinia"
	import { watch,ref} from "vue"
	import { WeekCard,export_WeekCard } from "@/api/mold"
	import { ElMessage } from "element-plus"
	
	import { downloadBlob } from "@/utils/download"
	  
	const factory_store =useFactoryStore()
	const {factory} =storeToRefs(factory_store)
	
	
	const loading = ref(false)
	const tableData = ref<any[]>([])
	
	
	const timeRange = ref<any[]>([])
	
	const formatDate = (date: Date) => {
	    const pad = (n: number) => String(n).padStart(2, "0")
	
	    return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())} ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`
	}

	  
	  // 时间范围
	  const get_body =()=> ({
	  	 factory: factory_store.factory,
	  	 st: timeRange.value[0],
	  	 et: timeRange.value[1],
	   })


	
  
	const fetchData = async () => {
		
		
		if(!timeRange.value||timeRange.value.length !== 2  ){
		        ElMessage.warning("请选择时间范围")
		        return
		    }

		loading.value=true
	 
		const body = get_body()
		
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
		
	}
  
	const refresh = async()=>{
	
	    initTimeRange()
	
	    await fetchData()
	
	}
	

	  

  
  
	watch(
	factory ,
	async ()=>{
		
		initTimeRange()
		await fetchData()
		ElMessage.success("分厂数据展示成功")
		},
	    {immediate: true}
	)
  
  
 import { ElLoading } from "element-plus" 
	const exportExcel = async () => {
		const loading = ElLoading.service({
		    lock: true,
		    text: "文件正在生成，请稍候……",
		    background: "rgba(0,0,0,0.5)"
		  })
		console.log("开始导出")
		try {
		  const body =get_body()
		  const res = await export_WeekCard(body)
		  downloadBlob(res.data, "weekcard.xlsx")
		  console.log("下载完成")
		} catch (e) {
		  console.error(e)
		  ElMessage.error("导出失败")
		} finally {
		  console.log("finally")
		
		  
		loading.close()
		}
		
		
		
		
		
		
		
		
		
		
		
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
  