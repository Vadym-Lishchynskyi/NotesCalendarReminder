# Flask_SQLAlchemy here and everything connected with DB

from flask_login import UserMixin

from NotesCalendarReminder import db


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    mail = db.Column(db.VARCHAR(100), primary_key=True)
    password = db.Column(db.VARCHAR(256))
    name = db.Column(db.VARCHAR(40))
    surname = db.Column(db.VARCHAR(40))

    def __init__(self, mail, password, name, surname):
        self.mail = mail
        self.password = password
        self.name = name
        self.surname = surname

    def get_id(self):
        return self.mail


class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(40))
    description = db.Column(db.TEXT)
    date_pub = db.Column(db.Date)
    date_to_submit = db.Column(db.DateTime)

    user_id = db.Column(db.VARCHAR(100), db.ForeignKey('users.mail'), nullable=False)
    user = db.relationship('Users', backref=db.backref('Tasks', lazy=True))

    def __init__(self, name, description, date_pub, date_to_submit, user_id):
        self.name = name
        self.description = description
        self.date_pub = date_pub
        self.date_to_submit = date_to_submit

        self.user_id = user_id
