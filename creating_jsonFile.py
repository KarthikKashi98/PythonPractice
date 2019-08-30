import json
"""
this function will create the json file and dump the json input which is taken as a parameter.
param : json_input

"""


def create(json_input):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile,indent=4)


if __name__=='__main__':
    #creating a json input

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
# calling the create function
create(data)