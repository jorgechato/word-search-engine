from flask import Flask
from flask_restplus import Api
from werkzeug.wsgi import DispatcherMiddleware
from prometheus_client import make_wsgi_app

from api.controller import ns
from metrics.controller import mns


app = Flask(__name__)

app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})

api = Api(
    app,
    version='1.0',
    title='Word search engine',
    description='The service will allow a user to search an specific word in an URL',
)

api.add_namespace(ns)
api.add_namespace(mns)

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000)
