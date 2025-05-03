from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, cors, celery
from app.routes import register_routes
from app.models import User, Task

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    # Register routes
    register_routes(app)

    return app

def create_celery_app(app=None):
    app = app or create_app()
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery