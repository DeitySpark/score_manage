from apps import db


# 成绩模型类
class Score(db.Model):
    __tablename__ = 'Score'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stu_id = db.Column(db.Integer, db.ForeignKey('Student.stu_id'), nullable=False)
    stu_name = db.Column(db.String(50), nullable=False)
    college = db.Column(db.String(50), nullable=False)
    major = db.Column(db.String(50), nullable=False)
    course_name = db.Column(db.String(120), db.ForeignKey('Course.name'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

