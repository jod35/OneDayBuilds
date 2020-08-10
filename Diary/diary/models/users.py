from diary.utils.database import db
from diary.utils.logins import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),unique=True,nullable=True)
    email=db.Column(db.String(40),nullable=False)
    password=db.Column(db.Text)

    from ..models.events import Event 

    events=db.relationship('Event',backref='author',lazy=True)

    def set_password(self,password):
        self.password=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def create(self):
        db.session.add(self)
        db.session.commit()
