<template>
	<div class="login">
		<form action="">
			<div class="form-group">
				<input type="text" v-model.lazy.trim="username" class="form-control" placeholder="Username">
			</div>
			<div class="form-group" v-if="title==='Register'">
				<input type="email" v-model.trim.lazy="email" class="form-control" placeholder="E-mail">
			</div>
			<div class="form-group">
				<input type="password" v-model.trim.lazy="password" class="form-control" placeholder="Password">
			</div>
			<div class="form-control" v-if="title==='Register'">
				<el-select v-model.trim="role" class="m-2 radius" placeholder="Select">
					<el-option
							v-for="item in options"
							:key="item.value"
							:label="item.label"
							:value="item.value"
					/>
				</el-select>
			</div>
			<el-button type="submit" class="form-button primary" @click="submitInfo">{{ title }}</el-button>
			<a href="#" class="tip" v-if="title==='Register'" @click="changeFunction">Have an account, log in...</a>
			<a href="#" class="tip" v-if="title==='Login'" @click="changeFunction">No account, sign up...</a>
		</form>
	</div>
</template>

<script>
import { ref } from 'vue'
import { loginSub, registerSub } from '@/network/log_reg'
import 'element-plus/theme-chalk/el-message.css'
import { msg } from '@/components/login/InformMsg'

export default {
  name: "LoginBox",
  data () {
    return {
      title: 'Login',
      value: ref('Student'),
      options: [
        { value: 'student', label: 'Student' },
        { value: 'teacher', label: 'Teacher' }
      ],
      username: '',
      email: '',
      password: '',
      role: ''
    }
  },
  methods: {
    changeFunction () {
      if (this.title === 'Login') {
        this.title = 'Register'
      } else {
        this.title = 'Login'
      }
    },
    submitInfo () {
      // 登录
      if (this.title === 'Login') {
        //  如果信息为空，弹出警告
        if (this.username === '' || this.password === '') {
          msg('warning', '请填写完整信息')
        } else {
          // 创建登录信息对象
          let loginObj = {
            username: this.username,
            password: this.password
          }
          // 发送登录请求
          loginSub(loginObj).then(
            res => {
              console.log(res)
              // 请求成功，返回响应
              if (res.data.code === 200) {
                // 如果登录成功，跳转到首页
                msg('success', res.data.msg)
                this.$router.push({ path: '/index' })
                console.log(res.data.data)
                this.$store.commit('setToken', res.data.data)
              } else {
                // 如果登录失败，弹出警告
                msg('error', res.data.msg)
              }
            },
            err => {
              // 请求失败，弹出警告
              msg('error', err)
            })
        }
      } else {
        // 注册
        if (this.username === '' || this.password === '' || this.email === '' || this.role === '') {
          msg('warning', '请填写完整信息')
        } else {
          // 创建注册信息对象
          let registerObj = {
            username: this.username,
            email: this.email,
            password: this.password,
            role: this.role
          }
          // 发送注册请求
          registerSub(registerObj).then(
            res => {
              // 请求成功，返回响应
              // 如果注册成功，跳转到登录页面
              if (res.data.code === 200) {
                msg('success', 'Register successfully')
                this.$router.push({ path: '/' })
              } else {
                // 如果注册失败，弹出警告
                msg('error', res.data.msg)
              }
            },
            err => {
              // 请求失败，返回错误
              console.log(err)
            })
        }
      }
    }
  }
}
</script>

<style scoped>
@import "@/assets/css/base.css";
/*表单盒子*/
.login {
    height: 100%;
    background-color: rgba(255, 255, 255, 0.6);
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 30px;
    padding: 0 30px;
}

/*form 表单*/
.login form {
    margin: 30px 0;
    width: 100%;
    height: 90%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

input, select {
    outline: none;
}

/*输入框*/
.login .form-group {
    margin-bottom: 20px;
    background-color: #fff;
    border-radius: 4px;
    height: 30px;
}

.form-group input {
    height: 30px;
    border: none;
    border-radius: 25px;
    padding: 0 10px;
}

/*选择栏*/
.form-control {
    background-color: #fff;
    margin: 0 auto 20px;
    border-radius: 25px;
}

/*按钮*/
.login .form-button {
    width: 80px;
    margin-left: 30%;
}

/*最后一行提示*/
.tip {
    cursor: pointer;
    color: #7080e8;
    font-size: 12px;
    margin-top: 20px;
    text-align: right;
}
</style>

