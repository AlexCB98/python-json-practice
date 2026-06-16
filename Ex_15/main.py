import json

with open('players.json', 'r') as players:
    data = json.load(players)

total_gold = 0
total_players = 0

for name in data:
    total_gold += data[name]['gold']
    total_players += 1

print(f'Total players: {total_players}')
print(f'Total gold: {total_gold}')