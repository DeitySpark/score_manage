<template>
	<div class="login-view">
		<div class="main-box">
			<login-box></login-box>
			<p class="title">
				学<br>生<br>成<br>绩<br>管<br>理<br>系<br>统
			</p>
		</div>
	</div>
</template>

<script>
import LoginBox from '@/components/login/LoginBox'

export default {
  name: "LoginView",
  components: {
    LoginBox
  }
}
</script>

<style scoped>
.login-view{
	width: 100%;
	height: 100vh;
	background: url("@/assets/img/background.jpg") no-repeat center center ;
	background-size: cover;
	position: relative;
}
.main-box{
	height: 50%;
	background-color: rgba(255,255,255,0.3);
	position:absolute;
	top: 25%;
	left: 15%;
	border-radius: 30px;
	display: flex;
	flex-direction: row;
	justify-content: center;
}
.title{
	font-size: 22px;
	color: #fff;
	font-weight: bold;
	font-style: italic;
	margin: 30px 30px;
}
</style>
