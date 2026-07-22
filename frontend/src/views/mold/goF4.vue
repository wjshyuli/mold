<template>
	
	
<div class="f4">
	<el-button type="primary" plain size="large" @click="gof4">进入四分厂</el-button>
</div>

</template>
  
  
  
  <script setup lang="ts">

  	import { ref } from "vue"
  	import { onMounted } from "vue"
  	
  	
	
	
	const gof4 = async() => {
	   window.open(
		"http://10.3.10.118",
		"_blank"
	  )
	}
  	
  	

  
	
	</script>
	
<style>
	
.f4 {
  display: flex;
  align-items: center;
  justify-content: center;
  
  
  
  height: 75vh;
  
  
}


</style>