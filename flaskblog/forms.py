from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class RegistrationForm(FlaskForm):
	username = StringField("User Name", validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("E-mail",validators=[DataRequired(),Email()])
	password = PasswordField("Password",validators=[DataRequired()])
	confirm_password = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
	email = StringField("E-mail",validators=[DataRequired(),Email()])
	password = PasswordField("Password",validators=[DataRequired()])
	remember = BooleanField("Remember me")	
	submit = SubmitField("Login")