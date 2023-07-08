from flask import Blueprint, render_template, request, session, redirect, url_for
import time

import view.account as view_account
import view.organization as view_organization
import view.task as view_task
import view.project as view_project

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')

        login_user = view_account.login(username=username, password=password)
        if login_user[0]:
            session['username'] = login_user[1]
            session['name'] = login_user[2]
            session['uid'] = login_user[3]

            session['is_authenticated'] = True

            time.sleep(1)
            return redirect(url_for('home.index'))

    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('name', None)
    session.pop('uid', None)
    session.pop('is_authenticated', None)

    time.sleep(1)
    return redirect(url_for('auth.login'))


@auth_bp.route('/profile')
def profile():
    username = session.get('username')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('auth/profile.html', username=username)
