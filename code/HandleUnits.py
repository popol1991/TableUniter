import collections
import json
import sys


nn = sys.argv[1]  # unit name
bu = sys.argv[2]  # unit base-unit
infile = sys.argv[3]   # input file
outfile = sys.argv[4]  # output file

fout = open(outfile, 'w')

with open(infile) as json_file:
    data = json.load(json_file)
    collection_list = data['results']['collection1']
    l = len(collection_list)
    names = []
    multipliers = []
    for i in range(0, l):
        name = collection_list[i]['name']['text']
        names.append(name)

        num = collection_list[i]['multiplier']
        if num == '':
            multiplier = -1
        else:
            num = num.replace(',', '')
            try:
                multiplier = float(num)
            except ValueError, e:
                print 'error'+ num + 'error'

        multipliers.append(multiplier)

    a = collections.OrderedDict()

    a['name'] = nn
    a['base-unit'] = bu

    b = []     # for units

    for j in range(0, l):
        c = collections.OrderedDict()
        c['name'] = names[j]

        d = collections.OrderedDict()
        if multipliers[j] != -1:
            d['multiplier'] = multipliers[j]
        d['zero-point'] = 0

        c['in-base-unit'] = d

        b.append(c)

    a['units'] = b

    json.dump(a, fout, indent=4, encoding="utf-8")


