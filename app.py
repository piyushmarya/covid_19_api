import os
from flask import Flask
from flask_restful import Api

from resources.world import WorldResource
from resources.country import CountryResource,AllCountriesResource

app = Flask(__name__)
api = Api(app)

api.add_resource(WorldResource,'/total')
api.add_resource(CountryResource,'/country/<string:name>')
api.add_resource(AllCountriesResource,'/allcountry')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
