from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AddPetForm(FlaskForm):
    kind = StringField('username', validators=[DataRequired()])
    city = StringField('password', validators=[DataRequired()])
    link = StringField('email', validators=[DataRequired()])


