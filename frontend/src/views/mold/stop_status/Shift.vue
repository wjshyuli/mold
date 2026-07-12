<template>
	
  <el-table
    :data="tableData"
    border
    stripe
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
	  prop="bz"
	  label="班组"
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
