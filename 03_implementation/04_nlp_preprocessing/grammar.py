#!/usr/bin/env python3
import click
import time as watch
from lib.grammar_methods import correction_iterator
from lib.log_handler import log_info


@click.command()
@click.option(
    '-g', '--grammar', type=click.STRING, default="res/grammar.txt",
    help='use grammar file to correct words (default is "res/grammar.txt")'
)
def correct_grammar(grammar):
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'correcting with grammar: {grammar}')

    lines = 0
    for line in correction_iterator(doc, grammar):
        if line is None:
            break
        click.get_text_stream('stdout', 'utf-8').write(line + '\n')
        lines += 1

    log_info(f'corrected {lines} lines')
    log_info(f'correction completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    correct_grammar()
