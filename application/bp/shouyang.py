from flask import Blueprint,request,url_for,redirect,json,abort
from flask_login import login_required,login_user

from ..models import db
from ..models.user import User

bp = Blueprint('shouyang',__name__)

# get info
@bp.route("/")
@login_required
def ha():
    return 'hello'