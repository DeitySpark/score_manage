<template>
	<div class="count-score">
		<!--		左边成绩统计表格-->
		<div class="score-table">
			<table-box :table-key="tableKey" :table-list="scoreList">
				<template v-slot:operation>
					<el-table-column label="操作">
						<template #default="scope">
							<el-button
									type="primary"
									round
									size="small"
									@click="editScore(scope.row)"
							>
								修改成绩
							</el-button>
						</template>
					</el-table-column>
				</template>
			</table-box>
		</div>
		<!--		弹出对话框-->
		<el-dialog
				v-model="centerDialogVisible"
				title="修改成绩"
				width="30%"
				align-center
		>
			<!--			弹出对话框的内容-->
			<div class="edit-form">
				<form-input-box :form="form"/>
			</div>
			<template #footer>
      <span class="dialog-footer">
        <el-button @click="cancelEdit">取消</el-button>
        <el-button type="primary" @click="confirmEdit">
        确认修改
        </el-button>
      </span>
			</template>
		</el-dialog>
		<!--		右边成绩图表-->
		<div class="score-count-img">
			<chart-box :count-list="countList"/>
		</div>
	</div>
</template>

<script>
import { getCountScore, updateScore } from '@/network/teacher'
import { msg } from '@/assets/js/InformMsg'
import 'element-plus/theme-chalk/el-message.css'
import { ref } from 'vue'


export default {
  name: "CountScore",
  components: {
    ChartBox: () => import('@/components/common/ChartBox'),
    TableBox: () => import('@/components/common/TableBox')
  },
  data () {
    return {
      centerDialogVisible: ref(false),
      form: {},
      scoreList: [],
      tableKey: [
        { title: '学号', value: 'stu_id' },
        { title: '姓名', value: 'stu_name' },
        { title: '成绩', value: 'score' }
      ],
      countList: [
        { score: '0-59', count: 0 },
        { score: '60-69', count: 0 },
        { score: '70-79', count: 0 },
        { score: '80-89', count: 0 },
        { score: '90-100', count: 0 }
      ],
      course: this.$store.state.countScoreCourse
    }
  },
  mounted () {
    this._getCountScore()
  },
  watch: {
    scoreList: function () {
      this._countScore()
    }
  },
  methods: {
    // 修改成绩
    editScore (row) {
      console.log(row)
      this.form = [
        { title: '学号', value: row.stu_id, disabled: 1 },
        { title: '姓名', value: row.stu_name, disabled: 1 },
        { title: '成绩', value: row.score, disabled: 0 }
      ]
      this.centerDialogVisible = true
    },
    // 取消修改
    cancelEdit () {
      this.centerDialogVisible = false
    },
    // 确认修改
    confirmEdit () {
      this.centerDialogVisible = false
      let obj = {
        stu_id: this.form[0].value,
        course: this.course,
        score: this.form[2].value
      }
      updateScore(obj).then(res => {
        if (res.data.code === 200) {
          msg('success', '修改成功')
        } else {
          msg('error', '修改失败')
        }
      })
      this._getCountScore()
    },
    // 统计成绩
    _countScore () {
      let scoreList = this.scoreList
      scoreList.forEach(item => {
        if (item.score >= 0 && item.score <= 59) {
          this.countList[0].count++
        } else if (item.score >= 60 && item.score <= 69) {
          this.countList[1].count++
        } else if (item.score >= 70 && item.score <= 79) {
          this.countList[2].count++
        } else if (item.score >= 80 && item.score <= 89) {
          this.countList[3].count++
        } else if (item.score >= 90 && item.score <= 100) {
          this.countList[4].count++
        }
      })
    },
    // 获取成绩
    _getCountScore () {
      let obj = { course_name: this.$store.state.countScoreCourse }
      getCountScore(obj).then(res => {
        console.log(res)
        if (res.data.code === 200) {
          this.scoreList = res.data.data
        } else {
          msg('error', res.data.msg)
        }
      })
    }
  }
}
</script>

<style scoped>
.count-score {
    display: flex;
    justify-content: space-between;
    padding: 0 20px;
}

/*成绩列表*/
.score-table {
    width: 50%;
    border-right: 1px solid #ebeef5;
}

/*成绩图表*/
.score-count-img {
    width: 45%;
}

/*弹出对话框*/
.dialog-footer button:first-child {
    margin-right: 10px;
}

/*表单*/
.edit-form {
    margin: 0 auto;
    display: flex;
    justify-content: center;
}
</style>
