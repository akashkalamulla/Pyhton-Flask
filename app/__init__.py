from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect

# Initialize the database
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    # Configuration
    app.config.from_pyfile('../config/config.py')

    # Initialize extensions (if any)
    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    login_manager.login_view = 'web.login'
    login_manager.login_message_category = 'info'

    from .models import discover_models
    discover_models()

    # from .models import User
    from .models.user import User
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Import the models so Alembic can detect them
    # from app import models

    # login_manager.init_app(app)

    # Import and register blueprints
    from .routes import web
    app.register_blueprint(web)

    from .middleware import restrict_access
    app.before_request(restrict_access)

    return app
