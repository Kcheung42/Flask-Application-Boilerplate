import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# instantiate the db
db = SQLAlchemy()

#Application Factory Pattern
def create_app():

    # instantiate the app
    app = Flask(__name__)
    api = Api(app)

    # set up config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    #register blueprints
    from project.api.app import app_blueprint
    app.register_blueprint(app_blueprint)

    @app.route('/')
    def index():
        return '<h1>Hello World!</h1>'

    return app
