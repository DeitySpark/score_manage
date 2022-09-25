<template>
	<div class="common-layout ">
		<el-container class="main-page">
			<!--    header_nav -->
			<el-header class="header">
				<header-nav></header-nav>
			</el-header>

			<!--    aside -->
			<el-aside class="aside">
				<student v-if="role === 'Student'"/>
				<teacher v-if="role === 'Teacher'"/>
				<admin v-if="role === 'Admin'"/>
			</el-aside>
			<!-- main-content -->
			<el-main>
				<router-view/>
			</el-main>
		</el-container>

	</div>
</template>

<script>
import HeaderNav from '@/components/header_nav/HeaderNav'
import Student from '@/components/side_nav/Student'
import Admin from '@/components/side_nav/Admin'
import Teacher from '@/components/side_nav/Teacher'

export default {
  name: 'IndexView',
  components: {
    Admin,
    Student,
    Teacher,
    HeaderNav
  },
  data () {
    return {
      role: this.$store.state.user.role
    }
  }
}
</script>

<style scoped>
@import '@/assets/css/base.css';

* {
    margin: 0;
    padding: 0;
}

.main-page {
    background-color: #f0f0f0;
    width: 100%;
    height: 100vh;
}

.header {
    padding: 0;
    height: 60px;
}

.aside {
    width: 200px;
    background-color: #fff;
    height: calc(100vh - 60px);
}
</style>
