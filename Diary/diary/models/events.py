from diary.utils.database import db

class Event(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(45),nullable=False)
    content=db.Column(db.Text)

    def __init__(self,name,content):
        self.name=name
        self.content=content

    def create(self):
        db.session.add(self)
        db.session.commit()
        