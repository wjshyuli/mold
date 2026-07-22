import { defineStore } from "pinia"
import { ref } from "vue"
import { me } from "@/api/user"

export const useUserStore = defineStore("user", () => {

    const username = ref("")
    const isLogin = ref(false)


    // 获取当前登录用户
    async function getUser() {

        try {

            const res = await me()

            if (res.data.code === 200) {

                username.value = res.data.username
                isLogin.value = true

                return true
            }

        } catch (error) {

            isLogin.value = false
            return false
        }

    }


    return {
        username,
        isLogin,
        getUser
    }

})