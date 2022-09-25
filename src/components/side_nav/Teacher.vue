<template>
	<aside-nav />
</template>

<script>
import AsideNav from '@/components/side_nav/AsideNav'
import { Info } from '@/assets/js/aside/teacher'

export default {
  name: "TeacherAside",
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
