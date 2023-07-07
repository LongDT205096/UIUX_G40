class AppConfig:
    DEBUG = False
    SECRET_KEY = '20200563'


class DatabaseConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql://uiux:admin@localhost:5435/uiux'