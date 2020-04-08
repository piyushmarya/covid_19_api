import json
import requests
from bs4 import BeautifulSoup


class WorldModel():
    def __init__(self, data):
        self.data = data

    @classmethod
    def get_world_data(self):
        try:
            with open("database/covid_19.json") as fd:
                file = json.load(fd)
            return file["world"]
        except Exception as er:
            ## TODO:
            print(er)

    def save_world_data(self):
        try:
            with open("database/covid_19.json","w") as fd:
                json.dump(self.data,fd,indent = 4)
        except Exception as e:
            return False
        return True
