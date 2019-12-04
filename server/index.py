from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from route import *

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Root, '/')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')

