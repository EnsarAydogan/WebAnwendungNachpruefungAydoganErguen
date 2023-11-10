#forms.py
from flask import flash
from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, HiddenField, SelectField, StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo


class CreateTodoForm(FlaskForm): #genutzt bei /todos/
    description = StringField(validators=[InputRequired(), Length(min=3)])
    user_id = HiddenField()
    submit = SubmitField('Create')

class TodoForm(FlaskForm): #genutzt bei /todos/1
    method = HiddenField()
    id = HiddenField()
    user_id = HiddenField()
    complete = BooleanField()
    description = StringField(validators=[InputRequired()])
    list_id = SelectField(coerce=int, choices=[], validate_choice=False)
    submit = SubmitField('Update')

class CreateListForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(min=3)])
    user_id = HiddenField() 
    submit = SubmitField('Create')


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        from db import User
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            #Mirkan 2.
            flash('That username already exists. Please choose a different one.', 'danger')
            raise ValidationError('Username already exists.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


    
#Mirkan 4.
class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[InputRequired()])
    new_password = PasswordField('New Password', validators=[InputRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('Confirm New Password', validators=[InputRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')