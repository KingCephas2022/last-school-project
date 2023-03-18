from flask import Flask
from flask_restx import Api
from .auth.view import auth_namespace 
from .courses import courses_namespace
from .conf.confi import config_dict
from .utils import db
from .courses import Course
from .scores import Score
from .user import User
from flask_migrate import Migrate



def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    migrate = Migrate(app, db)

    authorizations = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Add a JWT token to the header with ** Bearer &lt;JWT&gt; ** token to authorize"
        }
    }

    api = Api(app,  
        title='Student Management System API',
        description='using REST API service',
        authorizations=authorizations, 
        security='Bearer Auth'    )

    api.add_namespace(courses_namespace, path = '/courses')
    api.add_namespace(courses_namespace, path = '/students')
    api.add_namespace(auth_namespace, path = '/auth')

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'user': User,
            'Course': Course,
            'Score': Score,
        }
       
        return app

    