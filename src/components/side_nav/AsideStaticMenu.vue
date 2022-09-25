<template>
	<el-menu-item v-for="(item, index) in Info.staticHandle" :key="item" :index="index">
		<el-icon>
			<Tickets/>
		</el-icon>
		<span>{{ item.title }}</span>
	</el-menu-item>
</template>

<script>
import { Tickets } from '@element-plus/icons'

export default {
  name: "AsideStaticMenu",
  components: {
    Tickets
  },
  inject: ['Info']
}
</script>

<style scoped>

</style>
