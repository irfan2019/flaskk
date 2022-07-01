from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class registrationform(FlaskForm):
	username=StringField("username",validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField("email",validators=[DataRequired(),Email()])
	password=PasswordField("password",validators=[DataRequired()])
	confirm_password=PasswordField("confirm_password",validators=[DataRequired(),EqualTo('password')])

	submit=SubmitField('sign up')

class loginform(FlaskForm):
	email=StringField("email",validators=[DataRequired(),Email()])
	password=PasswordField("password",validators=[DataRequired()])
	submit=SubmitField('sign up')