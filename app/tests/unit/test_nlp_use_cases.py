from os import linesep

from bda_core.use_cases.nlp.correct_grammar import (
    correct_grammar,
    correct_grammar_stream
)
from bda_core.use_cases.nlp.lemm_doc import (
    lemm_doc,
    lemm_doc_stream
)
from bda_core.use_cases.nlp.normalize_doc import (
    normalize_doc,
    normalize_json,
    normalize_doc_stream,
    normalize_json_stream
)
from bda_core.use_cases.nlp.remove_stopwords import (
    remove_stopwords,
    remove_stopwords_json,
    remove_stopwords_stream,
    remove_stopwords_json_stream
)
from bda_core.use_cases.nlp.stemm_doc import (
    stemm_doc,
    stemm_json,
    stemm_doc_stream
)

doc = [
    'ich kann die bilder in übungen nicht bearbeiten.',
    'lückentxte weg datenn verloren gegangen von pp 1.3.3 von rabatt',
    'bitte deaktivieren sie dieses gerät. vielen dank.'
]

en_doc = [
    'I have a unit test up and running'
]

en_doc_stream = str.join('\n', en_doc)


def test_normalize_doc():
    normalized_doc = normalize_doc(doc)
    assert normalized_doc == [
        'ich kann die bilder in übungen nicht bearbeiten',
        'lückentxte weg datenn verloren gegangen von pp von rabatt',
        'bitte deaktivieren sie dieses gerät vielen dank'
    ]


def test_normalize_json():
    test_json = {'name': 'Artikel ABC', "text": doc[0]}
    normalized_json = normalize_json(test_json, 'text')
    assert normalized_json == {
        'name': 'Artikel ABC',
        'text': 'ich kann die bilder in übungen nicht bearbeiten'
    }


def test_normalize_doc_stream():
    doc_stream = (line for line in doc)
    corrected_doc = []
    for line in normalize_doc_stream(doc_stream):
        corrected_doc.append(line)
    assert corrected_doc == [
        'ich kann die bilder in übungen nicht bearbeiten',
        'lückentxte weg datenn verloren gegangen von pp von rabatt',
        'bitte deaktivieren sie dieses gerät vielen dank'
    ]


def test_normalize_json_stream(capsys):
    test_json = [{'name': 'Artikel ABC', "text": doc[0]}]
    corrected_doc = normalize_json_stream(test_json)
    captured = capsys.readouterr()

    corrected_doc = '{"name": "Artikel ABC", "text": "ich kann die bilder in übungen nicht bearbeiten"}' + linesep
    assert captured.out == corrected_doc


def test_correct_grammar():
    corrected_doc = correct_grammar(doc)
    assert corrected_doc == [
        'ich kann die bilder in übungen nicht bearbeiten.',
        'lückentexte weg daten verloren gegangen von pp 1.3.3 von rabatt',
        'bitte deaktivieren sie dieses gerät. vielen dank.'
    ]


def test_correct_grammar_stream():
    corrected_doc = []
    doc_stream = (line for line in doc)
    for line in correct_grammar_stream(doc_stream):
        corrected_doc.append(line)
    assert corrected_doc == [
        'ich kann die bilder in übungen nicht bearbeiten.',
        'lückentexte weg daten verloren gegangen von pp 1.3.3 von rabatt',
        'bitte deaktivieren sie dieses gerät. vielen dank.'
    ]


def test_remove_stopwords():
    cleaned_doc = remove_stopwords(doc)
    assert cleaned_doc == [
        'bilder übungen bearbeiten.',
        'lückentxte datenn verloren gegangen pp 1.3.3 rabatt',
        'bitte deaktivieren gerät. dank.'
    ]


def test_remove_stopwords_stream():
    corrected_doc = []
    doc_stream = (line for line in doc)
    for line in remove_stopwords_stream(doc_stream):
        corrected_doc.append(line)
    assert corrected_doc == [
        'bilder übungen bearbeiten.',
        'lückentxte datenn verloren gegangen pp 1.3.3 rabatt',
        'bitte deaktivieren gerät. dank.'
    ]


def test_remove_stopwords_json():
    test_json = {'name': 'Artikel ABC', "text": doc[0]}
    cleaned_doc = remove_stopwords_json(test_json, 'text')
    assert cleaned_doc == {
        'name': 'Artikel ABC',
        'text': 'bilder übungen bearbeiten.'
    }


def test_remove_stopwords_json_stream(capsys):
    test_json = [{'name': 'Artikel ABC', "text": doc[0]}]
    corrected_doc = remove_stopwords_json_stream(test_json, text_key='text')
    captured = capsys.readouterr()

    corrected_doc = '{"name": "Artikel ABC", "text": "bilder übungen bearbeiten."}' + linesep
    assert captured.out == corrected_doc


def test_stemming_de():
    stemmed_doc = stemm_doc(doc, 'de')
    assert stemmed_doc == [
        'ich kann die bild in ubung nicht bearbeiten.',
        'luckentxt weg datenn verlor gegang von pp 1.3.3 von rabatt',
        'bitt deaktivi sie dies gerat. viel dank.'
    ]


def test_stemming_en():
    lemmed_doc = stemm_doc(en_doc, 'en')
    assert lemmed_doc == [
        'i have a unit test up and run'
    ]


def test_stemming_json_de():
    test_json = {'name': 'Artikel ABC', "text": doc[0]}
    stemmed_json = stemm_json(test_json, 'text', 'de')
    assert stemmed_json == {
        'name': 'Artikel ABC',
        'text': 'ich kann die bild in ubung nicht bearbeiten.'
    }


def test_stemming_json_en():
    test_json = {'name': 'Article ABC', "text": en_doc[0]}
    stemmed_json = stemm_json(test_json, 'text', 'en')
    assert stemmed_json == {
        'name': 'Article ABC',
        'text': 'i have a unit test up and run'
    }


def test_stemming_de_stream():
    doc_stream = (line for line in doc)
    corrected_doc = []
    for line in stemm_doc_stream(doc_stream, 'de'):
        corrected_doc.append(line)
    assert corrected_doc == [
        'ich kann die bild in ubung nicht bearbeiten.',
        'luckentxt weg datenn verlor gegang von pp 1.3.3 von rabatt',
        'bitt deaktivi sie dies gerat. viel dank.'
    ]


def test_stemming_en_stream():
    corrected_doc = []
    en_doc_stream = (line for line in en_doc)
    for line in stemm_doc_stream(en_doc_stream, 'en'):
        corrected_doc.append(line)
    assert corrected_doc == [
        'i have a unit test up and run'
    ]


def test_lemming_de():
    lemmed_doc = lemm_doc(doc, 'de')
    assert lemmed_doc == [
        'ich können der bild in übung nicht bearbeiten.',
        'lückentxte weg datenn verlieren gehen von pp 1.3.3 von rabatt',
        'bitte deaktivieren ich dies geraten. viel danken.'
    ]


def test_lemming_en():
    lemmed_doc = lemm_doc(en_doc, 'en')
    assert lemmed_doc == [
        'I have a unit test up and run'
    ]


def test_lemming_de_stream():
    corrected_doc = []
    doc_stream = (line for line in doc)
    for line in lemm_doc_stream(doc_stream, 'de'):
        corrected_doc.append(line)
    assert corrected_doc == [
        'ich können der bild in übung nicht bearbeiten.',
        'lückentxte weg datenn verlieren gehen von pp 1.3.3 von rabatt',
        'bitte deaktivieren ich dies geraten. viel danken.'
    ]
