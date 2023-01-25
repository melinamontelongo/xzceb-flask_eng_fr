import unittest
import sys
sys.path.append("..")
from machinetranslation.translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Yes"), "Oui")
        self.assertEqual(english_to_french("Thank you"), "Je vous remercie")
        self.assertIsNone(english_to_french(None))        #Checking for null input
        self.assertIsNotNone(french_to_english("Cat"))    #Checking for not null input
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Oui"), "Yes")
        self.assertEqual(french_to_english("Merci"), "Thank you")
        self.assertIsNone(french_to_english(None))        #Checking for null input
        self.assertIsNotNone(french_to_english("Chat"))   #Checking for not null input
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
