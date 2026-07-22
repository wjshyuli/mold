<template>
  <div class="login-container">
    <div class="login-card">
      <!-- 标题 -->
      <div class="login-header">
        <h2>欢迎登录</h2>
        <p>请输入您的账号信息</p>
      </div>

      <!-- 登录表单 -->
      <form @submit.prevent="handleLogin" class="login-form">
        <!-- 用户名 -->
        <div class="form-group">
          <label for="username">用户名</label>
          <div class="input-wrapper">
            <span class="input-icon">👤</span>
            <input
              id="username"
              v-model="loginForm.username"
              type="text"
              placeholder="请输入用户名"
              autocomplete="username"
              required
            />
          </div>
        </div>

        <!-- 密码 -->
        <div class="form-group">
          <label for="password">密码</label>
          <div class="input-wrapper">
            <span class="input-icon">🔒</span>
            <input
              id="password"
              v-model="loginForm.password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="请输入密码"
              autocomplete="current-password"
              required
            />
            <button
              type="button"
              class="toggle-password"
              @click="showPassword = !showPassword"
            >
              {{ showPassword ? '🙈' : '👁️' }}
            </button>
          </div>
        </div>

        <!-- 登录按钮 -->
        <button type="submit" class="login-btn" :disabled="loading">
          <span v-if="loading">登录中...</span>
          <span v-else>登 录</span>
        </button>

        <!-- 错误提示 -->
        <div v-if="errorMessage" class="error-message">
          ❌ {{ errorMessage }}
        </div>
      </form>

      <!-- 底部额外操作 -->
		<div class="login-footer">
        <a href="#">忘记密码？</a>
        <a href="#">注册新账号</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { login,csrf ,me} from "@/api/user"
import { ElMessage } from "element-plus"
import { ref, reactive } from 'vue'
  
import { onMounted } from "vue"
import { useUserStore } from "@/stores/user"

// 如果你使用 Vue Router，可以引入：
import { useRouter } from 'vue-router'

const router = useRouter()

// 表单数据
const loginForm = reactive({
  username: '',
  password: ''
})

// 状态
const loading = ref(false)
const errorMessage = ref('')
const showPassword = ref(false)


onMounted(async () => {
	try{
	
	        await csrf()
	
	    }catch(e){
	
	        console.log("csrf获取失败")
	
	    }

    
})
  

// 登录提交处理
const handleLogin = async () => {
  // 清空之前的错误
  errorMessage.value = ''

  // 简单前端验证
  if (!loginForm.username.trim() || !loginForm.password.trim()) {
    errorMessage.value = '用户名和密码不能为空'
    return
  }

  loading.value = true
  
  
try {

    const res = await login(loginForm)

    if (res.data.code == 200) {

        ElMessage.success("✅ 登录成功")
		



        
        const userStore = useUserStore()
		
		
		
		await userStore.getUser()
		
		    
		
		router.push("/")
		
		
		
		

    } else {

        errorMessage.value = res.data.msg|| '登录失败，请检查用户名和密码'

    }

}
catch (err) {

    errorMessage.value = "网络异常"

}
finally {

    loading.value = false

}
  
  	
	

}
</script>

<style scoped>
/* ===== 全局重置 & 容器 ===== */
.login-container {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 20px;
}

/* ===== 登录卡片 ===== */
.login-card {
  background: white;
  border-radius: 16px;
  padding: 40px 36px 30px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease;
}

.login-card:hover {
  transform: translateY(-4px);
}

/* ===== 标题 ===== */
.login-header {
  text-align: center;
  margin-bottom: 28px;
}

.login-header h2 {
  margin: 0 0 6px;
  font-size: 26px;
  font-weight: 700;
  color: #333;
}

.login-header p {
  margin: 0;
  color: #888;
  font-size: 14px;
}

/* ===== 表单 ===== */
.login-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.form-group label {
  font-size: 14px;
  font-weight: 600;
  color: #555;
}

/* ===== 输入框 ===== */
.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  border: 1.5px solid #ddd;
  border-radius: 8px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  background: #fafafa;
}

.input-wrapper:focus-within {
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
  background: white;
}

.input-icon {
  padding: 0 10px 0 14px;
  font-size: 16px;
  opacity: 0.6;
  user-select: none;
}

.input-wrapper input {
  flex: 1;
  padding: 12px 12px 12px 0;
  border: none;
  background: transparent;
  font-size: 15px;
  outline: none;
  color: #333;
  min-width: 0;
  width: 100%;
}

.input-wrapper input::placeholder {
  color: #aaa;
}

/* ===== 密码切换按钮 ===== */
.toggle-password {
  background: none;
  border: none;
  padding: 0 14px 0 8px;
  font-size: 18px;
  cursor: pointer;
  opacity: 0.6;
  transition: opacity 0.2s;
  flex-shrink: 0;
}

.toggle-password:hover {
  opacity: 1;
}

/* ===== 登录按钮 ===== */
.login-btn {
  margin-top: 6px;
  padding: 14px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 17px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  letter-spacing: 2px;
}

.login-btn:hover:not(:disabled) {
  transform: scale(1.02);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
}

.login-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

/* ===== 错误提示 ===== */
.error-message {
  margin-top: 4px;
  padding: 10px 14px;
  background: #fee2e2;
  border: 1px solid #fecaca;
  border-radius: 8px;
  color: #b91c1c;
  font-size: 14px;
  text-align: center;
}

/* ===== 底部链接 ===== */
.login-footer {
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
  font-size: 14px;
}

.login-footer a {
  color: #667eea;
  text-decoration: none;
  transition: color 0.2s;
}

.login-footer a:hover {
  color: #764ba2;
  text-decoration: underline;
}
</style>