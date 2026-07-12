<template>

  <!-- 页面标题 -->
  

    

    <div class="toolbar">
		<h2>库存基础数据维护</h2>
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

    <!-- 左边 -->

    <div class="table-box">

      <h3>胶囊库存数量</h3>

      <el-table
        :data="capsuleData"
        border
        stripe
        height="700"
      >

        <el-table-column
          prop="specification"
          label="胶囊规格"
		  width="240"
        />

        <el-table-column
          prop="quantity"
          label="胶囊数量(个)"
		  width="120"
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

    <!-- 右边 -->

    <div class="table-box">

      <h3>夹盘库存数量</h3>

      <el-table
        :data="clampData"
        border
        stripe
        height="700"
		style="width: 100%;"
      >

        <el-table-column
          prop="specification"
          label="夹盘规格"
		  width="240px"
        />

        <el-table-column
          prop="quantity"
          label="夹盘数量(个)"
		  width="120px"
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

  </div>
  
<!-- -------------  -->
<el-dialog
  v-model="dialog"
  title="新增库存"
>

  <el-form :model="form">


    <el-form-item label="类型">

      <el-select v-model="form.type">

        <el-option
          label="胶囊"
          value="胶囊"
        />

        <el-option
          label="夹盘"
          value="夹盘"
        />

      </el-select>

    </el-form-item>



    <el-form-item label="型号">

      <el-input
        v-model="form.specification"
      />

    </el-form-item>



    <el-form-item label="数量">

      <el-input-number
        v-model="form.quantity"
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
import { getStockBase,addStockBase ,deleteStockBase,updateStockBase} from "@/api/stock"
const dialog = ref(false)
const editId = ref<number | null>(null)

const form = ref({

    type:"胶囊",

    specification:"",

    quantity:0

})


const tableData = ref<any[]>([])



// 胶囊数据
const capsuleData = computed(()=>{

    return tableData.value.filter(
        item => item.type === "胶囊"
    )

})



// 夹盘数据
const clampData = computed(()=>{

    return tableData.value.filter(
        item => item.type === "夹盘"
    )

})





const fetchData = async()=>{


    const res = await getStockBase()


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
        type:"胶囊",
        specification:"",
        quantity:1
    }

    dialog.value=true

}





const addStock = async () => {
    try {
		editId.value = null
        await addStockBase(form.value)
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
	    
	    
	    await deleteStockBase(id)
	
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

        type:row.type,

        specification:row.specification,

        quantity:row.quantity

    }

    dialog.value=true

}

const saveStock = async()=>{

    try{

        if(editId.value === null){

            // 新增
            await addStockBase(form.value)

        }else{

            // 修改
            await updateStockBase(
            
				editId.value,
				{
				
					"type":form.value.type,
					"specification":form.value.specification,
					"quantity":form.value.quantity
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

    flex:1;

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