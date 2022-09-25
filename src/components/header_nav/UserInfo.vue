<template>
	<el-dropdown size="large" >
		<span class="uN">{{ userName }}</span>
		<template #dropdown>
			<el-dropdown-menu class="menu">
				<el-dropdown-item>
					<span>abcd</span>
				</el-dropdown-item>
				<el-dropdown-item>个人中心</el-dropdown-item>
				<el-dropdown-item>退出登录</el-dropdown-item>
			</el-dropdown-menu>
		</template>
	</el-dropdown>
</template>

<script>
export default {
  name: "UserInfo",
	data() {
		return {
			userName: this.$store.state.user.username
		}
	}
}
</script>

<style scoped>
@import '@/assets/css/base.css';
.uN {
	font-size: 16px;
	color: #409eff;
}
/*用户信息*/
.menu{
		text-align: center;
}


</style>
