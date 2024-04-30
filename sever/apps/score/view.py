# 导入包
from flask import request, jsonify
# 导入模块
from apps import db
from apps.score import score_bp

# 导入模型类，方法
from apps.score.model import Score


# 注册视图函数
# 筛选成绩信息
@score_bp.route('/getscore', methods=['GET', 'POST'])
def get_score():
    stu_id = request.form.get('stu_id')
    stu_exist = Score.query.filter_by(stu_id=stu_id).all()
    print(stu_exist)
    if stu_exist is None:
        return jsonify({'code': 1, 'msg': '学生信息为空'})
    else:
        data = []
        for i in stu_exist:
            data.append({'stu_id': i.stu_id, 'stu_name': i.stu_name, 'course_name': i.course_name, 'score': i.score})

        return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 添加成绩
@score_bp.route('/addscore', methods=['POST'])
def add_score():
    pass


# 修改成绩
@score_bp.route('/updatescore', methods=['POST'])
def update_score():
    stu_id = request.form.get('stu_id')
    course = request.form.get('course')
    score = request.form.get('score')
    print(stu_id, course, score)
    stu_exist = Score.query.filter_by(stu_id=stu_id, course_name=course).first()
    if stu_exist is None:
        return jsonify({'code': 1, 'msg': '学生成绩为空'})
    else:
        stu_exist.score = score
        db.session.commit()
        return jsonify({'code': 200, 'msg': '修改成功'})


# 统计成绩
@score_bp.route('/countscore', methods=['GET', 'POST'])
def count_score():
    course_name = request.form.get('course_name')
    print(course_name)
    course_exist = Score.query.filter_by(course_name=course_name).all()
    print(course_exist)
    if len(course_exist) == 0:
        return jsonify({'code': 1, 'msg': '该课程没有成绩信息'})
    else:
        data = []
        for i in course_exist:
            data.append({'stu_id': i.stu_id, 'stu_name': i.stu_name, 'score': i.score})

        return jsonify({'code': 200, 'msg': '获取成功', 'data': data})


# 删除成绩
@score_bp.route('/deletescore', methods=['POST'])
def delete_score():
    pass
