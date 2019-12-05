from flask_restful import Resource, Api
from k_means import *
from utils_csv_reader import *
from json import *


class Root(Resource):
    def get(self):
        blog_data, blog_names = get_data()
        result = k_means(blog_data)
        named_list = elements_for_names(result, blog_names)

        return {'res': named_list}  # Fetches first column that is Employee ID
