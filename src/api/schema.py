from flask_restplus import fields
from flask_restplus import Model


query_schema = Model('Query', {
    'word': fields.String,
    'strict': fields.Boolean(default=True),
    'limiters': fields.List(fields.String(default=""))
})

response_schema = Model('Word', {
    '__this': fields.Url(absolute=True),
    'query': fields.Nested(query_schema),
    'source': fields.String,
    'found': fields.Boolean,
    'count': fields.Integer,
})

request_schema = Model('Search', {
    'query': fields.Nested(query_schema),
    'source': fields.String,
})
