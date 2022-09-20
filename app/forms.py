from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PokeFinderForm(FlaskForm):
    name = StringField('Poke Name', validators=[DataRequired()])
    submit = SubmitField()