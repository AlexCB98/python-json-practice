import json

with open('players.json', 'r') as players:
    data = json.load(players)

player_name = input('Player name: ').title()

try:
    print(f'Level: {data[player_name]['level']}')
    print(f'Gold: {data[player_name]['gold']}')
    print(f'Health: {data[player_name]['health']}')

except KeyError:
    print('Player not found')
    create_new = input('Create player ? [ y/n ]: ').lower()
    if create_new == 'y':
        data[player_name] = {
            'level': 1,
            'gold': 0,
            'health': 100
        }
        print('Player added successfully !')

with open('players.json', 'w') as players:
    json.dump(data, players, indent= 4)

