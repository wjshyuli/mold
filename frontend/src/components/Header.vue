<template>
		
		<div class="headerr" style="color: black;">
<!-- 			<div class="logo">
				
			</div> -->
			
			<div class="toolbar">
				<span>分厂：</span>
				
				<el-select v-model= "factory" style="width: 150px;">
					<el-option label="一分厂" :value="1"></el-option>
					<el-option label="二分厂" :value="2"></el-option>
					<el-option label="三分厂PCR" :value="30"></el-option>
					<el-option label="三分厂TBR" :value="31"></el-option>

				</el-select>
				


				
				

				
			</div>
			
			
<!-- 			<div class="download">
				<el-button type="primary">
					导出Excle
				</el-button>
			</div -->
			
			
			<div class="user">
				<el-icon :size="18">
				  <Bell />
				</el-icon>
				
				
				admin
			</div>
			
			
		</div>









</template>


<script setup lang="ts">
	
	import {
	  Fold,
	  Bell,
	  User,
	} from '@element-plus/icons-vue'
	

	

	import { useFactoryStore } from '@/stores/factory'
	import { storeToRefs } from 'pinia'
	
	const factoryStore = useFactoryStore()
	const { factory } = storeToRefs(factoryStore)
	
	
	
	

	
	
	
</script>


<style scoped>
.headerr {
  height: 60px;

  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: 0 20px;


  background: white; 
}

.logo {
  min-width: 120px;
}

.toolbar {
  display: flex;
  align-items: center;
  
  gap: 12px;

  flex: 1;
  margin-left: 20px;
  
}
.download{
	margin-right: 90px;
}

.user {
  display: flex;
  align-items: center;
  gap: 8px;

  cursor: pointer;
  color: #606266;
}

.user:hover {
  color: #409EFF;
}
</style>
