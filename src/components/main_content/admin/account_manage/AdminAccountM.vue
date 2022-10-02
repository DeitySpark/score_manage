<template>
	<div class="account-manage">
		<data-show :table-list="tableList" :table-key="tableKey">
		</data-show>
	</div>
</template>

<script>
import { StudentManageList } from '@/network/admin'

export default {
  name: "AdminAccountM",
  data () {
    return {
      tableKey: [
        { title: '学号', value: 'stu_id', sortable: 1},
        { title: '姓名', value: 'name' },
        { title: '性别', value: 'sex' },
        { title: '昵称', value: 'username' },
        { title: '学院', value: 'college' },
        { title: '专业 ', value: 'major' },
        { title: '学分 ', value: 'credits' },
      ],
      tableList: []
    }
  },
  mounted () {
    this._StudentManageList()
  },
  methods: {
    _StudentManageList () {
      StudentManageList().then(res => {
        this.tableList = res.data.data
      })
    }
  }
}
</script>

<style scoped>

</style>
