import json

with open('players.json', 'r') as players:
    data = json.load(players)

name = input('Name: ').title()

try:

    reward = data[name]['level'] * 50
    data[name]['gold'] += reward
    print(f'Reward claimed: {reward} gold ')
    print(f'{name} now has {data[name]['gold']} gold')

except KeyError:
    print('Player not found')


with open('players.json', 'w') as players:
    json.dump(data, players, indent= 4)