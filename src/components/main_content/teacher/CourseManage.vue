<template>
	<div class="course-manage"></div>
	<table-box class="course-table" :table-key="tableKey" :table-list="courseList">
		<template v-slot:operation>
			<el-button
					type="primary"
					round
					size="small"
					@click="handleEdit(scope.$index, scope.row)">
				查看统计
			</el-button>
		</template>
	</table-box>
</template>

<script>
import { getStudentCourse } from '@/network/teacher'

export default {
  name: "CourseManage",
  data () {
    return {
      tea_id: this.$store.state.account.user_id,
      courseList: [],
      tableKey: [
        { title: '课程编号', value: 'id' },
        { title: '类别', value: 'type' },
        { title: '课程名', value: 'name' },
        { title: '学分', value: 'credit' },
        { title: '上课时间', value: 'start_time' },
        { title: '上课地点', value: 'place' },
        { title: '课时', value: 'hours' }
      ]
    }
  },
  components: {
    TableBox: () => import('@/components/common/TableBox')
  },
  mounted () {
    this.getCourse(this.tea_id)
  },
  methods: {
    getCourse (tea_id) {
      let obj = { tea_id: tea_id }
      getStudentCourse(obj).then(res => {
        console.log(res)
        this.courseList = res.data.data
      })
    }
  }
}
</script>

<style scoped>

</style>
