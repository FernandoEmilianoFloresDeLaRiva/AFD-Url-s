import unittest
from AFD import Automata
from validator_txt import ValidatorTxt
from leer_afd_txt import leer_automata_de_txt

class TestURLValidator(unittest.TestCase):

    def setUp(self):
        self.data = leer_automata_de_txt('automata.txt')
        self.validatorData = ValidatorTxt(self.data) 
        if self.validatorData.validar_existencia_alfabeto():
            self.validator = Automata(self.data)
        else:
            raise Exception('Define bien el automata')

    # Clase válida
    def test_valid_url_with_protocol(self):
        self.assertTrue(self.validator.validar_cadena('https://www.google.com'))
    
    def test_valid_url_without_protocol(self):
        self.assertTrue(self.validator.validar_cadena('http://www.example.com'))
    
    def test_valid_url_with_port_and_params(self):
        self.assertTrue(self.validator.validar_cadena('https://example.com/path'))

    # Clase inválida
    def test_invalid_protocol(self):
        self.assertFalse(self.validator.validar_cadena('htp://wrong'))
    
    def test_invalid_non_url_string(self):
        self.assertFalse(self.validator.validar_cadena('notAURL'))
    
    def test_invalid_url_with_special_characters(self):
        self.assertFalse(self.validator.validar_cadena('https://example?.com'))

    def test_empty_string(self):
        self.assertFalse(self.validator.validar_cadena(''))

    def test_url_with_spaces(self):
        self.assertFalse(self.validator.validar_cadena('https ://example.com'))

if __name__ == '__main__':
    unittest.main()
