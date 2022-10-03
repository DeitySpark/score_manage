import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "login" */ '@/views/LoginView'),
    meta: {
      isKeepAlive: false
    }
  },
  // 学生端
  {
    path: '/student',
    name: 'Student',
    component: () => import(/* webpackChunkName: "index" */ '@/views/StudentView'),
    meta: {
      isKeepAlive: true
    },
    children: [
      // 首页
      {
        path: 'index',
        name: 'StudentIndex',
        components: {
          stuTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/home/HomeContent')
        }
      },
      // 成绩管理
      {
        path: 'score',
        name: 'StuScoreManage',
        components: {
          stuTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/student/ScoreManager.vue')
        }
      },
      // 个人信息
      {
        path: 'profile',
        name: 'StuProfile',
        components: {
          stuTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/student/StuProfile.vue')
        }
      },
      // 修改密码
      {
        path: 'updatepwd',
        name: 'StuUpdatePwd',
        components: {
          stuTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/student/UpdatePwd.vue')
        }
      }
    ]
  },
  // 教师端
  {
    path: '/teacher',
    name: 'TeacherView',
    component: () => import(/* webpackChunkName: "notfound" */ '@/views/TeacherView'),
    meta: {
      isKeepAlive: false
    },
    children: [
      // 首页
      {
        path: 'index',
        name: 'TeacherIndex',
        components: {
          teaTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/home/HomeContent')
        }
      },
      // 课程管理
      {
        path: 'course',
        name: 'ScoreManage',
        components: {
          teaTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/teacher/TeaCourseManage.vue')
        }
      },
      // 课程数据统计
      {
        path: 'countscore',
        name: 'CountScore',
        components: {
          teaTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/teacher/CountScore.vue')
        }
      },
      // 个人信息
      {
        path: 'profile',
        name: 'TeaProfile',
        components: {
          teaTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/teacher/TeaProfile.vue')
        }
      },
      // 修改密码
      {
        path: 'updatepwd',
        name: 'TeaUpdatePwd',
        components: {
          teaTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/teacher/TeaUpdatePwd.vue')
        }
      }
    ]
  },
  // 管理员端
  {
    path: '/admin',
    name: 'AdminView',
    component: () => import(/* webpackChunkName: "notfound" */ '@/views/AdminView'),
    children: [
      // 首页
      {
        path: 'index',
        name: 'AdminIndex',
        components: {
          adminTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/home/HomeContent')
        }
      },
      // 学生管理
      {
        path: 'stumanage',
        name: 'StudentManage',
        components: {
          adminTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/admin/StudentManage.vue')
        }
      },
      // 教师管理
      {
        path: 'teamanage',
        name: 'TeacherManage',
        components: {
          adminTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/admin/TeacherManage.vue')
        }
      },
    //  课程管理
      {
        path: 'coursemanage',
        name: 'CourseManage',
        components: {
          adminTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/admin/CourseManage.vue')
        }
      },
      // 专业管理
      {
        path: 'majormanage',
        name: 'MajorManage',
        components: {
          adminTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/admin/MajorManage.vue')
        }
      },
      // 账号管理
      // 账号管理
      {
        path: 'account/:role',
        name: 'StuAccount',
        components: {
          adminTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/admin/AccountManage.vue')
        }
      },
      // 个人信息
      {
        path: 'profile',
        name: 'AdminProfile',
        components: {
          adminTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/admin/AdminProfile.vue')
        }
      },
      // 修改密码
      {
        path: 'updatepwd',
        name: 'AdminUpdatePwd',
        components: {
          adminTable: () => import(/* webpackChunkName: "score" */ '@/components/main_content/admin/AdminUpdatePwd.vue')
        }
      }
    ]
  }
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
