"""
Traductor Unit Test
"""
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Testing unit for english_to_french function
    """
    def test_when_text_is_null(self):
        """
        If the text value is null then return is None
        """
        self.assertIsNone(english_to_french(""))

    def test_correct_traduction_en_fr(self):
        """
        If the text value is in english the return is in french
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("World"), "World")

class TestFrenchToEnglish(unittest.TestCase):
    """
    Testing unit for french_to_english function
    """
    def test_when_text_is_null(self):
        """
        If the text value is null then return is None
        """
        self.assertIsNone(french_to_english(""))

    def test_correct_traduction_fr_en(self):
        """
        If the text value is in french the return is in english
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Monde"), "Monde")

unittest.main()
