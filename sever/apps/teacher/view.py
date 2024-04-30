# 导入包
from flask import request, jsonify
# 导入模块
from apps import db
from apps.teacher import teacher_bp
from apps.teacher.model import Teacher
from apps.utils import sex_init


# 注册普通方法
# 获取全部教师信息
def get_all_teacher():
    # 获取学生信息
    stu_info = Teacher.query.all()
    data = []
    for i in stu_info:
        data.append(
            {
                'tea_id': i.teacher_id,
                'name': i.name,
                'sex': sex_init(i.sex),
                'address': i.address,
                'college': i.college,
            })
    # 返回学生信息
    return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 筛选教师信息
def get_teacher_info(user_id):
    # 查询数据库中是否存在数据
    tea_exist = Teacher.query.filter_by(teacher_id=user_id).first()
    # 打印查询结果
    if tea_exist is None:
        return jsonify({'code': 1, 'msg': '教师信息为空'})
    else:
        # 把性别由布尔值转换为中文
        if tea_exist.sex == 0:
            sex = '女'
        else:
            sex = '男'
        data = [
            {
                'tea_id': {'title': '教师编号', 'value': tea_exist.teacher_id},
                'name': {'title': '姓名', 'value': tea_exist.name},
                'sex': {'title': '性别', 'value': sex},
                'birthday': {'title': '出生日期', 'value': str(tea_exist.birthdays)}
            },
            {
                'address': {'title': '地址', 'value': tea_exist.address},
                'college': {'title': '学院', 'value': tea_exist.college}
            }

        ]
        return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 注册视图函数
# 获取教师信息
@teacher_bp.route('/get', methods=['GET', 'POST'])
def get_stu_info():
    if request.method == 'GET':
        data = get_all_teacher()
        return data
    else:
        user_id = request.form.get('user_id')
        data = get_teacher_info(user_id)
        return data


# 添加教师信息
@teacher_bp.route('/addteacher', methods=['POST'])
def add_teacher():
    pass


# 修改教师信息
@teacher_bp.route('/updateteacher', methods=['POST'])
def update_teacher():
    pass


# 删除教师信息
@teacher_bp.route('/deleteteacher', methods=['POST'])
def delete_teacher():
    pass
