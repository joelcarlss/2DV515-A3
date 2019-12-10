from flask_restful import Resource, Api
from algorithm import run
from json import *


class Root(Resource):
    def get(self):
        words = ['java', 'programming']
        result = run(words)
        return {'res': result}  # Fetches first column that is Employee ID
