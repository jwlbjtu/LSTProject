from flask_wtf import Form
from wtforms import StringField, SubmitField # form fields like <input> in HTML
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')