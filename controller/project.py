from flask import Blueprint, render_template, url_for, redirect, session

import view.project as view_project
import view.account as view_account
import view.organization as view_organization

project_bp = Blueprint('project', __name__, url_prefix='/project')


@project_bp.route('/')
def index():
    username = session.get('name')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    uid = session.get('uid')
    projects = view_project.find_by_account_id(uid)
    length = 0
    if projects is not None:
        length = len(projects)
    return render_template('project/index.html', username=username, projects=projects, len=length)


@project_bp.route('/<id>/general')
def general(id):
    username = session.get('name')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    uid = session.get('uid')
    project = view_project.find_by_id(id)
    return render_template('project/detail/general.html', username=username, project=project)


@project_bp.route('/<id>/tasks')
def tasklist(id):
    username = session.get('username')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    project = view_project.find_by_id(id)
    tasks = project.tasks
    length = 0
    if tasks is not None:
        length = len(tasks)

    return render_template('project/detail/task-list.html', tasks=tasks, len=len(tasks))


@project_bp.route('/<id>/members')
def member(id):
    username = session.get('username')
    is_authenticated = session.get('is_authenticated')

    if not is_authenticated:
        return redirect(url_for('auth.login'))

    project = view_project.find_by_id(id)
    return render_template('project/detail/member.html', project=project)

