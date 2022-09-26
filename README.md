# student_score

## 全栈练手小项目————成绩管理系统
### 设计软件： MasterGo
### UI： Element plus UI
### 前端 ： Vue + Vue-router + Vuex + axios
### 后端 ： python Flask
### 数据库： MySQL

## 仓库管理
- front-end 分支 前端代码
- back- end 分支 后端代码

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## 后端路由地址
```
Map([<Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>,
 <Rule '/account/register/' (OPTIONS, POST) -> account.register>,
 <Rule '/account/login/' (GET, OPTIONS, POST, HEAD) -> account.login>,
 <Rule '/account/update/password' (OPTIONS, POST) -> account.update_password>,
 <Rule '/account/update/info' (OPTIONS, POST) -> account.update_info>,
 <Rule '/teacher/getallteacher' (GET, OPTIONS, POST, HEAD) -> teacher.get_all_teacher>,
 <Rule '/teacher/addteacher' (OPTIONS, POST) -> teacher.add_teacher>,
 <Rule '/teacher/updateteacher' (OPTIONS, POST) -> teacher.update_teacher>,
 <Rule '/teacher/deleteteacher' (OPTIONS, POST) -> teacher.delete_teacher>,
 <Rule '/major/getallmajor' (GET, OPTIONS, POST, HEAD) -> major.get_all_major>,
 <Rule '/major/getmajor' (GET, OPTIONS, POST, HEAD) -> major.get_major>,
 <Rule '/major/addmajor' (OPTIONS, POST) -> major.add_major>,
 <Rule '/major/deletemajor' (OPTIONS, POST) -> major.delete_major>,
 <Rule '/student/getinfo' (GET, OPTIONS, POST, HEAD) -> student.get_info>,
 <Rule '/student/update_info' (OPTIONS, POST) -> student.update_info>,
 <Rule '/student/add_info' (OPTIONS, POST) -> student.add_info>,
 <Rule '/student/delete_info' (OPTIONS, POST) -> student.delete_info>,
 <Rule '/admin/getalladmin' (GET, OPTIONS, POST, HEAD) -> admin.get_all_admin>,
 <Rule '/admin/addadmin' (OPTIONS, POST) -> admin.add_admin>,
 <Rule '/admin/deleteadmin' (OPTIONS, POST) -> admin.delete_admin>,
 <Rule '/admin/updateadmin' (OPTIONS, POST) -> admin.update_admin>,
 <Rule '/course/getallcourse' (GET, OPTIONS, POST, HEAD) -> course.get_all_course>,
 <Rule '/course/getcourse' (GET, OPTIONS, POST, HEAD) -> course.get_course>,
 <Rule '/course/addcourse' (OPTIONS, POST) -> course.add_course>,
 <Rule '/course/deletecourse' (OPTIONS, POST) -> course.delete_course>,
 <Rule '/course/updatecourse' (OPTIONS, POST) -> course.update_course>,
 <Rule '/score/getscore' (GET, OPTIONS, POST, HEAD) -> score.get_score>,
 <Rule '/score/addscore' (OPTIONS, POST) -> score.add_score>,
 <Rule '/score/updatescore' (OPTIONS, POST) -> score.update_score>,
 <Rule '/score/countscore' (GET, OPTIONS, POST, HEAD) -> score.count_score>,
 <Rule '/score/deletescore' (OPTIONS, POST) -> score.delete_score>])
```
