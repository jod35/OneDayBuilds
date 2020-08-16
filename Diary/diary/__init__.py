from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .utils.database import db
from .utils.logins import login_manager
from .models.events import Event
from .models.users import User


app=Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
login_manager.init_app(app)
migrate=Migrate(app,db)


#user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from . import routes

@app.shell_context_processor
def make_shell_context():
    return {
        'db':db,
        'User':User,
        'Event':Event             
    }