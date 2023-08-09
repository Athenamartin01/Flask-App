from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,SelectField,DateField

class Games(db.Model): #Creates a table for the database
    id = db.Column(db.Integer, primary_key=True) #creates a primary key
    name = db.Column(db.String(30)) 

class BasicForm(FlaskForm): #Creates a form
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    dob = DateField('DOB: ')
    fav_num = IntegerField('Favourite Number: ')
    fav_food = SelectField('Favourite Food: ', choices=[
        ('Pizza','Pizza'),
        ('Spaghetti','Spaghetti'),
        ('Chilli','Chilli')]) #the first item in tuple is stored value, the second is displayed to user
    submit = SubmitField('Add Name')