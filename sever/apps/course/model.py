from apps import db


# 课程模型类
class Course(db.Model):
    __tablename__ = 'Course'
    id = db.Column(db.Integer, unique=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(120), primary_key=True, nullable=False)
    type = db.Column(db.String(120), nullable=False)
    teacher_name = db.Column(db.String(50), db.ForeignKey('Teacher.name'), nullable=False)
    credit = db.Column(db.Float, nullable=False)
    start_time = db.Column(db.Date, nullable=False)
    place = db.Column(db.String(120), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
