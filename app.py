import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.world import ContinentResource, CountryResource
from resources.documentation import DocumentationResource
from utils.configparser import parser

app = Flask(__name__)

CORS(app)

app.config['SECRET_KEY'] = parser.get('API', 'SECRET_KEY')
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)

api.add_resource(DocumentationResource, "/")
api.add_resource(CountryResource, "/country/all")
api.add_resource(ContinentResource, "/continent/all")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
