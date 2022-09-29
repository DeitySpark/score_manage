<template>
	<el-form :model="form1" label-width="120px" disabled class="profile-form">
		<el-form-item :label="form1.stu_id.title" v-if="this.role === 'student'">
			<el-input v-model="form1.stu_id.value"/>
		</el-form-item>
		<el-form-item :label="form1.name.title">
			<el-input v-model="form1.name.value"/>
		</el-form-item>
		<el-form-item :label="form1.sex.title">
			<el-input v-model="form1.sex.value"/>
		</el-form-item>
		<el-form-item :label="form1.birthday.title">
			<el-col :span="11">
				<el-date-picker
						v-model="form1.birthday.value"
						type="date"
						placeholder="选择出生日期"
						style="width: 100%"
				/>
			</el-col>
		</el-form-item>
	</el-form>
	<el-form :model="form2" label-width="120px" disabled class="profile-form">
		<el-form-item v-for="item in form2" :key="item" :label="item.title">
			<el-input v-model="item.value"/>
		</el-form-item>
	</el-form>
</template>

<script>
import { getStudentInfo } from '@/network/student'
import { getTeacherInfo } from '@/network/teacher'

export default {
  name: "ProfileInfo",
  data () {
    return {
      form1: {
        stu_id: {},
        name: {},
        sex: {},
        birthday: {}
      },
      form2: {
        address: {},
        college: {},
        major: {},
        credits: {},
        GPA: {}
      },
      username: this.$store.state.account.username,
      user_id: this.$store.state.account.user_id,
      role: this.$store.state.account.role
    }
  },
  mounted () {
    this.getProfileInfo()
  },
  methods: {
    getProfileInfo () {
      console.log(this.username)
      if (this.role === 'student') {
        getStudentInfo({ username: this.username }).then(res => {
          console.log(res)
          this.form1 = res.data.data[0]
          this.form2 = res.data.data[1]
        })
      } else if (this.role === 'teacher') {
        getTeacherInfo({ user_id: this.user_id }).then(res => {
          console.log(res)
          this.form1 = res.data.data[0]
          this.form2 = res.data.data[1]
        })
      } else {
        // getAdminInfo({ username: this.username }).then(res => {
        //   console.log(res)
        // })
      }
    }
  }
}
</script>

<style scoped>
.profile-form {
    margin: 20px;
    max-width: 700px;
}
</style>
