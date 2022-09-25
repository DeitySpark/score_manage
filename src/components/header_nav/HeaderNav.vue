<template>
	<el-container class="nav">
		<div class="left">
			<div class="logo">
				<span>学生成绩管理系统</span>
			</div>
		</div>
		<div class="right">
			<span class="search_box">
				<input type="search"><i class="iconfont icon-sousuo"/>
			</span>
			<user-info class="user-info"></user-info>
		</div>
	</el-container>
</template>

<script>
import UserInfo from '@/components/header_nav/UserInfo'

export default {
  name: 'HeaderView',
  components: {
    UserInfo
  },
  data () {
    return {
      searchIsShow: false
    }
  },
  methods: {
    searchClick () {
      this.searchIsShow = !this.searchIsShow
    }
  }
}
</script>

<style scoped>
@import '@/assets/css/base.css';
@import '@/assets/css/header_nav.css';
/*导航栏*/
.nav {
    background-color: #fff;
    width: 100%;
    height: 60px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12);
    display: flex;
    align-items: center;
    text-align: center;
    position: relative;
}
/*左边部分*/
/*logo*/
.logo {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    font-size: 20px;
    font-weight: bold;
    font-style: italic;
    color: #409eff;
		margin-left: 20px;
}
/*右边部分*/
.right {
    position: absolute;
    right: 40px;
    display: flex;
    align-items: center;
}

.search-btn {
    position: absolute;
    right: 70px;
}

.icon-sousuo:active {
    font-size: 20px;
    color: #409eff;
}

/*搜素框*/
.search_box {
    display: flex;
    align-items: center;
    justify-content: space-around;
    border: 1px solid #ccc;
    border-radius: 50px;
    padding: 0 10px;
    height: 30px;
}

.search_box input {
    border: none;
    outline: none;
    width: 100%;
    height: 100%;
    font-size: 14px;
    color: #666;
    margin-left: 10px;
}

/*搜索按钮*/
.icon-sousuo {
    font-size: 20px;
    color: #ccc;
}

.user-info {
    margin-left: 20px;
}

</style>
