from flask import Blueprint, render_template, flash, url_for, redirect, session

home_bp = Blueprint('home', __name__)


@home_bp.route('/')
def index():
    username = session.get('username')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('home/index.html', username=username)
