from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, IntegerField, SubmitField
from wtforms.fields.core import BooleanField, SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Form for adding a new pet"""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )

    species = SelectField(
        "Species",
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)]
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)]
    )

    submit = SubmitField('Submit')


class EditPetForm(FlaskForm):
    """Form for editing an existing Pet"""

    photo_url = StringField(
        'Photo URL',
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)]
    )

    available = BooleanField("Available")

    submit = SubmitField('Submit')
