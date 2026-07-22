<template>
  <el-container class="layout">
    <!-- 左侧菜单 -->
    <el-aside width="220px" class="aside">
      <div class="logo">
        <h2>MES_模具汇总</h2>
        
      </div>

      <el-menu
        router
        class="menu"
        default-active="/"
        :default-openeds="['mold']"
      >
		
		
		<el-menu-item index="/">
		    首页
		</el-menu-item>
<!-- 		<el-menu-item index="Login">
		    登录
		</el-menu-item> -->

		
        <el-sub-menu index="mold">
          <template #title>
            <span>模具管理</span>
          </template>

          <el-menu-item index="/mold/specification">
            硫化机规格设置
          </el-menu-item>

          <el-menu-item index="/mold/weekcard_change">
            周期牌更换记录
          </el-menu-item>

          <el-menu-item index="/mold/mold_status">
            硫化模具现状
          </el-menu-item>

          <el-menu-item index="/mold/stop_status">
            硫化停机统计
          </el-menu-item>

          <el-menu-item index="/mold/goF4">
            四分厂模具链接
          </el-menu-item>
        </el-sub-menu>

        <el-sub-menu index="stock">
          <template #title>
            <span>胶囊夹盘库存管理</span>
          </template>

          <el-menu-item index="/mold/stock_base">
            库存基础设置
          </el-menu-item>

          <el-menu-item index="/mold/stock_correspondence">
            对应关系表
          </el-menu-item>

          <el-menu-item index="/mold/stock_show">
            库存现状
          </el-menu-item>


        </el-sub-menu>

      </el-menu>
    </el-aside>

    <!-- 右侧 -->
    <el-container>
      <!-- 顶部 -->
      <el-header class="header">

		    <Header></Header>
		
		
      </el-header>

      <!-- 内容 -->
      <el-main class="main">
        <el-card shadow="never">
          <router-view />
        </el-card>
      </el-main>
    </el-container>
  </el-container>
</template>



<script setup lang="ts">

import Header from '@/components/Header.vue';
</script>






<style scoped>

.layout {
  height: 100vh;
}

/* 左侧 */

.aside {
  /* position:fixed;
  left:0;
  top: 0;
  width: 200px;
  height: 100vh; */

  border-right: 1px solid #ebeef5;
  background: #ffffff;
  
}

.logo {
  height: 60px;

  display: flex;
  flex-direction: column;

  justify-content: center;
  align-items: center;

  border-bottom: 1px solid #ebeef5;
}

.logo h2 {
  margin: 0;
  font-size: 20px;
}

.logo span {
  font-size: 12px;
  color: #909399;
}

/* 菜单 */

.menu {
  border-right: none;
}

/* Header */
/* 
.header {
  height: 60px;

  display: flex;

  justify-content: space-between;
  align-items: center;

  padding: 0 24px;

  border-bottom: 1px solid #ebeef5;

  background: white;
}

.header-left {
  font-size: 18px;
  font-weight: bold;
}

.header-right {
  cursor: pointer;
} */

/* 主区域 */

.main {


  
  background: #f5f7fa;
  padding: 0px;
}

</style>
