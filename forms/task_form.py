import re
from wtforms import Form, SelectField, StringField, SubmitField, ValidationError, validators, PasswordField
from databases.db import User


class InstrumentForm(Form):
    name = StringField('Name', [validators.length(min=4, max=80), validators.DataRequired()])
    category_id = SelectField('Category', [validators.DataRequired()], choices=[], coerce=int)
    supplier_id = SelectField('Supplier', [validators.DataRequired()], choices=[], coerce=int)
    image = StringField('Image', [validators.length(min=4, max=500)])
    image_2 = StringField('Image 2', [validators.length(min=4, max=500)])
    submit = SubmitField('Save')
    submit_2 = SubmitField('Cancel')


class UserForm(Form):
    name = StringField('Name', [validators.length(min=4, max=80), validators.DataRequired()], render_kw={"placeholder": "Name "})
    password = PasswordField('Password', [validators.length(min=4, max=80), validators.DataRequired()], render_kw={"placeholder": "Password "})
    submit = SubmitField('Login')

class RegisterForm(Form):
    name = StringField('Name', [validators.length(min=4, max=80), validators.DataRequired()], render_kw={"placeholder": "Name "})
    password = PasswordField('Password', [validators.length(min=4, max=80), validators.DataRequired()], render_kw={"placeholder": "Password "})
    submit = SubmitField('Register')
    def validate_name(form, field):
        forbidden_chars = r'[%\s"\\\/]'
        if re.search(forbidden_chars, field.data):
            raise ValidationError('Username cannot contain %, spaces, quotes, backslashes, or slashes.')

        existing_user_username = User.query.filter_by(name=field.data).first()
        if existing_user_username:
            raise ValidationError('That username already exists. Please choose a different one.')
    