from flask_wtf import FlaskForm
from wtforms import (
    validators,
    StringField,
    PasswordField,
    BooleanField)
from app.user_app.models import User
        

class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Username"
        }
    )
    password = PasswordField(
        "Password",
        validators=[validators.DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Password"
        }
    )
    remember = BooleanField(
        "Remember Me ?")
