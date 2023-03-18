from .utils import db
from datetime import datetime




class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.Integer, nullable=False)
    course = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime() , nullable=False , default=datetime.utcnow)



    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)