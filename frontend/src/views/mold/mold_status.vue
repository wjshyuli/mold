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
	import { ref } from "vue"
	import { onMounted } from "vue"
	import { getMoldStatus } from "@/api/mold"
	import { ElMessage } from "element-plus"
	
	  
	const factory_store =useFactoryStore()
	
	
	const loading = ref(false)
	  
	const tableData = ref<any[]>([])
	

	  


	
  
	const fetchData = async () => {
		
		
		

		loading.value=true
		console.log('fac'+factory_store.factory);
	 
		const body = {
			 "factory": factory_store.factory,

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

	  
	onMounted(() => {
	  
	
	  
	  })
  
  
  
import * as XLSX from "xlsx"	
import { saveAs } from "file-saver"
const exportExcel = () => {
	
  const exportData = tableData.value.map(item => ({
    "部门名称": factory_store.factory,
	"工厂":item.aa
	

  }))
  
 console.log(tableData.value)
 console.log(factory_store.factory)
 
 


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