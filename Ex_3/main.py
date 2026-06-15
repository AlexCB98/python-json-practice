import json

with open('player.json', 'r') as player:
    data = json.load(player)

data['health'] = 100

with open('player.json', 'w') as player:
    json.dump(data, player, indent= 4)