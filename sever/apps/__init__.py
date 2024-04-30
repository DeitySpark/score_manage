# 导入包
from flask import Flask
from apps.model import db
import settings
from flask_cors import CORS

# 导入蓝图
from apps.account.view import account_bp
from apps.admin.view import admin_bp
from apps.course.view import course_bp
from apps.major.view import major_bp
from apps.teacher.view import teacher_bp
from apps.student.view import student_bp
from apps.score.view import score_bp

# 导入模型类
from apps.account.model import Account
from apps.student.model import Student
from apps.teacher.model import Teacher
from apps.admin.model import Admin
from apps.course.model import Course
from apps.major.model import Major




def create_app():
    # 创建app并配置
    app = Flask(__name__)
    app.config.from_object(settings.DevelopmentConfig)
    CORS(app, supports_credentials=True)
    # 创建数据库对象
    with app.app_context():
        # 初始化数据库
        db.init_app(app)
        # 创建数据库表
        db.create_all()

    # 注册蓝图
    app.register_blueprint(account_bp)
    app.register_blueprint(teacher_bp)
    app.register_blueprint(major_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(score_bp)

    return app
