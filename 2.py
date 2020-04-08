import json
d1 = {'item': 'item1', 'amount': 400}
dictionaries = [{'item': 'item1', 'amount': 400},
                {'item': 'item2', 'amount': 300},
                {'item': 'item1', 'amount': 750}]

diction = {'item1': 0, 'item2': 0}
for x in dictionaries:
    if x['item'] == 'item1':
        diction['item1'] += x['amount']
    elif x['item'] == 'item2':
        diction['item2'] += x['amount']

print(diction)
with open("file_2.json", "w") as write_file:
    json.dump(diction, write_file)
