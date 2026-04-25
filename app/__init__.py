import os

from flask import Flask
from flask_login import LoginManager

from app.config import Config
from app.database.db import db
from app.models.user import User
from app.routes import register_routes
from app.services.auth_service import ensure_default_admin
from app.utils.formatters import money


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = "Faca login para acessar o sistema."


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    app.jinja_env.filters["money"] = money
    register_routes(app)

    with app.app_context():
        db.create_all()
        ensure_default_admin()

    return app
