# 导入包
from flask import request, jsonify
from flask_cors import CORS
# 导入模块
from apps import db
from apps.course import course_bp
from apps.course.model import Course
from apps.teacher.model import Teacher


# 定义方法
# 获取所有课程
def get_all_courses():
    courses = Course.query.all()
    data = [{
        'id': i.id,
        'name': i.name,
        'type': i.type,
        'teacher_name': i.teacher_name,
        'credit': i.credit,
        'start_time': str(i.start_time),
        'place': i.place,
        'hours': i.hours
    }for i in courses]
    return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 筛选课程信息
def get_course(tea_id):
    # 查询教师姓名
    tea_name = Teacher.query.filter_by(teacher_id=tea_id).first().name
    print(tea_name)
    # 查询数据库中是否存在数据
    tea_exist = Course.query.filter_by(teacher_name=tea_name).all()
    # 打印查询结果
    print(tea_exist)
    if tea_exist is None:
        return jsonify({'code': 1, 'msg': '课程信息为空'})
    else:
        data = []
        for i in tea_exist:
            data.append({'id': i.id, 'type': i.type, 'name': i.name,
                         'credit': i.credit, 'start_time': str(i.start_time),
                         'place': i.place, 'hours': i.hours})
        print(data)
        return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 注册视图函数
# 获取程信息
@course_bp.route('/get', methods=['GET', 'POST'])
def get_course():
    if request.method == 'GET':
        return get_all_courses()
    else:
        tea_id = request.form.get('tea_id')
        return get_course(tea_id)


# 添加课程
@course_bp.route('/addcourse', methods=['POST'])
def add_course():
    pass


# 删除课程
@course_bp.route('/deletecourse', methods=['POST'])
def delete_course():
    pass


# 修改课程信息
@course_bp.route('/updatecourse', methods=['POST'])
def update_course():
    pass
