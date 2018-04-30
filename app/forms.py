from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CoderForm(FlaskForm):
    text_data = StringField("text_data", validators=[DataRequired()])
    coders = StringField("coders", validators=[DataRequired()])


class MelodyEscapeHelperForm(FlaskForm):
    image = FileField("image", validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

