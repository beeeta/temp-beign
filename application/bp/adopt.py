from flask import Blueprint,request,url_for,redirect,json,abort
from flask_login import login_required
from ..models import db
from ..models.pet import Pet

from ..models import db
from ..models.user import User

bp = Blueprint('shouyang',__name__)

# get shouyang list info
@bp.route("/index")
@login_required
def ha():
    return 'hello'