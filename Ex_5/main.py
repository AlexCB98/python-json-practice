import json


try:
    with open('players.json', 'r') as players:
        data = json.load(players)
except FileNotFoundError:
    print('File not found')