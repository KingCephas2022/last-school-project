from .utils import db

#from flask_restx import Namespace

#user_namespace = Namespace('score', description='name space for users')

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable = False, unique = True)
    password_hash = db.Column(db.String(),nullable = False)
    is_admin = db.Column(db.Boolean(), default=True)
    is_student = db.Column(db.Boolean(), default=False)

    user_type = db.Column(db.String(10))

    __mapper_args__ = {
        'polymorphic_on': user_type,
        'polymorphic_identity': 'user'
    }


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def __repr__(self) -> str:
        return self.email    