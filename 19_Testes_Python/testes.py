import unittest

from atividades import comer, dormir

class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando retorno com comida saudavel."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando retorno com comida gostosa."""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza porque só se vive uma vez.'
        )

    def test_dormir_pouco(self):
        """ Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir 4 horas.'
        )

    def test_dormir_muito(self):
        """ Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Dormi pra caramba filho!.'
        )

if __name__ == '__main__':
    unittest.main()


