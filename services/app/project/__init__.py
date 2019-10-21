import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# instantiate the db
db = SQLAlchemy()

#Application Factory Pattern
def create_app():

    app = Flask(__name__)

    api = Api(app)
    app_settings = os.getenv('APP_SETTINGS')

    @app.route('/')
    def index():
        return '<h1>Hello World!</h1>'

    return app
