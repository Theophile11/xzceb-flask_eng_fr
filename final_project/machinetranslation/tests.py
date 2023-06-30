import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TestTranslation(unittest.TestCase):

    def test_french(self):
        self.assertEqual(englishToFrench('Hi'), 'Bonjour')

    def test_english(self):
        self.assertEqual(frenchToEnglish('Deux'), 'Two')

if __name__ == '__main__':
    unittest.main()