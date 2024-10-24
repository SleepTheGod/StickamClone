from flask import render_template, redirect, url_for, session, request, flash
from app import app, db, socketio
from app.models import User
from app.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, current_user, login_required
from flask_socketio import send, join_room, leave_room

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('profile', username=user.username))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('profile', username=user.username))
    return render_template('register.html', form=form)

@app.route('/profile/<username>')
@login_required
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/stream/<username>')
@login_required
def stream(username):
    return render_template('stream.html', username=username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@socketio.on('message')
def handleMessage(msg):
    send(msg, broadcast=True)

@socketio.on('join')
def handleJoin(room):
    join_room(room)

@socketio.on('leave')
def handleLeave(room):
    leave_room(room)
