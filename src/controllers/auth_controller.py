from models.User import User
from schemas.UserSchema import user_schema
from main import db
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for, flash
from main import bcrypt
from flask_login import login_user, current_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET'])
def main_page():
    return redirect(url_for('projects.project_index'))


@auth.route('/auth/register', methods=['POST'])
def auth_register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already in use. Please try another.')
        return redirect(url_for('auth.signup'))

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email already in use. Please try another.')
        return redirect(url_for('auth.signup'))

    user = User()
    user.username = username
    user.email = email
    user.password = bcrypt.generate_password_hash(password).decode('utf-8')

    db.session.add(user)
    db.session.commit()

    flash('You are now registered. Please sign in here')

    # return jsonify(user_schema.dump(user))
    return redirect(url_for('auth.login'))


@auth.route('/auth/login', methods=['POST'])
def auth_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        flash('Invalid Credentials')
        return redirect(url_for('auth.login'))

    login_user(user)
    # return jsonify(user_schema.dump(user))
    flash(f'Welcome {user.username}, you are now signed in')
    return redirect(url_for('projects.project_index'))


@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You are now signed out')
    return redirect(url_for('projects.project_index'))