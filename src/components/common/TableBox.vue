<template>
	<el-table :data="tableList" stripe style="width: 100%" height="520" class="table">
		<el-table-column :prop="item.value" :label="item.title" v-for="item in tableKey" :key="item"/>
		<el-table-column label="Operations" v-if="role!=='student'">
<!--			 eslint-disable-next-line-->
			<template #default="scope">
				<slot name="operation"></slot>
			</template>
		</el-table-column>
	</el-table>
</template>
<script>
export default {
  name: "TableBox",
  data () {
    return {
      role: this.$store.state.account.role
    }
  },
  props: {
    tableList: {
      type: Array,
      default: () => []
    },
    tableKey: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<style scoped>
.table{
		text-align: center;
}
</style>
