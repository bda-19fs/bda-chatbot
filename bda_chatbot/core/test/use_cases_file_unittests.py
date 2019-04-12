import unittest
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from use_cases.file.extract_column import extract_column


class TestFileMethods(unittest.TestCase):
    def setUp(self):
        self.doc = [
            'ich,kann,die,bilder,in,übungen,nicht,bearbeiten',
            'lückentxte,weg,datenn,verloren,gegangen,von,pp,1.3.3,von,rabatt',
            'bitte,deaktivieren,sie,dieses,gerät.,vielen,dank.'
        ]

    def test_extract_column(self):
        normalized_doc = extract_column(self.doc, column=4, separator=',')
        self.assertEqual(normalized_doc, [
            'in',
            'gegangen',
            'gerät.'
        ])


if __name__ == '__main__':
    unittest.main()
