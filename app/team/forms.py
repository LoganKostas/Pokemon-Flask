from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app.forms import PokeFinderForm

class CreateTeamForm(FlaskForm):
    poke1 = StringField('Poke1', validators=[])
    poke2 = StringField('Poke2', validators=[])
    poke3 = StringField('Poke3', validators=[])
    poke4 = StringField('Poke4', validators=[])
    poke5 = StringField('Poke5', validators=[])
    poke6 = StringField('Poke6', validators=[])
    submit = SubmitField()


