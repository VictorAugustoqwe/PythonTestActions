import unittest
from Fila import Fila

class CasosDeTesteFila(unittest.TestCase):

    def setUp(self):
        self.fila = Fila()

    def testInicioVazio(self):
        self.assertTrue(self.fila.vazio())

    def testEnfilerarDoisElementos(self):
        self.fila.enfilera(2)
        self.fila.enfilera(3)
        self.assertEqual(self.fila.elementos, [2,3])

    def testDesenfilera(self):
        self.fila.elementos = [2,3]
        self.assertEqual(self.fila.desenfilera(), 2)