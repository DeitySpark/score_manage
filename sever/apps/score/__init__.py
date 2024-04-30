from flask import Blueprint
from flask_cors import CORS

# 创建蓝图对象
score_bp = Blueprint('score', __name__, url_prefix='/score')
# 跨域
CORS(score_bp, supports_credentials=True)
