<template>
	<el-menu
			default-active="2"
			class="el-menu-vertical-demo"
			@open="handleOpen"
			@close="handleClose"
	>
		<el-sub-menu v-for="(item, index) in Info.openalHandle" :key="item" :index='index'   >
			<template #title>
				<el-icon>
					<Tickets />
				</el-icon>
				<span>{{ item.title }}</span>
			</template>
			<el-menu-item v-for="(i, ind) in item.contain" :key="i" :index="index+'-'+ind" >
				<el-icon>
					<Link />
				</el-icon>
				<span>{{ i.title }}</span>
			</el-menu-item>
		</el-sub-menu>
	</el-menu>
</template>

<script>
import { Tickets, Link } from "@element-plus/icons"

export default {
  name: "AsideOpenalMenu",
  data () {
    return {
      activeIndex: '1'
    }
  },
  inject: ['Info'],
  components: {
    Tickets,
    Link
  },
	methods: {
		handleOpen(key, keyPath) {
			console.log(key, keyPath);
		},
		handleClose(key, keyPath) {
			console.log(key, keyPath);
		}
	}
}
</script>

<style scoped>

</style>
