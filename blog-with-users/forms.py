from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    Email = StringField("Email", validators=[DataRequired(), Email()])
    Password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Register Me")

# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    Email = StringField("Email", validators=[DataRequired(), Email()])
    Password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField("Log Me In")

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField("Write your Comment", validators=[DataRequired()])
    submit = SubmitField("Comment")