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

    values = csv_handler.extract(file, col, out, enc, sep)
    pickle_handler.dump(values, out)

    click.echo(f'\nextracted {len(values)} of lines -> {out}')
    click.echo('extraction complete!\n')


@cli.command('pipeline_stemming')
@click.option(
    '-f', '--file', type=click.STRING, default='extract.p',
    help='extract file to use in process (default is "extract.p")'
)
@click.option(
    '-o', '--out', type=click.STRING, default='pipeline_stemming.p',
    help='output file for pipeline (default is "pipeline_stemming.p")'
)
@click.option(
    '-s', '--stopwords', type=click.STRING, default='res/custom_ch_stopwords.p',
    help='stopwords file in pipeline (default is "res/custom_ch_stopwords.p")'
)
def pipeline(file, out, stopwords):
    doc = pickle_handler.load(file)
    normalized_doc = nlp_methods.normalize_doc(doc)
    click.echo(f'- normalized {len(normalized_doc)} sentences')

    tokenized_doc = nlp_methods.tokenize_doc(normalized_doc)
    click.echo(f'- tokenized {len(tokenized_doc)} sentences')

    stopwords = pickle_handler.load(stopwords)
    cleaned_doc = nlp_methods.remove_stopwords_doc(tokenized_doc, stopwords)
    click.echo(f'- removed stopwords from {len(cleaned_doc)} sentences')


if __name__ == '__main__':
    cli()
