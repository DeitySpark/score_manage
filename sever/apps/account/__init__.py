from flask import Blueprint
from flask_cors import CORS

# 创建蓝图对象
account_bp = Blueprint('account', __name__, url_prefix='/account')
# 跨域
CORS(account_bp, supports_credentials=True)
