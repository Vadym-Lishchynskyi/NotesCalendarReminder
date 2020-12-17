from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'secret!'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0204@localhost:3306/NotesCalendar'
db = SQLAlchemy(app)
manager = LoginManager(app)

from NotesCalendarReminder import funcs, models, routes, config

db.create_all()



