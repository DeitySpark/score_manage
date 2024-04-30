# 导入模块
from apps import create_app

app = create_app()

if __name__ == '__main__':
    app.run(Debug=True, host='0.0.0.0', port=5000)
