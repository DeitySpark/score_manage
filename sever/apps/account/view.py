# 导入包
from flask import request, jsonify
# 导入模块
from apps import db
from apps.account import account_bp
from apps.account.model import Account
from apps.student.model import Student
from apps.teacher.model import Teacher
from apps.admin.model import Admin


# 账号管理
@account_bp.route('/get', methods=['GET', 'POST'])
def account_manage():
    # 获取参数
    role = request.form.get('role')
    print(role)
    # 查询数据
    account_info = Account.query.filter_by(role=role).all()
    # 返回数据
    data = []
    if role == 'student':
        for i in account_info:
            name = Student.query.filter_by(stu_id=i.user_id).first().name
            data.append({
                'id': i.user_id,
                'name': name,
                'username': i.username,
                'email': i.email,
            })
    elif role == 'teacher':
        for i in account_info:
            name = Teacher.query.filter_by(teacher_id=i.user_id).first().name
            data.append({
                'id': i.user_id,
                'name': name,
                'username': i.username,
                'email': i.email,
            })
    else:
        for i in account_info:
            name = Admin.query.filter_by(admin_id=i.user_id).first().name
            data.append({
                'id': i.user_id,
                'name': name,
                'username': i.username,
                'email': i.email,
            })
    print(data)
    return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 注册账号
@account_bp.route('/register/', methods=['POST', 'OPTIONS'])
def register():
    username = request.form.get('username')
    # 查询数据库中是否存在该用户
    user_exist = Account.query.filter_by(username=username).first()
    if user_exist:
        return jsonify({'code': 1, 'msg': '用户已存在'})
    else:
        password = request.form.get('password')
        email = request.form.get('email')
        user_id = request.form.get('user_id')
        role = request.form.get('role')
        # 创建用户对象映射到数据库
        user_info = Account(username=username, user_id=user_id, password=password, email=email, role=role)
        print('Account info: ', user_info)
        # 将用户对象添加到数据库
        db.session.add(user_info)
        db.session.commit()
        # 返回注册成功
        return jsonify({'code': 200, 'msg': '注册成功'})


# 登录
@account_bp.route('/login/', methods=['GET', 'POST', 'OPTIONS'])
def login():
    # 查询数据库中是否存在该用户
    username = request.form.get('username')
    account_exist = Account.query.filter_by(username=username).first()
    if account_exist is None:
        user_exist = Account.query.filter_by(user_id=username).first()
    else:
        user_exist = account_exist

    # 如果用户不存在
    print(user_exist)
    if user_exist is None:
        return jsonify({'code': 1, 'msg': '用户不存在'})
    else:
        password = request.form.get('password')
        # 如果密码不正确
        if user_exist.password != password:
            return jsonify({'code': 2, 'msg': '密码不正确'})
        else:
            data = {'token': 66, 'user_id': user_exist.user_id, 'username': user_exist.username,
                    'role': user_exist.role}
            return jsonify({'code': 200, 'msg': '登录成功', 'data': data})


# 修改帐号密码
@account_bp.route('/update/password', methods=['POST'])
def update_password():
    pass


# 修改帐户信息
@account_bp.route('/update/info', methods=['POST'])
def update_info():
    pass
