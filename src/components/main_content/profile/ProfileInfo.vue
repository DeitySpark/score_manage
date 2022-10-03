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
	<div class="profile-form">
		<form-input-box :form="form2" class="profile-form-item"/>
	</div>

</template>

<script>
import { getStudentInfo } from '@/network/student'
import { getTeacherInfo } from '@/network/teacher'
import FormInputBox from '@/components/common/FormInputBox'

export default {
  name: "ProfileInfo",
  components: {
    FormInputBox
  },
  data () {
    return {
      form1: {
        stu_id: {},
        name: {},
        sex: {},
        birthday: {}
      },
      form2: [],
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
      // console.log(this.username)
      if (this.role === 'student') {
        getStudentInfo({ username: this.username }).then(res => {
          console.log(res)
          this.form1 = res.data.data[0]
          let form2 = res.data.data[1]
          for(let i in form2) {
            form2[i]['disabled'] = 1
          }
          // console.log(form2)
          this.form2 = form2
        })
      } else {
        getTeacherInfo({ user_id: this.user_id }).then(res => {
          this.form1 = res.data.data[0]
          let form2 = res.data.data[1]
          for(let i in form2) {
						form2[i]['disabled'] = 1
					}
          // console.log(form2)
          this.form2 = form2
        })
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

.profile-form-item {
    margin: 0 80px;
}
</style>
