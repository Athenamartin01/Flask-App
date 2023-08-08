from application import app,db


with app.app_context():
    db.drop_all() #removes all the data from the databse
    db.create_all() #inserts all data into database