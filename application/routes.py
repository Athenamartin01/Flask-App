from application import app, db
from application.models import *
from flask import render_template,request

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete')
def delete():
    first_game = Games.query.first()
    db.session.delete(first_game)
    db.session.commit()
    return('The first entry has been deleted')

@app.route('/count')
def count_():
    return(f'There are currently {Games.query.count()} games in the table.')

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/b')
def bonly():
    names = ["ben", "harry", "bob", "jay", "matt", "bill"]
    return render_template('b.html',names=names)

@app.route('/form', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        dob = form.dob.data
        fav_num = form.fav_num.data
        fav_food = form.fav_food.data
        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name}{last_name[0]}{fav_num}{fav_food}'

    return render_template('home.html', form=form, message=message)
