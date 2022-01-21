

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from handlers.routes import configure_routes


app = Flask(__name__)
api = Api(app)
CORS(app)
configure_routes(api, app)
client = app.test_client()

def test_base_route():

    url = '/'

    response = client.get(url)

    assert response.status_code == 302

def test_api_route():

    url = '/api/'

    response = client.get(url)

    assert response.status_code == 200

def test_api_top_n_plants_route():

    url = '/api/top/plants/'

    response = client.get(url)

    assert response.status_code == 200  

def test_api_state_gen_all_route():

    url = '/api/state-gen/all/'

    response = client.get(url)

    assert response.status_code == 200

def test_api_state_filter_route():

    url = '/api/state-gen/filter/ak/'

    response = client.get(url)

    assert response.status_code == 200
