from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import Required, Optional


class NagForm(Form):
    name = StringField('Name', validators=[Required()])
    frequency = IntegerField('Number of Days', validators=[Required()])
    message_to_send = TextAreaField("Message to Send", validators=[Optional()])
    submit = SubmitField('Submit')
