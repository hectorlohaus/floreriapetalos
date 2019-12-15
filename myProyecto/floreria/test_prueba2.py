import unittest

from prueba2 import registro_flor

class TestProbar(unittest.TestCase):
    def testFlorcita(self):
        self.assertTrue(registro_flor('Lavanda',2995),True)
        self.assertTrue(registro_flor('Jacinto',3500),False)
        self.assertFalse(registro_flor('Lirio', 6000),False)
