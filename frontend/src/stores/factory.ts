import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useFactoryStore = defineStore('factory', () => {

  // 当前分厂
  const factory = ref(1)

  return {
    factory
  }

})