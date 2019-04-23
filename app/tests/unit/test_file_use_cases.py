import os
from os import linesep
from bda_core.use_cases.file.extract_column import (
    extract_column,
    extract_column_stream
)


def test_extract_column():
    doc = [
        'ich,kann,die,bilder,in,übungen,nicht,bearbeiten',
        'lückentxte,weg,datenn,verloren,gegangen,von,pp,1.3.3,von,rabatt',
        'bitte,deaktivieren,sie,dieses,gerät.,vielen,dank.'
    ]

    normalized_doc = extract_column(doc, column=4, separator=',')

    assert normalized_doc == [
        'in',
        'gegangen',
        'gerät.'
    ]

def test_extract_column_stream(capsys):
    csv = '''ich,kann,die,bilder,in,übungen,nicht,bearbeiten
        lückentxte,weg,datenn,verloren,gegangen,von,pp,1.3.3,von,rabatt
        bitte,deaktivieren,sie,dieses,gerät.,vielen,dank.'''

    extract_column_stream(csv, column=4, separator=',')

    captured = capsys.readouterr()
    assert captured.out == f'in{linesep}gegangen{linesep}gerät.{linesep}'
