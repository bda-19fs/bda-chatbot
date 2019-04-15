import click
from entities.file.reader import file_as_list
from entities.wiki.json_reader import from_str_to_json


def extract_text_from_article_stream(doc):
    doc = list(filter(lambda x: x != '', doc.split('\n')))
    print(doc)
    for line in doc:
        json_data = from_str_to_json(line)
        article_text = json_data['text']
        click.get_text_stream('stdout', 'utf-8').write(article_text + '\n')
