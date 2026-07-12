<template>
	
	
	<div class="top">
		<div class="topleft" >
			<h2 style="border: ;">硫化停机报表</h2>
		
			<el-date-picker
			v-model="aaa"
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
			  @click=""
			>
			  查询
			</el-button>
			<el-button
			  type="primary"
			  @click=""
			>
			  刷新
			</el-button>
			<el-button
			  type="success"
			  @click=""
			>
			  导出
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

  	import { ref } from "vue"
  	import { onMounted } from "vue"
  	
  	import { ElMessage } from "element-plus"

  	

  	
  	
  	

  	
  	const tableData = ref<any[]>([])
  	const aaa = ref<any[]>([])

  	
  	
  	const search = () => {

  	}
	
	</script>