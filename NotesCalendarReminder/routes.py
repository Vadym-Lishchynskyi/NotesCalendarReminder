from flask import render_template, redirect, request, url_for, session
from flask_login import login_required

from NotesCalendarReminder import app, funcs
from NotesCalendarReminder import db, manager
from NotesCalendarReminder.models import Users, Tasks


######## General web-pages ########
@app.route('/')
def home():
    return funcs.home()


@app.route('/new_task', methods=['POST', 'GET'])
@login_required
def new_task():
    user_id = session['_user_id']
    print(session)
    return funcs.new_task(user_id)


######## Authorization ########

@app.route('/login', methods=['POST', 'GET'])
def login():
    return funcs.login()


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    return funcs.logout()


@app.route('/register', methods=['POST', 'GET'])
def register():
    return funcs.register()


@manager.user_loader
def load_user(user_id):
    print(db.session.query(Users).get(user_id))
    return db.session.query(Users).get(user_id)


