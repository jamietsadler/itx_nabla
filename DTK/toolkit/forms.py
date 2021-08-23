from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class JSONForm(FlaskForm):
  json = StringField('json_string')
  submit = SubmitField('Save')
