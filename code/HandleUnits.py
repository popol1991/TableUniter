import collections
import json
import sys

nn = sys.argv[1]  # unit name
bu = sys.argv[2]  # unit base-unit

fout = open('power2.json', 'w')

with open('power.json') as json_file:
    data = json.load(json_file)
    collection_list = data['results']['collection1']
    l = len(collection_list)
    names = []
    multipliers = []
    for i in range(0, l):
        name = collection_list[i]['name']['text']
        names.append(name)

        num = collection_list[i]['multiplier']

        multiplier = float(num.replace(',', ''))
        multipliers.append(multiplier)

    a = collections.OrderedDict()

    a['name'] = nn
    a['base-unit'] = bu

    b = []     # for units

    for j in range(0, l):
        c = collections.OrderedDict()
        c['name'] = names[j]

        d = collections.OrderedDict()
        d['multiplier'] = multipliers[j]
        d['zero-point'] = 0

        c['in-base-unit'] = d

        b.append(c)

    a['units'] = b

    json.dump(a, fout, indent=4)


