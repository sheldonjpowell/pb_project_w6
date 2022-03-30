from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


# class SignUpForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')

class PhoneBook(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    phonenumber = StringField('Phonenumber', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Click To Add')
    