from flask import Blueprint, render_template, url_for, redirect, session

organization_bp = Blueprint('organization', __name__)


@organization_bp.route('/organization')
def index():
    username = session.get('username')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('organization/index.html', username=username, active_notification='active')