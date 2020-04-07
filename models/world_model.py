import json
import requests
from bs4 import BeautifulSoup


class WorldModel():
    main_dict={}

    @classmethod
    def get_world_data(self):
        with open("database/covid_19.json") as fd:
            file = json.load(fd)
        return file["world"]

    def save_world_data(self):
        request_content = requests.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?").content
        parser = BeautifulSoup(request_content, "html.parser")
        table = parser.find('table')
        table_rows = table.find_all('tr')
        table_rows.pop(0)
        for data in table_rows:
            dict_b = self.create_dict(data)
            self.main_dict.update(dict_b)
        self.main_dict.pop("total:")
        with open("database/covid_19.json","w") as fd:
            json.dump(self.main_dict,fd,indent=4)
        print(self.main_dict)

    def create_dict(self,data):
        td_data = data.find_all('td')
        td = [i.get_text() for i in td_data]
        dict_a = {td[0].lower():{
            "total":td[1],
            "new":td[2],
            "total_deaths":td[3].strip(),
            "new_deaths":td[4].strip(),
            "total_recovered":td[5],
            "active":td[6],
            "serious":td[7],
            "total_tested":td[10]
            }}
        return dict_a
