from flask_restful import Resource, Api
from algorithm import run
import glob
from json import *


class Root(Resource):
    def get(self, query):
        words = query.split('+')
        result = run(words)
        return {'res': result}  # Fetches first column that is Employee ID


class Page(Resource):
    def get(self, link):
        link = link.replace('+', '/')
        link = './wikipedia/Words/' + link
        file = open(link, 'r').read()
        return {'res': file}  # Fetches first column that is Employee ID
