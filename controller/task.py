from flask import Blueprint, render_template, url_for, redirect, session

import view.task as view_task
import view.organization as view_organization
import view.account as view_account

task_bp = Blueprint('task', __name__, url_prefix='/task')


@task_bp.route("/<id>")
def index(id):
    username = session.get('name')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    uid = session.get('uid')
    task = view_task.find_by_id(id)
    members = task.members
    return render_template('task/index.html', username=username, task=task, members=members, len=len(members))


@task_bp.route('/add')
def add():
    username = session.get('name')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    return render_template('task/add.html', username=username)