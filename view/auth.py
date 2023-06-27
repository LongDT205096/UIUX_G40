from flask import Blueprint, render_template, request, session, redirect, url_for
import time

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')

        if username == 'group40_uiux@gmail.com' and password == 'admin':
            session['username'] = username
            session['is_authenticated'] = True

            time.sleep(1)
            return redirect(url_for('home.index'))

    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('is_authenticated', None)

    time.sleep(1)
    return redirect(url_for('auth.login'))
