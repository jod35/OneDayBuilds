from flask_wtf import FlaskForm
from wtforms import TextAreaField,PasswordField,StringField,BooleanField
from wtforms.validators import DataRequired,EqualTo

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('confirm')])
    confirm=PasswordField('Confirm Password',validators=[DataRequired()])


    
class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('confirm')])
    remember_me=BooleanField('Keep Me Logged In')

class EventCreation(FlaskForm):
    name=StringField('What You did',validators=[DataRequired()])
    content=TextAreaField('Explain It',validators=[DataRequired()])
   
