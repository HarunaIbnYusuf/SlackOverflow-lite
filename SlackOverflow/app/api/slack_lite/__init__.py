"""
endpoints linked in this file.

"""
from flask import Blueprint

from flask_restful import Api

from app.api.slack_lite.display_module import Query, Fetch


posts = Blueprint("posts", __name__)

api = Api(posts)

api.add_resource(Query, '/api/v1/questions')
api.add_resource(Fetch, '/api/v1/questions')

