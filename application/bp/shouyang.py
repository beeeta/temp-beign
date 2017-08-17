from flask import Blueprint
from flask_login import login_required,login_user

from ..models.user import User

bp = Blueprint('shouyang',__name__)
user = User()

# login action
@bp.route("/login")
def login():
    login_user(user)
    print('login success')
    return 'login success'

# get info
@bp.route("/ha")
@login_required
def ha():
    return 'hello'