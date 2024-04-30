from flask import Blueprint
from flask_cors import CORS

# 创建蓝图对象
teacher_bp = Blueprint('teacher', __name__, url_prefix='/teacher')
# 跨域
CORS(teacher_bp, supports_credentials=True)
