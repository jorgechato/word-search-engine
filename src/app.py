from flask import Flask
from flask_restplus import Api

from api.controller import ns


app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title='Word search engine',
    description='The service will allow a user to search an specific word in an URL',
)

api.add_namespace(ns)

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000)
