import json


with open('player.json', 'r') as player:
    data = json.load(player)

with open('player.json', 'w') as player:

    data['level'] = data['level'] + 5
    data['gold'] = data['gold'] + 100

    json.dump(data, player, indent= 4)
