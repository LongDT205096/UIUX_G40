from flask import Flask

from config import AppConfig
from controller.home import home_bp
from controller.auth import auth_bp
from controller.project import project_bp
from controller.notification import notification_bp
from controller.task import task_bp
from controller.organization import organization_bp

app = Flask(__name__)
app.config.from_object(AppConfig)

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(project_bp)
app.register_blueprint(notification_bp)
app.register_blueprint(task_bp)
app.register_blueprint(organization_bp)
if __name__ == '__main__':
    app.run(debug=True, port='8090')
