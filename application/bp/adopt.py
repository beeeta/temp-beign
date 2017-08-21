from flask import Blueprint,request,url_for,redirect,json,abort
from flask_login import login_required

from ..models import db
from ..models.pet import Pet
from ..models.user import User

from ..forms.add_pet_form import AddPetForm

bp = Blueprint('shouyang',__name__)

# get shouyang list info
@bp.route("/index",methods=['GET'])
@login_required
def index():
    return Pet.query.all()

# get shouyang list info
@bp.route("/<id>",methods=['GET'])
@login_required
def detail(id):
    return Pet.query.get(id)

@bp.route("/add",methods=['POST'])
@login_required
def detail():
    form = AddPetForm()
    if form.validate_on_submit():
        pet = Pet(form.kind.data,form.city.data,form.link.data)
        db.session.add(pet)
        db.session.commit()
    return redirect(url_for('shouyang.index'))

@bp.route("/delete",methods=['POST'])
@login_required
def detail():
    id = request.args.id
    Pet.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('shouyang.index'))


