from flask import Blueprint,request,url_for,redirect,json,abort,render_template,make_response
from flask_login import login_required,login_user,logout_user,LoginManager

from ..models import db
from ..models.user import User
from ..forms.login_form import LoginForm
from ..forms.register_form import RegisterForm

bp = Blueprint('auth',__name__)

login_manager = LoginManager()

# login action
@bp.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('pages/login.html')
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                # 这里的密码如何校验？？
                login_user(user)
                # 登录成功
                return make_response(render_template('pages/index.html'),200)
        return redirect(url_for('auth.login'))

@bp.route('/logout')
def logout():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    logout_user(user)
    return redirect(url_for('auth.login'))

@bp.route("/register",methods=['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('pages/register.html')
    else:
        reg_form = RegisterForm()
        if reg_form.validate_on_submit():
            user = User(reg_form.username.data,reg_form.password.data,reg_form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        return redirect(url_for('auth.register'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id)