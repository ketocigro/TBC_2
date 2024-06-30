from flask_wtf import FlaskForm
from wtforms import StringField,  SelectField,  SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, NumberRange
from models import User

class AddItemForm(FlaskForm):
    category = SelectField('Category', choices=[('guitar', 'Guitar'), ('basses', 'Bass'), ('keyboard', 'Keyboard'), ('microphone', 'Microphone'), ('accessory', 'Accessory')], validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=0)])
    img = StringField('Image URL', validators=[DataRequired()])
    id = IntegerField('ID')
    submit = SubmitField('Add Item')



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already registered.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
