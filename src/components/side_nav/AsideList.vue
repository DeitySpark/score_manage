<template>
	<el-col :span="24">
		<el-menu
				default-active="2"
				class="el-menu-vertical-demo"
		>
			<el-menu-item index="1">
				<el-icon><House /></el-icon>
				<span >主页</span>
			</el-menu-item>
			<aside-static-menu />
			<aside-openal-menu />
		</el-menu>
	</el-col>
</template>

<script>
import AsideOpenalMenu from '@/components/side_nav/AsideOpenalMenu'
import AsideStaticMenu from '@/components/side_nav/AsideStaticMenu'
import { House } from '@element-plus/icons'

export default {
  name: "AsideList",
  components: {
    House,
    AsideStaticMenu,
    AsideOpenalMenu
  }
}
</script>

<style scoped>

</style>
