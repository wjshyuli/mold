<script setup lang="ts">
import { useRoute } from "vue-router"
import MainLayout from "./layout/MainLayout.vue"

const route = useRoute()

</script>


<template>

  <MainLayout v-if="route.path !== '/login'">

      <RouterView />

  </MainLayout>


  <RouterView v-else />


</template>