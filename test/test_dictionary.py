import unittest
from unittest.mock import patch
from game.dictionary import word_in_dictionary, DictionaryConnectionFailedException

class TestDictionary(unittest.TestCase):
    @patch('pyrae.dle.search_by_word')
    def test_word_in_dictionary(self, mock_search_by_word):
        word = "queso"
        mock_search_by_word.return_value.title = "queso | Definición | Diccionario de la lengua española | RAE - ASALE"
        self.assertEqual(word_in_dictionary(word), True)
        
    @patch('pyrae.dle.search_by_word')
    def test_word_not_in_dictionary(self, mock_search_by_word):
        word = "asdasdwadas"
        mock_search_by_word.return_value.title = "Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE"
        self.assertEqual(word_in_dictionary(word), False)
    
    @patch('pyrae.dle.search_by_word')
    def test_busqueda_fallo(self, mock_search_by_word):
        word = "auto"
        mock_search_by_word.return_value = None
        with self.assertRaises(DictionaryConnectionFailedException):
            word_in_dictionary(word)

if __name__ == '_main_':
    unittest.main()