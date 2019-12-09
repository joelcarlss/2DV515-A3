from flask_restful import Resource, Api
from algorithm import run
from json import *


class Root(Resource):
    def get(self):
        # run()
        return {'res': 'hej'}  # Fetches first column that is Employee ID
