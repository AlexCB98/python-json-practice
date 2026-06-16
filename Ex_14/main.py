import json

with open('players.json', 'r') as players:
    data = json.load(players)

name = input('Delete a player: ').title()

try:
    del data[name]
    print('Player deleted successfully!')

except KeyError:
    print('Player not found')

with open('players.json', 'w') as players:
    json.dump(data, players, indent= 4)