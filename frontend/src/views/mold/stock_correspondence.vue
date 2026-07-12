<template>

  <!-- 页面标题 -->
  

    

    <div class="toolbar">
		<h2>胶囊--夹盘对应关系数据表</h2>
		<div>
		

		<el-button
			type="primary"
			@click="fetchData"
		>
			刷新
		</el-button>
		</div>
      <el-button
        type="success"
        @click="opendialog"
      >
        新增
      </el-button>


    </div>




  <!-- 左右布局 -->

  <div class="content">


    

      

      <el-table
        :data="tableData"
        border
        stripe
        height="700"
      >

        <el-table-column
          prop="specification"
          label="硫化规格"
		  width="280"
        />

        <el-table-column
          prop="capsule"
          label="胶囊型号"
		  width="140"
        />
		<el-table-column
		  prop="clamp"
		  label="夹盘"
		  width="140"
		/>
		
		<el-table-column
		  label="操作"
		  width="240"
		  
		>
		
		<template #default="{row}" >
			<div class="ction-buttons">
			
			<el-button
			  type="success"
			  size="default"
			  @click="editStock(row)"
			>
			  编辑
			</el-button>
				
				
		    <el-button
		      type="danger"
		      size="default"
		      @click="deleteStock(row.id)"
		    >
		      删除
		    </el-button>
			
		
			
			</div>
			
			
		
		</template>
		
		</el-table-column>
		

      </el-table>

    


  </div>
  
<!-- -------------  -->
<el-dialog
  v-model="dialog"
  title="新增关系"
>

  <el-form :model="form">


  
    <el-form-item label="规格">

      <el-input
        v-model="form.specification"
      />

    </el-form-item>



    <el-form-item label="胶囊">

      <el-input-number
        v-model="form.capsule"
      />

    </el-form-item>
	
	<el-form-item label="夹盘">
	
	  <el-input-number
	    v-model="form.clamp"
	  />
	
	</el-form-item>



  </el-form>



  <template #footer>

    <el-button
      @click="dialog=false"
    >
      取消
    </el-button>


    <el-button
      type="primary"
      @click="saveStock"
    >
      保存
    </el-button>


  </template>


</el-dialog>

</template>




<script setup lang="ts">

import { ref, computed, onMounted } from "vue"
import { ElMessageBox, ElMessage } from 'element-plus'
import { getStockCor,addStockCor ,deleteStockCor,updateStockCor} from "@/api/stock"
const dialog = ref(false)
const editId = ref<number | null>(null)

const form = ref({

    clamp:"",

    specification:"",

    capsule:""

})


const tableData = ref<any[]>([])






const fetchData = async()=>{


    const res = await getStockCor()


    tableData.value = res.data


    console.log(tableData.value)


}



onMounted(()=>{

    fetchData()

})


const opendialog = ()=>{
	    // 清空编辑状态
	editId.value = null
	
	    // 初始化表单

    form.value={
        clamp:"",
        specification:"",
        capsule:"",
    }

    dialog.value=true

}





const addStock = async () => {
    try {
		editId.value = null
        await addStockCor(form.value)
		console.log(form.value)

        ElMessage.success("保存成功")

        dialog.value = false

        await fetchData()

    } catch (error) {
        console.error(error)
        ElMessage.error("保存失败")
    }
}


const deleteStock = async(id:number)=>{

	try {
	    await ElMessageBox.confirm(
	        "确定删除吗？",
	        "提示"
	    )
	    
	    
	    await deleteStockCor(id)
	
	    ElMessage.success("删除成功")
	
	
		
	    dialog.value = false
	    await fetchData()
	
	} catch (error) {
	    console.error(error)
	    ElMessage.error("保存失败")
	}
	
	
	
	
	

}


const editStock = (row:any)=>{

    editId.value = row.id

    form.value = {

        clamp:row.clamp,

        specification:row.specification,

        capsule:row.capsule

    }

    dialog.value=true

}

const saveStock = async()=>{

    try{

        if(editId.value === null){

            // 新增
            await addStockCor(form.value)

        }else{

            // 修改
            await updateStockCor(
            
				editId.value,
				{
				
					"clamp":form.value.clamp,
					"specification":form.value.specification,
					"capsule":form.value.capsule
				}
            )

        }


        ElMessage.success("保存成功")

        dialog.value=false

        await fetchData()


    }catch(error){

        console.error(error)

        ElMessage.error("保存失败")

    }

}




</script>










<style scoped>

.content{

    display:flex;

    gap:20px;

}

.table-box{

    flex:2;

}

.table-box h3{

    margin-bottom:10px;

}

.toolbar{
	display:flex;
	justify-content: flex-start;
	align-items: center;
	gap: 20px;
	
}
.ction-buttons{
	display:flex;
	justify-content: flex-start;
	align-items: center;
	gap: 10px;
	
	
}

</style>