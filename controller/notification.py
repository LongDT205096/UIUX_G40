from flask import Blueprint, render_template, url_for, redirect, session

notification_bp = Blueprint('notification', __name__)


@notification_bp.route('/notifications')
def index():
    username = session.get('username')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('notification/index.html', username=username, active_notification='active')