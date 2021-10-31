import requests
from pprint import pprint

response = requests.get('https://swapi.dev/api/people/')
pprint(response.json().get['name'])
