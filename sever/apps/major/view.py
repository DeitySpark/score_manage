# 导入包
from flask import request, jsonify
# 导入模块

from apps.major.model import Major
from apps.major import major_bp


# 方法函数
def get_all_major():
    # 获取所有专业
    major_list = Major.query.all()
    # 返回结果
    data = [{
        'id': i.major_id,
        'college': i.major_college,
        'major': i.major_name,
    } for i in major_list]
    return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 注册视图函数
# 获取全部专业信息
@major_bp.route('/get', methods=['GET', 'POST'])
def get_major():
    if request.method == 'GET':
        return get_all_major()
    else:
        return 'Error'

# 添加专业
@major_bp.route('/addmajor', methods=['POST'])
def add_major():
    pass


# 删除专业
@major_bp.route('/deletemajor', methods=['POST'])
def delete_major():
    pass
