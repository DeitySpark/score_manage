class Config:
    username = 'root'
    password = '123456'
    host = 'localhost'
    port = 3306
    database = 'student_score'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        username, password, host, port, database)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False
    JSONIFY_MIMETYPE = "application/json;charset=utf-8"


class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
