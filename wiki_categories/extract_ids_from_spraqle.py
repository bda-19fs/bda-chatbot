import json

data = None
with open('sparql_result.json', 'r') as f:
    data = json.load(f)

print(data['head'])

food_ids_list = data['results']['bindings']
ids = []

for doc in food_ids_list:
    current_id = doc['id']['value']
    ids.append(current_id)

print(len(ids))

f = open('article_ids.csv', 'w')
with f:
    for i in range(len(ids) -1):
        f.write(ids[i] + ',\n')
    f.write(ids[len(ids) -1] + '\n')
