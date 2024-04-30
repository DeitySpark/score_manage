from flask import Blueprint
from flask_cors import CORS

# 创建蓝图对象
student_bp = Blueprint('student', __name__, url_prefix='/student')
# 跨域
CORS(student_bp, supports_credentials=True)
