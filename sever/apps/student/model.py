from apps import db


# 用户信息模型类
class Student(db.Model):
    __tablename__ = 'Student'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    stu_id = db.Column(db.Integer, db.ForeignKey('Account.user_id'), unique=True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    sex = db.Column(db.Boolean, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(80), nullable=False)
    college = db.Column(db.String(80), nullable=False)
    major = db.Column(db.String(80), nullable=False)
    credits = db.Column(db.Integer, nullable=False)
    GPA = db.Column(db.Float, nullable=False)   # 绩点

    def __repr__(self):
        return 'stu_id: {}, username: {}, name: {}, sex: {},'.format(
            self.stu_id, self.username, self.name, self.sex)
