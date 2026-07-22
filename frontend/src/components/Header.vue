<template>
		
		<div class="headerr" style="color: black;">
<!-- 			<div class="logo">
				
			</div> -->
			
			
			<el-radio-group v-model="factory" class="factory-group">
			  <el-radio-button :value="1">
			    一分厂
			  </el-radio-button>
			
			  <el-radio-button :value="2">
			    二分厂
			  </el-radio-button>
			
			  <el-radio-button :value="30">
			    三分厂PCR
			  </el-radio-button>
			
			  <el-radio-button :value="31">
			    三分厂TBR
			  </el-radio-button>
			</el-radio-group>
			
			
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


<style >
.headerr {
  height: 60px;

  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: 0 20px;


  background: white; 
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
