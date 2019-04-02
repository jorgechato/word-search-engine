from flask_restplus import Resource
from flask_restplus import Namespace


mns = Namespace('', description='Simple word search engine metrics')


@mns.route("/health")
class Health(Resource):
    def get(self, **kwargs):
        return {"alive": True}
