from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bcrypt_.sqlite"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)
    password = db.Column(db.String(30), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET','POST'])
def home():
    if request.form:
        person = Register(name=request.form.get("name"), password=bcrypt.generate_password_hash(request.form.get("password")))
        db.session.add(person)
        db.session.commit()
    registrees = Register.query.all()
    return render_template("root.html", registrees=registrees)

@app.route('/login', methods=['GET','POST'])
def login():
    access = False
    if request.form:
        login_obj = Register.query.filter_by(name=request.form.get('name')).first() 
        if bcrypt.check_password_hash(login_obj.password,request.form.get('password')):
            access = True
    registrees = Register.query.all()
    return render_template("login.html", registrees=registrees,access=access)

    

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')