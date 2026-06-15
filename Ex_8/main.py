import json

with open('players.json', 'r') as players:
    data = json.load(players)

print(f'Level: {data['Eldrin']['level']}')