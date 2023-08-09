from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,SelectField,DateField

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

class BasicForm(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    dob = DateField('DOB: ')
    fav_num = IntegerField('Favourite Number: ')
    fav_food = SelectField('Favourite Food: ', choices=[
        ('Pizza','Pizza'),
        ('Spaghetti','Spaghetti'),
        ('Chilli','Chilli')])
    submit = SubmitField('Add Name')