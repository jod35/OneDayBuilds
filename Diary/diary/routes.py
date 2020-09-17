from diary import db,app
from flask import render_template,flash,redirect,url_for,request
from .forms import RegistrationForm,LoginForm,EventCreation
from .models.users import User
from .models.events import Event
from flask_login import login_user,logout_user,current_user,login_required

@app.route('/')
def index():
    context={
        'title':"Welcome"
    }
    return render_template('index.html',**context)


@app.route('/login',methods=['GET', 'POST'])
def sign_in():
    form=LoginForm()
    username=form.username.data

    password=form.password.data

    user=User.query.filter_by(username=username).first()

        

    if user and user.check_password(password):
        login_user(user,remember=form.remember_me.data)

        return redirect(url_for('add_event'))
    # else:
    #     flash("Invalid Login")


    context={
        'title':'Login',
        'form':form
    }
    return render_template('login.html',**context)


@app.route('/signup',methods=['GET', 'POST'])
def create_account():
    form = RegistrationForm()
    if request.method == 'POST':
        username=form.username.data
        email=form.email.data
        password=form.password.data
        confirm=form.confirm.data

        if password is not confirm:
            flash("Passwords do not much!")


        user=User.query.filter_by(username=username).first()


        if user is not None:
            flash("The user with username {} exists".format(username))

        new_user=User(username=username,email=email)

        new_user.set_password(password)

        new_user.create()

        flash("Account Created Successfully! You can now login")

        return redirect(url_for('sign_in'))


    context={
        'title':'Create Your Free Account',
        'form':form
    }
    return render_template('signup.html',**context)

@login_required
@app.route('/add_event',methods=['GET', 'POST'])
def add_event():

    
    
    form=EventCreation()
    if request.method == 'POST':
        name=form.name.data
        content=form.content.data

        new_event=Event(name=name,content=content)

        new_event.create()

        flash("Event added successfully")

        return redirect('/add_event')

    events=Event.query.all()
    context={
        'form':form,
        'events':events
    }
    return render_template('app.html',**context)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('sign_in'))
