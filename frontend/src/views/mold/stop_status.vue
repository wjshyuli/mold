<template>
    <div class="top">
    	<div class="topleft" >
    		<h2 style="border">硫化停机统计</h2>

    		<el-date-picker
    		v-model="timeRange"
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
    		  @click="search"
    		>
    		  查询
    		</el-button>

    		<el-button
    		  type="primary"
    		  @click="refresh"
    		>
    		  刷新
    		</el-button>

    		<el-button
				type="success"
				:loading="exportLoading"
				@click="exportExcel"
    		>
    		  导出
    		</el-button>

    	</div>
    </div>



	<el-tabs v-model="activeName">



	    <el-tab-pane
	      label="机台汇总"
	      name="machine"
	    >
	    <MachineTable ref="machineRef"/>
	    </el-tab-pane>

	    <el-tab-pane
	      label="班组汇总"
	      name="shift"
	    >
	    <ShiftTable ref="shiftRef"/>
	    </el-tab-pane>

		<el-tab-pane
		  label="停机明细"
		  name="detail"
		>
		<DetailTable ref="detailRef"/>
		</el-tab-pane>

		<el-tab-pane
		  label="停机汇总"
		  name="summary"
		>
		<SummaryTable ref="summaryRef"/>
		</el-tab-pane>

	</el-tabs>






</template>




<script setup lang="ts">
	import DetailTable from "@/views/mold/stop_status/DetailTable.vue"
	import SummaryTable from "@/views/mold/stop_status/SummaryTable.vue"
	import MachineTable from "@/views/mold/stop_status/MachineTable.vue"
	import ShiftTable from "@/views/mold/stop_status/Shift.vue"



	import { useFactoryStore } from "@/stores/factory"
	import { storeToRefs } from "pinia"
	import { onMounted, ref,watch } from "vue"
	import { downloadBlob } from "@/utils/download"

	import { ElMessage } from "element-plus"

	import { computed } from "vue"
	type TabName = "detail"| "summary"| "machine"| "shift"

	const activeName = ref<TabName>("machine")


	const detailRef = ref()
	const summaryRef = ref()
	const machineRef = ref()
	const shiftRef = ref()
	const exportLoading = ref(false) 
	const pageMap = {
	  detail: detailRef,
	  machine: machineRef,
	  shift: shiftRef,
	  summary: summaryRef,
	}


	const factory_store =useFactoryStore()
	const {factory} = storeToRefs(factory_store)

	const timeRange = ref<any[]>([])



	const initTimeRange = () => {

	    const today = new Date()

	    // 今天07:00
	    const end = new Date(today)
	    end.setHours(7, 0, 0, 0)

	    // 昨天07:00
	    const start = new Date(end)
	    start.setDate(start.getDate() - 1)

	    timeRange.value = [
	        formatDate(start),
			formatDate(end)


	    ]

	}



	const formatDate = (date: Date) => {
	    const pad = (n: number) => String(n).padStart(2, "0")

	    return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())} ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`
	}

	const currentPage = computed(() => pageMap[activeName.value]?.value)
	const body = computed(
		()=>({
		factory: factory_store.factory,
		st: timeRange.value[0],
		et: timeRange.value[1],
		type: activeName.value,
	 }))


	const search = async() => {
		console.log("activeName1111", activeName.value)
		console.log("currentPage1111", currentPage.value)
		if(!timeRange.value||timeRange.value.length !== 2  ){
		        ElMessage.warning("请选择时间范围")
		        return
		    }
		console.log(currentPage.value)
		console.log(currentPage.value?.fetchData)
		await currentPage.value?.fetchData(body.value)

		ElMessage.success('查询完成')
	}
	
import { ElLoading } from "element-plus"
const exportExcel = async () => {
  if (!timeRange.value || timeRange.value.length !== 2) {
    ElMessage.warning("请选择时间范围")
    return
  }

  exportLoading.value = true
	const loading = ElLoading.service({
      lock: true,
      text: "文件正在生成，请稍候……",
      background: "rgba(0,0,0,0.5)"
    })
  console.log("开始导出")

  try {
    console.log("开始请求后端")

    const res = await currentPage.value.exportData(body.value)

    console.log("后端返回", res)

    downloadBlob(res.data, `${activeName.value}.xlsx`)

    console.log("下载完成")
  } catch (e) {
    console.error(e)
    ElMessage.error("导出失败")
  } finally {
    console.log("finally")

    exportLoading.value = false
	loading.close()
  }
}








	const refresh = async()=>{

	    initTimeRange()
		await search()

	}


	onMounted(
	()=>{
	initTimeRange()
	search()
	}
	)

	watch(
		[factory,activeName],
		() => {
		search()
	  }
	  )

	watch(timeRange, (newValue) => {
	  if (!newValue || newValue.length !== 2) return

	  const start = new Date(newValue[0])
	  const end = new Date(newValue[1])

	  const diffDays =
	    (end.getTime() - start.getTime()) / (1000 * 60 * 60 * 24)

	  if (diffDays > 7) {
	    ElMessage.warning("查询时间不能超过7天，已恢复默认时间")
	    initTimeRange()
	  }
	})










</script>












<style >
	.topleft{
		  display: flex;
		  justify-content: space-between;
		  width: 700px;
		  align-items: center;
		  gap: 20px;
	  }
	.top,.topright{
		  display: flex;
		  align-items: center;
		  gap: 20px;
	  }

</style>
