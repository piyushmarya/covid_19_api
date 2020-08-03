import requests
from bs4 import BeautifulSoup

from utils.configparser import parser


def create_structure(table_row):
    """
    Creates a dictionary from the parameter data
    :param table_row: A html table row
    :return:
    """
    td_data_html = table_row.find_all('td')
    td = [i.get_text() for i in td_data_html]
    structure_dict = {td[1].lower().strip('\n').replace(" ", "_"): {
        "total": td[2],
        "new": td[3],
        "total_deaths": td[4].strip(),
        "new_deaths": td[5].strip(),
        "total_recovered": td[6],
        "active": td[7],
        "serious": td[8],
        "total_tested": td[11]
    }}
    return structure_dict


def scrape_continent_cases():
    """
    Scrapes all the total cases per continent.
    :return: Dictionary of total cases.
    """
    continent_dict = {}
    try:
        request_content = requests.get(parser.get('API', 'URL')).content
        html_parser = BeautifulSoup(request_content, "html.parser")
        table = html_parser.table
        continent_rows = table.find_all('tr', class_="total_row_world row_continent")
        for data in continent_rows[:6:]:
            dict_b = create_structure(data)
            continent_dict.update(dict_b)
        return continent_dict
    except Exception as err:
        return None


def scrape_total_cases():
    """
    Scrapes the webpage and finds cases of each country.
    :return: Dictionary of cases per country.
    """
    country_dict = {}
    try:
        request_content = requests.get(parser.get('API', 'URL')).content
        html_parser = BeautifulSoup(request_content, "html.parser")
        table = html_parser.table
        table_rows = table.find_all('tr')
        table_rows = table_rows[9::]
        for data in table_rows:
            dict_b = create_structure(data)
            country_dict.update(dict_b)
        return country_dict
    except Exception as err:
        return None
