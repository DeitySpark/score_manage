from flask import Blueprint
from flask_cors import CORS

# 创建蓝图对象
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
# 跨域
CORS(admin_bp, supports_credentials=True)
