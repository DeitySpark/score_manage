<template>
	<aside-nav />
</template>

<script>
import AsideNav from '@/components/side_nav/AsideNav'
import { Info } from '@/assets/js/aside/student'
export default {
  name: "StudentAside",
	components: {
		AsideNav
	},
	provide() {
		return {
			Info
		}
	},
}
</script>

<style scoped>

</style>
