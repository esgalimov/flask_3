from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    title = StringField('Job title', validators=[DataRequired()])
    team_leader = StringField('Team leader id', validators=[DataRequired()])
    work_size = StringField('Work size', validators=[DataRequired()])
    collaborators = StringField('collaborators')
    is_finished = BooleanField('Is Job finished?')
    submit = SubmitField('Sumbit')