from diary import db,app
from flask import render_template

@app.route('/')
def index():
    context={
        'title':"Welcome"
    }
    return render_template('index.html',**context)


@app.route('/login')
def sign_in():
    context={
        'title':'Login'
    }
    return render_template('login.html',**context)


@app.route('/signup')
def create_account():
    context={
        'title':'Create Your Free Account'
    }
    return render_template('signup.html',**context)

@app.route('/add_event')
def add_event():
    pass