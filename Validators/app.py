from typing import Any
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField # We will only use StringField and SubmitField in our simple form.
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY']='SOME_KEY' #Configure a secret key for CSRF protection.


class UserCheck:
    def __init__(self, banned:list, message=None):# Here we set up the class to have the banned and message attributes. banned must be passed through at declaration.
        self.banned = banned
        if not message:
            message = 'Please choose another username' # If no message chosen, then this default message is returned.
        self.message = message

    def __call__(self, form, field):
    # Here we define the method that is ran when the class is called. If the data in our field is in the list of words then raise a ValidationError object with a message.
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)

class Special_Char_Check:
    def __init__(self,message=None):
        self.special = ['!','@','"',"'",'£','$','/','\\',',']
        if not message:
            message = f'Please Avoid using {self.special} in the username'
        self.message = message

    def __call__(self, form, field):
        if any(i in field.data for i in self.special):
            raise ValidationError(self.message) 

class myForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        UserCheck(message="That username is not allowed", banned = ['root','admin','sys']),
        Length(min=2,max=15),
        Special_Char_Check()
        ])
    submit = SubmitField('Sign up')    



@app.route('/', methods=['GET','POST'])
def postName():
    form = myForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('home.html', form = form, username=username)
    else:
        return render_template('home.html', form = form, username="")   

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')