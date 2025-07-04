"""
Unittest - Antes e após hooks

------
Hooks - são os testes em si, Ou seja, a execução dos testes.
------

setup() -> é executado antes de cada mét0do de teste. É util para criarmos instancias de objetos e outros dados;

tearDown() -> é executado ao final de cada mét0do de teste. É útil para excluir dados ou fechar conexões com
banco de dados.
"""
import unittest

class ModoluTest(unittest.TestCase):
    def setUp(self):
        #Configurações do Setup()
        pass

    def test_primeiro(self):
        #Setup vai rodar antes do teste.
        #teardown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # Setup vai rodar antes do teste.
        # teardown() vai rodar após o teste.
        pass

    def tearDown(self):
        #configurações do tearDown()
        pass