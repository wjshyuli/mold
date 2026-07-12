<template>
	
  <el-table
    :data="tableData"
    style="width:100%"
  >
  

  
  
  
  
    <el-table-column
      prop="gc"
      label="工厂"
    />
	<el-table-column
	  prop="sbid"
	  label="机台"
	/>
	<el-table-column
	  prop="tjyyz"
	  label="停机原因"
	/>
	<el-table-column
	  prop="tjfz"
	  label="停机分钟"
	/>

    <el-table-column
      prop="tjtj"
      label="统计分钟"
    />
	
	<el-table-column
	  prop="tjbl"
	  label="停机比率"
	/>
	<el-table-column
	  prop="bz"
	  label="班组"
	/>
	<el-table-column
	  prop="bc"
	  label="班次"
	/>
	<el-table-column
	  prop="createdate"
	  label="开始时间"
	/>	
	<el-table-column
	  prop="enddate"
	  label="结束时间"
	/>	
	<el-table-column
	  prop="gzrq"
	  label="工作日期"
	/>
	<el-table-column
	  prop="userid"
	  label="操作人"
	/>
	
	
	
  </el-table>

</template>

<script setup lang="ts">
import { ref } from "vue"
import { getStopStatus } from "@/api/mold"
import { ElMessage } from "element-plus"

const tableData = ref<any[]>([])

const fetchData = async (body:any) => {

    try{
	
		console.log(body)
        const res = await getStopStatus(body)


        tableData.value = res.data

    }catch(error){

        ElMessage.error("网络异常")


		

    }

}

defineExpose({
    fetchData
})
</script>
