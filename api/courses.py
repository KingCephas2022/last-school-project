from .utils import db
from datetime import datetime
from flask_restx import Namespace

courses_namespace = Namespace('course', description='name space for course names')

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    course_code = db.Column(db.String(10), unique=True)
    credit_hours = db.Column(db.Integer, default=1) 
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
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