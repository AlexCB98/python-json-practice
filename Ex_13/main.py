import json

with open('players.json', 'r') as players:
    data = json.load(players)

cont = 0

for name in data:
    cont += 1
    print(f'Player_{cont}: {name}')