from .bp.shouyang import bp
from .dec import login_manager

from flask import Flask

def create_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    app.register_blueprint(bp)
    return app
