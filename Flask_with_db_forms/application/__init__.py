from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #create a flask app object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" #add a db to the app object
app.config['SECRET_KEY'] = 'Secret_Key' # add a secret key to acces forms

db = SQLAlchemy(app) #create the db as an object

from application import routes