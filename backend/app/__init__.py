rom flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from .routes import auth, user, forum, thread, post, search, admin
    app.register_blueprint(auth.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(forum.bp)
    app.register_blueprint(thread.bp)
    app.register_blueprint(post.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(admin.bp)

    return app
