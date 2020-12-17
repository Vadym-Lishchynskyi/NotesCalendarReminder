from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from NotesCalendarReminder import db, app, routes
from NotesCalendarReminder.models import Users, Tasks


####### Authorization ########
def login():
    mail = request.form.get('mail')
    password_ = request.form.get('password')

    if mail and password_:
        user = db.session.query(Users).filter_by(mail=mail).first()

        print(user.mail)
        if user:
            if check_password_hash(user.password, password_):
                login_user(user)

                next_page = request.args.get('next')
                print('you are logged in!')
                redirect('/')
                return render_template('main.html')
            else:
                flash('Password or email is incorrect')
    else:
        flash('Please fill mail and passwords fields')
        return render_template('login.html')


def register():
    mail = request.form.get('mail')
    password1 = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password1 or password2):
            flash('Please enter all the fields')
        elif password1 != password2:
            flash('Passwords are not equal')
        else:
            hash_pwd = generate_password_hash(password1)
            print(hash_pwd)
            print('you are registered!')
            new_user = Users(mail=mail, password=hash_pwd, name=None, surname=None)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login'))
    return render_template('register.html')


def logout():
    """Пока без выхода, потому что зачем!"""
    logout_user()

    return redirect(url_for('main'))


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login') + '?next=' + request.url)

    return response


######## General web-pages ########
def home():
    a = db.session.query(Tasks).all()
    print(type(a))
    for i in a:
        print(i.name)
    return render_template('for_everybody.html')


def new_task(user_mail):
    name = request.form.get('name')
    description = request.form.get('description')
    time_now = request.form.get('time_now')
    time_to_submit = request.form.get('time_to_submit')

    if request.method == 'POST':
        if not name:
            flash('Please enter name')
        if not description:
            description = None
        if not time_to_submit:
            time_to_submit = None

        new_task_ = Tasks(name=name, description=description, date_pub=time_now, date_to_submit=time_to_submit,
                          user_id=user_mail)

        db.session.add(new_task_)
        db.session.commit()

        return render_template('main.html')
    return render_template('new_task.html')
