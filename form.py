from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class Registrationform(FlaskForm):
    name = StringField("fullname",validators=[DataRequired(message="we need your full name it can't be empty")])
    email= StringField("email",validators=[DataRequired(),Email(message="Email is required")])
    password=PasswordField("Password",validators=[DataRequired(message="password is must be 6 charactors "),Length(min=6)])
    submit=SubmitField("register")