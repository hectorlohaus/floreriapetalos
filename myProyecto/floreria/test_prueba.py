import unittest

from prueba import registro_usu

class TestProbar(unittest.TestCase):
    def test_Usu(self):
        self.assertTrue(registro_usu('Hector',123),True)
        self.assertTrue(registro_usu('Soul',112),False)
        self.assertFalse(registro_usu('Mendy',222),False)
 