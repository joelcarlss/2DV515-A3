from flask_restful import Resource, Api
from k_means import *
from utils_csv_reader import *
from json import *


class Root(Resource):
    def get(self):

        return {'res': 'hej'}  # Fetches first column that is Employee ID
