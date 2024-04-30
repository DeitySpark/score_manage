# 导入包
from flask import request, jsonify
# 导入模块
from apps import db
from apps.admin.model import Admin
from apps.admin import admin_bp


# 注册视图函数
#  获取全部管理员信息
@admin_bp.route('/getinfo', methods=['GET', 'POST'])
def get_all_admin():
    username = request.form.get('username')
    # 查询数据库中是否存在数据
    stu_exist = Admin.query.filter_by(username=username).first()
    # 打印查询结果
    print(stu_exist)
    if stu_exist is None:
        return jsonify({'code': 1, 'msg': '管理员信息为空'})
    else:
        data = [
            {
                'admin_id': {'title': '管理员编号', 'value': stu_exist.admin_id},
                'username': {'title': '昵称', 'value': stu_exist.username},
                'name': {'title': '姓名', 'value': stu_exist.name},
                'token': {'title': '令牌', 'value': stu_exist.admin_token},
            }

        ]
        return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 添加管理员
@admin_bp.route('/addadmin', methods=['POST'])
def add_admin():
    pass


# 删除管理员
@admin_bp.route('/deleteadmin', methods=['POST'])
def delete_admin():
    pass


# 修改管理员信息
@admin_bp.route('/updateadmin', methods=['POST'])
def update_admin():
    pass
