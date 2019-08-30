import json

def create(json_input):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile,indent=4)



data = {}
data['student'] = []
data['student'].append({
    'name': 'karthik',
    'sem': '6',
    'from': 'GMIT'
})
data['student'].append({
    'name': 'Rahul',
    'sem': '6',
    'from': 'GMIT'
})
data['student'].append({
    'name': 'Spruthi',
    'sem': '6',
    'from': 'GMIT'
})

create(data)