<template>
    
	
	<div class="top">
		<div class="topleft" >
			<h2 style="border: ;">硫化模具现状</h2>

		</div>
			
		<div class="topright">
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
			  导出
			</el-button>
		</div>
	</div>
	

<el-table
	v-loading='loading'
    :data="tableData"
	
    border
    stripe
    style="width:100%"
	height="750"
	
	
  >

    <el-table-column
      prop="Gc"
      label="工厂"
	  width="80"
      
    />
    <el-table-column
      prop="Jt"
      label="机台"
	  width="80"
      
    />

	<el-table-column
      prop="Ggz"
      label="规格左"
	  width="430"
    />
	<el-table-column
	  prop="Ggy"
	  label="规格右"
	  width="430"
	/>
	<el-table-column
	  prop="Mjzbh"
	  label="模具左编号"
	  width="80"
	/>
	<el-table-column
	  prop="Lts"
	  label="左模具条数"
	  width="80"
	  
	/>
	<el-table-column
	  prop="Mjzjtsj"
	  label="模具左交替时间"
	  width="150"
	  
	/>
	<el-table-column
	  prop="Mjybh"
	  label="模具右编号"
	  width="80"
	/>
	<el-table-column
	  prop="Mjyjtsj"
	  label="模具右交替时间"
	  width="150"
	  
	/>
	<el-table-column
	  prop="Rts"
	  label="右模具条数"
	  width="80"
	  
	/>




</el-table>

	
	
</template>




  
  <script setup lang="ts">
	import { useFactoryStore } from "@/stores/factory"
	import { storeToRefs } from "pinia"
	import { ref ,watch} from "vue"
	import { downloadBlob } from "@/utils/download"
	
	import { getMoldStatus } from "@/api/mold"
	import { ElMessage } from "element-plus"
	
	  
	const factory_store =useFactoryStore()
	const {factory} = storeToRefs(factory_store)
	
	
	const loading = ref(false)
	const tableData = ref<any[]>([])
	

	  


	
  
	const fetchData = async () => {

		loading.value=true
		console.log('fac'+factory_store.factory);
	 
		const body = {
			 "factory": factory.value,

		 }
		
		try{
			const res=await getMoldStatus(body)
			tableData.value = res.data
		}
		catch (error) {
		
			ElMessage.error("网络异常，请稍后重试")
			console.log(error)
		
		} finally {
			loading.value = false
		}
		
		 
	 } 
  

  
  

	const refresh = async () => {
	  await fetchData()
	  ElMessage.success("刷新成功")
	}

	  
	watch(
	factory,
	async() => {
		await fetchData()
		ElMessage.success("显示分厂数据成功")
	},
	{
		immediate:true		
	}
	)
  
  
  

const exportExcel = async() => {
	
	window.open("/fastapi/export_modlstatus", "_blank")
	
	ElMessage.success("文件下载中✅")
}
	

 


</script>