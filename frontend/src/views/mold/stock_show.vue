<template>

  <!-- 页面标题 -->
    <div class="toolbar">
		<h2>各分厂胶囊夹盘用量展示</h2>
	</div>
 


  <!-- 左右布局 -->

<div class="content">

    <!-- 左边 -->

    <div class="table-box">

		<h3>1分厂用量</h3>

		<el-table
			:data="tableData1"
			border
			stripe
			height="700"
			>

			<el-table-column
			  prop="capsule"
			  label="胶囊"
			/>
			<el-table-column
			  prop="quantity1"
			  label="胶囊数" 
			/>
			<el-table-column
			  prop="clamp"
			  label="夹盘" 
			/>
			<el-table-column
			  prop="quantity2"
			  label="夹盘数"
			/>
			

		</el-table>

    </div>

    <!-- 右边 -->

    <div class="table-box">

		<h3>2分厂用量</h3>

		<el-table
			:data="tableData2"
			border
			stripe
			height="700"
			>

			<el-table-column
			  prop="capsule"
			  label="胶囊"
			/>
			<el-table-column
			  prop="quantity1"
			  label="胶囊数" 
			/>
			<el-table-column
			  prop="clamp"
			  label="夹盘" 
			/>
			<el-table-column
			  prop="quantity2"
			  label="夹盘数"
			/>
			

		</el-table>

    </div>

    <div class="table-box">

		<h3>3PCR分厂用量</h3>

		<el-table
			:data="tableData30"
			border
			stripe
			height="700"
			>

			<el-table-column
			  prop="capsule"
			  label="胶囊"
			/>
			<el-table-column
			  prop="quantity1"
			  label="胶囊数" 
			/>
			<el-table-column
			  prop="clamp"
			  label="夹盘" 
			/>
			<el-table-column
			  prop="quantity2"
			  label="夹盘数"
			/>
			

		</el-table>

    </div>
 <div class="table-box">
 
 	<h3>3TBR分厂用量</h3>
 
 	<el-table
 		:data="tableData31"
 		border
 		stripe
 		height="700"
 		>
 
 		<el-table-column
 		  prop="capsule"
 		  label="胶囊"
 		/>
 		<el-table-column
 		  prop="quantity1"
 		  label="胶囊数" 
 		/>
 		<el-table-column
 		  prop="clamp"
 		  label="夹盘" 
 		/>
 		<el-table-column
 		  prop="quantity2"
 		  label="夹盘数"
 		/>
 		
 
 	</el-table>
 
 </div>
 



	
			


</div>
  


</template>



<script setup lang="ts">
import { ref, onMounted } from "vue"
import { ElMessage } from "element-plus"
import { showStock } from "@/api/stock"

const tableData1 = ref<any[]>([])
const tableData2 = ref<any[]>([])
const tableData30 = ref<any[]>([])
const tableData31 = ref<any[]>([])

const fetchData = async () => {
    try {
        tableData1.value = (await showStock({ factory: "1" })).data

        tableData2.value = (await showStock({ factory: "2" })).data

        tableData30.value = (await showStock({ factory: "30" })).data

        tableData31.value = (await showStock({ factory: "31" })).data

    } catch (error) {
        console.log(error)
        ElMessage.error("获取数据失败")
    }
}

onMounted(() => {
    fetchData()
})
</script>








<style scoped>

.toolbar {
    margin-bottom: 20px;
}

.content {
    display: flex;
    gap: 2px;          /* 四张表之间的间距 */
    width: 100%;
}

.table-box {
    flex: 1;            /* 四个平均分宽度 */
    min-width: 0;       /* 非常重要，防止 el-table 撑开 */
}

.table-box h3 {
    text-align: center;
    margin-bottom: 10px;
}

</style>