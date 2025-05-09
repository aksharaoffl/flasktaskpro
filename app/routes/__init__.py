from flask import Blueprint
from .auth import auth_bp
from .task import task_bp


def register_routes(app):
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(task_bp, url_prefix='/api/tasks')