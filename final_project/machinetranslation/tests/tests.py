import unittest
import os, sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Yes"), "Oui")
        self.assertNotEqual(english_to_french("Thank you"), "Thank you")
        self.assertIsNone(english_to_french(None))        #Checking for null input
        self.assertIsNotNone(french_to_english("Cat"))    #Checking for not null input
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Oui"), "Yes")
        self.assertNotEqual(french_to_english("Merci"), "Merci")
        self.assertIsNone(french_to_english(None))        #Checking for null input
        self.assertIsNotNone(french_to_english("Chat"))   #Checking for not null input
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
