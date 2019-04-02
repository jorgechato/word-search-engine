from flask_restplus import Resource
from flask_restplus import Namespace
from flask_restplus import abort
from flask import request


ns = Namespace('', description='Simple word search engine')


@ns.route("/health")
class Health(Resource):
    def get(self, **kwargs):
        return {"alive": True}
