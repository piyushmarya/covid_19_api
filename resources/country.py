import json
from flask_restful import Resource


class CountryResource(Resource):
    def get(self, name):
        with open("database/covid_19.json") as fd:
            country_data=json.load(fd)
        if country_data.get(name):
            return country_data[name],200
        else:
            return {"msg":"No Cases Yet"},404


class AllCountriesResource(Resource):
    def get(self):
        with open("database/covid_19.json")as fd:
            data = json.load(fd)
        data.pop("world")
        return data
