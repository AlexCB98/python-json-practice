import json

try:
    with open('players.json', 'r') as players:
        data = json.load(players)

except FileNotFoundError:
    print('File not found')

except json.JSONDecodeError:
    print('File empty')

else:
    print('Player loaded successfully')

finally:
    print('Program finished')