"""
Introdução ao módulo Unittest

Unittest -> Teste Unitários

O que são teste unitários?
Testes é a forma de se testar unidades individuais de código fonte.
Unidades individuais ser: função, métodos, classes, módulos etc.

#Obs: teste unitário não é específico da linguagem python
Para criar nossos testes, criamos classes que herdam de unittest. TestCase e a partir
de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

Por convenção todos os testes do test case deve ter o inicial como test_nome

#Para executar os testes com Unittest
python nome_modulo.py

# Para executar os testes com unittest no modo verbose
python nome_modulo.py -v

# Docstrings nos testes
Podemos acrescentar (é recomendado) docstrings nos testes.
"""

# Prática - Utilizando a abordagem TDD