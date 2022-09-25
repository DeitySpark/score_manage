<template>
	<el-aside width="200px">
		<aside-list />
	</el-aside>
</template>

<script>
import AsideList from '@/components/side_nav/AsideList'

export default {
  name: 'AsideView',
  components: {
    AsideList
  }
}
</script>

<style scoped>
@import '@/assets/css/base.css';


</style>
