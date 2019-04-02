from flask_restplus import Resource
from flask_restplus import Namespace
from flask_restplus import abort
from flask import request

from api.schema import response_schema
from api.schema import request_schema
from api.schema import query_schema

from api.service import search

from metrics.prometheus import SEARCH_COUNTER
from metrics.prometheus import FLASK_REQUEST_LATENCY


ns = Namespace('', description='Simple word search engine')

ns.add_model('Word', response_schema)
ns.add_model('Query', query_schema)
ns.add_model('Search', request_schema)


@ns.route("/search")
class Search(Resource):
    @ns.doc(body=request_schema)
    @ns.expect(request_schema)
    @ns.marshal_with(response_schema, skip_none=True, code=200)
    @FLASK_REQUEST_LATENCY.time()
    def put(self, **kwargs):

        res = search(ns.payload)

        if res == None:
            return abort(404)

        SEARCH_COUNTER.inc()

        return res
