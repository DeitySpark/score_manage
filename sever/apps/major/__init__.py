from flask import Blueprint
from flask_cors import CORS

# 创建蓝图对象
major_bp = Blueprint('major', __name__, url_prefix='/major')
# 跨域
CORS(major_bp, supports_credentials=True)
