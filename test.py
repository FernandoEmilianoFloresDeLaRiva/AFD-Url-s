import unittest
from url_validator_dfa import URLValidatorDFA 

class TestURLValidator(unittest.TestCase):

    def setUp(self):
        self.validator = URLValidatorDFA()

    # Clase válida
    def test_valid_url_with_protocol(self):
        self.assertTrue(self.validator.is_valid_url('https://www.google.com'))
    
    def test_valid_url_without_protocol(self):
        self.assertTrue(self.validator.is_valid_url('http://www.example.com'))
    
    def test_valid_url_with_port_and_params(self):
        self.assertTrue(self.validator.is_valid_url('https://example.com/path'))

    # Clase inválida
    def test_invalid_protocol(self):
        self.assertFalse(self.validator.is_valid_url('htp://wrong'))
    
    def test_invalid_non_url_string(self):
        self.assertFalse(self.validator.is_valid_url('notAURL'))
    
    def test_invalid_url_with_special_characters(self):
        self.assertFalse(self.validator.is_valid_url('https://example?.com'))

    def test_empty_string(self):
        self.assertFalse(self.validator.is_valid_url(''))

    def test_url_with_spaces(self):
        self.assertFalse(self.validator.is_valid_url('https ://example.com'))

if __name__ == '__main__':
    unittest.main()
