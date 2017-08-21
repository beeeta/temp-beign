from .bp.adopt import bp as sy
from .bp.auth import bp as auth
from .bp.auth import login_manager
from .models import db

from flask_wtf.csrf import CSRFProtect
from flask import Flask

def create_app():
    app = Flask(__name__,template_folder='templates')
    app.config['SECRET_KEY']='FFFFF'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/begin'

    login_manager.init_app(app)
    db.init_app(app)
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(sy,url_prefix='/adopt')
    return app

