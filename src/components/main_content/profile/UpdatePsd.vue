<template>
	<el-form :model="form" label-width="120px"  class="profile-form">
		<el-form-item label="用户名:" >
			<el-input type="text" v-model="form.username" disabled="true"/>
		</el-form-item>
		<el-form-item label="旧密码:">
			<el-input type="password" v-model="form.oldPassword"/>
		</el-form-item>
		<el-form-item label="新密码:">
			<el-input type="password" v-model="form.newPassword"/>
		</el-form-item>
		<el-form-item label="确认密码:">
			<el-input type="password" v-model="form.confirmPassword"/>
		</el-form-item>
		<el-form-item>
			<el-button type="primary" @click="onSubmit">修改密码</el-button>
		</el-form-item>
	</el-form>
</template>

<script>
export default {
  name: "UpdatePsd",
	data () {
		return {
			form:{
        username: this.$store.state.account.username,
        oldPassword: '',
        newPassword: '',
        confirmPassword: ''
			}
		}
	},
}
</script>

<style scoped>
.profile-form {
    margin: 20px;
    max-width: 700px;
}
</style>
