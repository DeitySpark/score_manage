# 导入包
from flask import request, jsonify
# 导入模块
from apps import db
from apps.student import student_bp
from apps.student.model import Student
from apps.account.model import Account

# 导入方法
from apps.utils import sex_init


# 定义方法函数
# 获取全部学生信息
def get_all_student():
    # 获取学生信息
    stu_info = Student.query.all()
    data = []
    for i in stu_info:
        data.append(
            {
                'stu_id': i.stu_id,
                'name': i.name,
                'sex': sex_init(i.sex),
                'username': i.username,
                'address': i.address,
                'college': i.college,
                'major': i.major,
                'credits': i.credits,
            })
    # 返回学生信息
    return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 筛选学生信息
def get_student_info(username):
    # 查询数据库中是否存在数据
    stu_exist = Student.query.filter_by(username=username).first()
    # 打印查询结果
    print(stu_exist)
    if stu_exist is None:
        return jsonify({'code': 1, 'msg': '学生信息为空'})
    else:
        data = [
            {
                'stu_id': {'title': '学号', 'value': stu_exist.stu_id},
                'name': {'title': '姓名', 'value': stu_exist.name},
                'sex': {'title': '性别', 'value': sex_init(stu_exist.sex)},
                'birthday': {'title': '出生日期', 'value': str(stu_exist.birth_date)}
            },
            {
                'address': {'title': '地址', 'value': stu_exist.address},
                'college': {'title': '学院', 'value': stu_exist.college},
                'major': {'title': '专业', 'value': stu_exist.major},
                'credits': {'title': '学分', 'value': stu_exist.credits},
                'GPA': {'title': '绩点', 'value': stu_exist.GPA}
            }

        ]
        return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 注册视图函数
# 获取学生信息
@student_bp.route('/get', methods=['GET', 'POST'])
def get_stu_info():
    if request.method == 'GET':
        data = get_all_student()
        return data
    else:
        username = request.form.get('username')
        data = get_student_info(username)
        return data


# 修改学生信息
@student_bp.route('/update', methods=['POST'])
def update_info():
    stu_id = request.form.get('stu_id')
    user_exist = Student.query.filter_by(stu_id=stu_id).first()
    if user_exist is None:
        return jsonify({'code': 1, 'msg': '用户不存在'})
    else:
        # 修改用户某条信息
        for item in request.form:
            if item == 'username':
                continue
            else:
                setattr(user_exist, item, request.form.get(item))
        db.session.commit()
        return jsonify({'code': 200, 'msg': '修改成功', 'data': user_exist})


# 添加学生信息
@student_bp.route('/add', methods=['POST'])
def add_info(sex=None):
    stu_id = request.form.get('stu_id')
    user_exist = Student.query.filter_by(stu_id=stu_id).first()
    if user_exist:
        return jsonify({'code': 1, 'msg': '用户已存在'})
    else:
        # 创建数据映射到数据库
        stu = Student(
            stu_id=stu_id,
            username=request.form.get('username'),
            name=request.form.get('name'),
            sex=sex_init(sex),
            birth_date=request.form.get('birth_date'),
            address=request.form.get('address'),
            college=request.form.get('college'),
            major=request.form.get('major'),
            credits=request.form.get('credits'),
            GPA=request.form.get('GPA')
        )
        db.session.add(stu)
        db.session.commit()
        return jsonify({'code': 200, 'msg': '添加成功', 'data': stu})


# 删除学生信息
@student_bp.route('/delete', methods=['POST'])
def delete_info():
    stu_id = request.form.get('stu_id')
    user_exist = Student.query.filter_by(stu_id=stu_id).first()
    if user_exist is None:
        return jsonify({'code': 1, 'msg': '用户不存在'})
    else:
        db.session.delete(user_exist)
        db.session.commit()
        return jsonify({'code': 200, 'msg': '删除成功', 'data': user_exist})
