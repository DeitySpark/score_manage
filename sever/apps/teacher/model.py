from apps import db


# 教师信息模型类
class Teacher(db.Model):
    __tablename__ = 'Teacher'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('Account.user_id'), primary_key=True, nullable=True)
    name = db.Column(db.String(80), primary_key=True, nullable=False, unique=True)
    sex = db.Column(db.Boolean, nullable=False)
    birthdays = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    # 学院
    college = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'name: {}, sex: {}, college: {}'.format(self.name, self.sex, self.college)
