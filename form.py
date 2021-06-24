from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    url = StringField('Url', validators=[DataRequired()])
    submit = SubmitField('Shoot')