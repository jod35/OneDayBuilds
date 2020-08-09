from diary import db,app
from flask import render_template
from .forms import RegistrationForm,LoginForm,EventCreation

@app.route('/')
def index():
    context={
        'title':"Welcome"
    }
    return render_template('index.html',**context)


@app.route('/login')
def sign_in():
    form=LoginForm()
    context={
        'title':'Login',
        'form':form
    }
    return render_template('login.html',**context)


@app.route('/signup')
def create_account():
    form = RegistrationForm()
    context={
        'title':'Create Your Free Account',
        'form':form
    }
    return render_template('signup.html',**context)

@app.route('/add_event')
def add_event():
    pass