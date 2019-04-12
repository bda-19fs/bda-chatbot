import unittest
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from use_cases.nlp.normalize_doc import normalize_doc
from use_cases.nlp.correct_grammar import correct_grammar
from use_cases.nlp.remove_stopwords import remove_stopwords
from use_cases.nlp.stemm_doc import stemm_doc
from use_cases.nlp.lemm_doc import lemm_doc


class TestNlpMethods(unittest.TestCase):
    def setUp(self):
        self.doc = [
            'ich kann die bilder in übungen nicht bearbeiten.',
            'lückentxte weg datenn verloren gegangen von pp 1.3.3 von rabatt',
            'bitte deaktivieren sie dieses gerät. vielen dank.'
        ]

        self.en_doc = [
            'I have a unit test up and running'
        ]

    def test_normalize_doc(self):
        normalized_doc = normalize_doc(self.doc)
        self.assertEqual(normalized_doc, [
            'ich kann die bilder in übungen nicht bearbeiten',
            'lückentxte weg datenn verloren gegangen von pp von rabatt',
            'bitte deaktivieren sie dieses gerät vielen dank'
        ])

    def test_correct_grammar(self):
        corrected_doc = correct_grammar(self.doc)
        self.assertEqual(corrected_doc, [
            'ich kann die bilder in übungen nicht bearbeiten.',
            'lückentexte weg daten verloren gegangen von pp 1.3.3 von rabatt',
            'bitte deaktivieren sie dieses gerät. vielen dank.'
        ])

    def test_remove_stopwords(self):
        cleaned_doc = remove_stopwords(self.doc)
        self.assertEqual(cleaned_doc, [
            'bilder übungen bearbeiten.',
            'lückentxte datenn verloren gegangen pp 1.3.3 rabatt',
            'bitte deaktivieren gerät. dank.'
        ])

    def test_stemming_de(self):
        stemmed_doc = stemm_doc(self.doc, 'de')
        self.assertEqual(stemmed_doc, [
            'ich kann die bild in ubung nicht bearbeiten.',
            'luckentxt weg datenn verlor gegang von pp 1.3.3 von rabatt',
            'bitt deaktivi sie dies gerat. viel dank.'
        ])

    def test_stemming_en(self):
        # would produce readable output if normalized first
        lemmed_doc = stemm_doc(self.en_doc, 'en')
        self.assertEqual(lemmed_doc, [
            'i have a unit test up and run'
        ])

    def test_lemming_de(self):
        lemmed_doc = lemm_doc(self.doc, 'de')
        self.assertEqual(lemmed_doc, [
            'ich können der bild in übung nicht bearbeiten.',
            'lückentxte weg datenn verlieren gehen von pp 1.3.3 von rabatt',
            'bitte deaktivieren ich dies geraten. viel danken.'
        ])

    def test_lemming_en(self):
        # would produce readable output if normalized first
        lemmed_doc = lemm_doc(self.en_doc, 'en')
        self.assertEqual(lemmed_doc, [
            'I have a unit test up and run'
        ])


if __name__ == '__main__':
    unittest.main()
