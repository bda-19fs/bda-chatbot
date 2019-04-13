import csv

def read_article_ids(filepath):
    with open(filepath, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        return [int(row[0]) for row in reader]

def keep_article_by_id(id, ids_list):
    return id in ids_list
