import json

with open('player.json', 'r') as player:
    data = json.load(player)

name = data['name']
level = data['level']
gold = data['gold']

print(f'Name: {name}\n'
      f'Level: {level}\n'
      f'Gold: {gold}')