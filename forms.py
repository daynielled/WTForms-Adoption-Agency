from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,IntegerField
from wtforms.validators import InputRequired, URL, Optional, NumberRange



class AddPetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species',choices=[("cat", "Cat"),("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes')


class EditPetForm(FlaskForm):
    """Form to edit pet details"""
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes')
    available = BooleanField("Available?")






