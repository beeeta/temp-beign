from flask import Blueprint
from flask_login import login_required,login_user

bp = Blueprint('shouyang',__name__)

# login action
@bp.route("/login")
def login():


# get info
@bp.route("/ha")
@login_required
def ha():
    return 'hello'