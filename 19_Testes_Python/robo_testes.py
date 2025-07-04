import unittest

from robo import Robo

class TestRobo(unittest.TestCase):

    def setUp(self):
        self.megamen = Robo('Mega men', bateria = 50)
        print('Inicio de Test sendo executado')

    def teste_carregar(self):
        self.megamen.carregar()
        self.assertEqual(self.megamen.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megamen.dizer_nome(), 'Beep Boop. Eu sou o MEGA MEN')
        self.assertEqual(self.megamen.bateria, 49, 'A bateria deveria estar em 49%')

    def tearDown(self):
        print('Final de test sendo executado!')

if __name__ == '__main__':
    unittest.main()