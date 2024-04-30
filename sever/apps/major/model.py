from apps import db


# 创建专业信息模型类
class Major(db.Model):
    __tablename__ = 'Major'
    major_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    major_college = db.Column(db.String(50), primary_key=True, nullable=False)
    major_name = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)

    def __repr__(self):
        return 'major_id: {}, major_college: {}, major_name: {}'.format(
            self.major_id, self.major_college, self.major_name)
