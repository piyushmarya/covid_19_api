from flask_restful import Resource
from models.scraper import scrape_continent_cases, scrape_total_cases


class ContinentResource(Resource):

    def get(self):
        continent_cases_dict = scrape_continent_cases()
        if continent_cases_dict:
            return continent_cases_dict, 200
        return {"message": "Internal Server Error"}, 501


class CountryResource(Resource):

    def get(self):
        country_cases_dict = scrape_total_cases()
        if country_cases_dict:
            return country_cases_dict, 200
        return {"message": "Internal Server Error"}, 501
