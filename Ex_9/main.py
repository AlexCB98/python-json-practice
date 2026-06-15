import json

with open('players.json', 'r') as players:
    data = json.load(players)

player_name = input('Player: ').title()

try:

    print(f'Level: {data[player_name]['level']}')
    print(f'Gold: {data[player_name]['gold']}')
    print(f'Health: {data[player_name]['health']}')

except KeyError:
    print('Player not found')