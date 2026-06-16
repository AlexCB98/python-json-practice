import json

with open('players.json', 'r') as players:
    data = json.load(players)

name = input('Name: ').title()

try:
    data[name]['gold'] += 100
    print('Reward claimed!')
    print(f'{name} now has {data[name]['gold']}')

except KeyError:
    print('Player not found.')

with open('players.json', 'w') as players:
    json.dump(data, players, indent= 4)