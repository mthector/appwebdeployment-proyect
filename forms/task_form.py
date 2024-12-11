from wtforms import Form, SelectField, StringField, SubmitField, validators

class InstrumentForm(Form):
    name = StringField('Name', [validators.length(min=4, max=80), validators.DataRequired()])
    category_id = SelectField('Category', [validators.DataRequired()], choices=[], coerce=int)
    supplier_id = SelectField('Supplier', [validators.DataRequired()], choices=[], coerce=int)
    image = StringField('Image', [validators.length(min=4, max=500)])
    image_2 = StringField('Image 2', [validators.length(min=4, max=500)])
    submit = SubmitField('Save')
