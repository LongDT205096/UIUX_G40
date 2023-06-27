from flask import Blueprint, render_template, flash, url_for, redirect, session

message_bp = Blueprint('message', __name__)


@message_bp.route('/messages')
def chat():
    return render_template('messages/message.html')