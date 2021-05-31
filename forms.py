from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import validators
from wtforms.fields.core import BooleanField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    '''Form for adding a new furry little friend, or maybe a reptile friend too!'''

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Pet Species", validators=[InputRequired()])
    photo_url = StringField("Pet Photo (online link)", validators=[InputRequired(), URL()])
    age = IntegerField("Age", validators=[InputRequired()])
    notes = StringField("Pet Bio", validators=[Optional(), Optional()])
    available = BooleanField("Available?")

class EditPetForm(FlaskForm):
    '''Form for editing pet info'''

    photo_url = StringField("Pet Photo (online link)", validators = [InputRequired(), URL()])
    notes = StringField("Pet Bio", validators=[Optional(), Optional()])
    available = BooleanField("Available?")