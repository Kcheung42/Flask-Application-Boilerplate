from flask_restful import Resource, Api
from flask import Blueprint


app_blueprint = Blueprint('app', __name__)
api = Api(app_blueprint)

class AppPings(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(AppPings, '/app/ping')
