#!/usr/bin/env python3
import click
import time as watch
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.nlp.correct_grammar import correct_grammar_stream


@click.command()
@click.option(
    '-g', '--grammar', type=click.STRING, default='res/custom_ch_grammar.txt',
    help='use grammar file to correct words (default is "res/custom_ch_grammar.txt")'
)
def grammar(grammar):
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').readlines()

    log_info(f'correcting with grammar: {grammar}')

    for i, line in enumerate(correct_grammar_stream(doc, grammar)):
        click.get_text_stream('stdout', 'utf-8').write(f'{line}')

    log_info(f'corrected {i+1} lines')
    log_info(f'correction completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    grammar()
