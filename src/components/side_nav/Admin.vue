<template>
	<aside-nav />
</template>

<script>
import AsideNav from '@/components/side_nav/AsideNav'
import { Info } from '@/assets/js/aside/admin'

export default {
  name: "AdminAside",
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
