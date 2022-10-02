# student_score

## 全栈练手小项目————成绩管理系统
### 设计软件： MasterGo
### UI： Element plus UI
### 前端 ： Vue cli3 + Vue-router + Vuex + axios + Chart.js
### 后端 ： python Flask
### 数据库： MySQL

## 仓库管理
- front-end 分支 前端代码
- back- end 分支 后端代码

## 前端 Vue Project setup
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

## 后端目录树
```
│  app.py   # 后端主程序
│  settings.py   # 后端配置文件
├─apps  
│  │  model.py   # 数据库模型创建
│  │  utils.py   # 工具函数
│  │  __init__.py   # flask初始化
│  │
│  ├─account    # 账户模块
│  │  │  model.py   # 账户模型创建
│  │  │  view.py    # 账户视图函数
│  │  │  __init__.py    # 账户蓝图注册
│  │  │
│  ├─admin  # 管理员模块
│  │  │  model.py   # 管理员模型创建
│  │  │  view.py    # 管理员视图函数
│  │  │  __init__.py    # 管理员蓝图注册
│  │  │
│  ├─course   # 课程模块
│  │  │  model.py   # 课程模型创建
│  │  │  view.py    # 课程视图函数
│  │  │  __init__.py    # 课程蓝图注册
│  │
│  ├─major  # 专业模块
│  │  │  model.py   # 专业模型创建
│  │  │  view.py    # 专业视图函数
│  │  │  __init__.py    # 专业蓝图注册
│  │
│  ├─score  # 成绩模块
│  │  │  model.py   # 成绩模型创建
│  │  │  view.py    # 成绩视图函数
│  │  │  __init__.py    # 成绩蓝图注册
│  │
│  ├─student    # 学生模块
│  │  │  model.py   # 学生模型创建
│  │  │  view.py    # 学生视图函数
│  │  │  __init__.py    # 学生蓝图注册
│  │
│  ├─teacher    # 教师模块
│  │  │  model.py   # 教师模型创建
│  │  │  view.py    # 教师视图函数
│  │  │  __init__.py    # 教师蓝图注册
│
├─static    # 静态文件
├─templates   # 模板文件


```
