from flask import Flask

from config.app_config import Config
from view.home import home_bp
from view.auth import auth_bp
from view.message import message_bp


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(message_bp)


if __name__ == '__main__':
    app.run(debug=True)