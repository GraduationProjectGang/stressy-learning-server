from flask import Flask, render_template, request, url_for
from flask_restx import Resource, Api
from model import Federated

app = Flask(__name__)
port = 5002
host = "127.0.0.1"

# TODO: federeated module import
federate_module = __import__()
api = Api(
    app,
    version='0.1',
    title="stressy-learning-server",
    description="",
    terms_url="/",
    contact="",
    license="MIT"
)

api.add_namespace(Federated, '/model')

if __name__ == '__main__':
    app.run(host=host, port=port)
