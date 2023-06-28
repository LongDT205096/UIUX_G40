from flask import Blueprint, render_template, url_for, redirect, session

project_bp = Blueprint('project', __name__)


@project_bp.route('/projects')
def index():
    username = session.get('username')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('project/index.html', username=username)


@project_bp.route('/project/<id>')
def detail(id):
    username = session.get('username')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('project/detail.html', username=username, project_name='Pro')
