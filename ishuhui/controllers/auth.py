from flask import Blueprint, render_template, abort, current_app, flash, redirect, session, url_for
from flask import request
from flask_login import login_user, logout_user

from ..models.user import User

bp_auth = Blueprint('auth', __name__)


@bp_auth.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        request_token = request.form.get('_csrf_token')
        if not token or not request_token or token != request_token:
            abort(403)


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if current_app.config['USERNAME'] != username or current_app.config['PASSWORD'] != password:
            flash('Login failed!', 'danger')
            return redirect(request.url)
        else:
            login_user(User())
            flash('Login succeed!', 'success')
            return redirect(url_for('admin.mange'))
    abort(404)


@bp_auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect('/')



