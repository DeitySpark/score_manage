export const Info = {
  
  staticHandle: [
    {
      title: "学生管理",
      path: '/admin/students'
    },
    {
      title: "教师管理",
      path: '/admin/teacher'
    },
    {
      title: "课程管理",
      path: '/admin/course'
    },
    {
      title: "专业管理",
      path: '/admin/major'
    },
    {
      title: "专业选课",
      path: '/admin/majcourse'
    }
  ],
  
  openalHandle: [
    {
      title: "账号管理",
      contain: [
        { title: '学生账号', path: '/admin/stuaccount' },
        { title: '教师账号', path: '/admin/teaaccount' },
        { title: '管理员账号', path: '/admin/adminaccount' }
      ]
    },
    {
      title: "个人中心",
      contain:
        [
          {title: '个人信息', path: '/admin/profile'},
          { title: '修改密码', path: '/admin/update'}
        ],
    }
  ]
}
