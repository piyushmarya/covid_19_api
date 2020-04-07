import os
from flask import Flask
from flask_restful import Api

from resources.world import WorldResource
from resources.country import CountryResource,AllCountriesResource
app = Flask(__name__)
api = Api(app)

api.add_resource(WorldResource,'/total')
api.add_resource(CountryResource,'/country/<string:name>')
api.add_resource(AllCountriesResource,'/world')

if __name__ == "__main__":
    app.run(int(os.environ.get("PORT"), debug=True))
