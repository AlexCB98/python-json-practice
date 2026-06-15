import json


with open('players.json', 'r') as players:
    data = json.load(players)

try:
    print(data['health'])
except KeyError:
    print('Key not found')