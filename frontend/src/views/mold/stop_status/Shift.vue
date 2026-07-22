<template>
	
  <el-table
    :data="tableData"
    border
    stripe
    style="width:100%"
	v-loading="loading"
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
import { getStopStatus ,export_StopStatus_shift} from "@/api/mold"
import { ElMessage } from "element-plus"

const tableData = ref<any[]>([])
const loading = ref(false)

const fetchData = async (body:any) => {

    try{
		loading.value=true
		console.log(body)
        const res = await getStopStatus(body)


        tableData.value = res.data
		loading.value=false

    }catch(error){

        ElMessage.error("网络异常")


		

    }

}

const exportData = async (body:any) => {

    try{
	
        const body1 = {
            st: body.st,
            et: body.et
        }
        
        return await export_StopStatus_shift(body1)

    }catch(error){

        ElMessage.error("网络异常")
    }

}






defineExpose({
    fetchData,exportData
})
</script>
