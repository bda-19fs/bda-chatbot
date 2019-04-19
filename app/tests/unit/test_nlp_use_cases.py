from bda_core.use_cases.nlp.normalize_doc import normalize_doc
from bda_core.use_cases.nlp.normalize_doc import normalize_json
from bda_core.use_cases.nlp.correct_grammar import correct_grammar
from bda_core.use_cases.nlp.remove_stopwords import remove_stopwords
from bda_core.use_cases.nlp.remove_stopwords import remove_stopwords_json
from bda_core.use_cases.nlp.stemm_doc import stemm_doc
from bda_core.use_cases.nlp.stemm_doc import stemm_json
from bda_core.use_cases.nlp.lemm_doc import lemm_doc

doc = [
    'ich kann die bilder in übungen nicht bearbeiten.',
    'lückentxte weg datenn verloren gegangen von pp 1.3.3 von rabatt',
    'bitte deaktivieren sie dieses gerät. vielen dank.'
]

en_doc = [
    'I have a unit test up and running'
]

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

def test_correct_grammar():
    corrected_doc = correct_grammar(doc)
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

def test_remove_stopwords_json():
    test_json = {'name': 'Artikel ABC', "text": doc[0]}
    cleaned_doc = remove_stopwords_json(test_json, 'text')
    assert cleaned_doc == {
        'name':'Artikel ABC',
        'text':'bilder übungen bearbeiten.'
    }

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
    test_json = {'name':'Artikel ABC',"text":doc[0]}
    stemmed_json = stemm_json(test_json, 'text', 'de')
    assert stemmed_json == {
        'name':'Artikel ABC',
        'text':'ich kann die bild in ubung nicht bearbeiten.'
    }

def test_stemming_json_en():
    test_json = {'name':'Article ABC',"text":en_doc[0]}
    stemmed_json = stemm_json(test_json, 'text', 'en')
    assert stemmed_json == {
        'name':'Article ABC',
        'text':'i have a unit test up and run'
    }

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
