from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from handlers.routes import configure_routes



app = Flask(__name__)

api = Api(app)

CORS(app)

configure_routes(api, app)




