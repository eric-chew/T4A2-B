from models.User import User
from schemas.UserSchema import user_schema, users_schema
from main import db
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for
from main import bcrypt
from flask_login import login_user, current_user, logout_user, login_required

auth = Blueprint('auth', __name__, url_prefix = '/user')

@auth.route('/register', methods=['POST'])
def auth_register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user:
        return abort(400, description='A user with this username already exists')
    
    user = User.query.filter_by(email=email).first()
    if user:
        return abort(400, description='A user with this email already exists')

    user = User()
    user.username = username
    user.email = email
    user.password = bcrypt.generate_password_hash(password).decode('utf-8')

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))

@auth.route("/login", methods=["POST"])
def auth_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password): 
        return abort(401, description="Invalid Credentials")

    login_user(user)
    return jsonify(user_schema.dump(user))