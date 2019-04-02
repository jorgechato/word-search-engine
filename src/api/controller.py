from flask_restplus import Resource
from flask_restplus import Namespace
from flask_restplus import abort
from flask import request

from api.schema import response_schema
from api.schema import request_schema
from api.schema import query_schema

from utils.source import get_source
from utils.source import strict_search


ns = Namespace('', description='Simple word search engine')

ns.add_model('Word', response_schema)
ns.add_model('Query', query_schema)
ns.add_model('Search', request_schema)


@ns.route("/health")
class Health(Resource):
    def get(self, **kwargs):
        return {"alive": True}


@ns.route("/search")
class Search(Resource):
    @ns.doc(body=request_schema)
    @ns.expect(request_schema)
    @ns.marshal_with(response_schema, skip_none=True, code=200)
    def put(self, **kwargs):
        return {"strict": True}
