#!/usr/bin/env python
import click
import lib.csv_handler as csv_handler
import lib.pickle_handler as pickle_handler
import lib.nlp_methods as nlp_methods


@click.group()
def cli():
    pass


@cli.command('extract')
@click.option(
    '-f', '--file', type=click.STRING, required=True,
    help='csv file to export column from'
)
@click.option(
    '-c', '--col', type=click.INT, required=True,
    help='column number to export (starting at 0)'
)
@click.option(
    '-o', '--out', type=click.STRING, default='extract.p',
    help='output file for extract (default is "extract.p")'
)
@click.option(
    '-e', '--enc', type=click.STRING, default='utf-8',
    help='file encoding (default is "utf-8")'
)
@click.option(
    '-s', '--sep', type=click.STRING, default=',',
    help='column separator (default is ",")'
)
def extract(file, col, out, enc, sep):
    click.echo(f'extracting column {col} from {file}...\n')
    head, line_numbers = csv_handler.extract(file, col, out, enc, sep)

    click.echo(f'showing head of column {col}:')
    for i, value in enumerate(head):
        click.echo(f'[{i}]\t{value}')
    click.echo(f'\nextracted {line_numbers} of lines -> {out}')
    click.echo('extraction complete!\n')


@cli.command('pipeline')
@click.option(
    '-f', '--file', type=click.STRING, default='extract.p',
    help='extract file to use in process (default is "extract.p")'
)
def pipeline(file):
    doc = pickle_handler.load(file)
    normalized_doc = nlp_methods.normalize_doc(doc)
    print(normalized_doc)


if __name__ == '__main__':
    cli()
