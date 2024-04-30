from flask import Blueprint
from flask_cors import CORS

# 创建蓝图对象
course_bp = Blueprint('course', __name__, url_prefix='/course')
# 跨域
CORS(course_bp, supports_credentials=True)
