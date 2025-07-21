# 🐍 Curso de Python - Resumo Pessoal

Repositório com anotações e resumos que escrevi com minhas próprias palavras durante o curso de Python da Geek University. Organizado por módulos para facilitar revisões e consultas rápidas.

---

## 📌 Módulo 14 - Decoradores em Python

### 🔹 Funções de maior grandeza

Funções que retornam outras funções, nessa aula também aprendi sobre funções dentro de funções que podem acessar o recebimento de funções externas.

### 🔹 O que são decorators?

Decorators são funções que decoram outras funções, você cria uma função e pode "reescrever" ela passando outra de parâmetro apenas com `@funcao_quefoifeita`

### 🔹 Decoradores com diferentes assinaturas

Essa aula foi mais sobre decoradores de funções, porém com kwargs e recebendo mais parâmetros de entrada.

### 🔹 Preservando Metadata

Os metadatas são dados intrínsecos da própria função, porém quando temos uma função dentro de uma função, e pedimos os metadatas com `print(funcao.__name__)` ou `print(funcao.__doc__)`, ela acaba retornando sempre da primeira função e não da segunda. Basta adicionar `@wraps(funcao)`.

### 🔹 Forçando tipos de dados com um decorator

Você pode criar um decorator recebendo kwargs com vários tipos de parâmetros de entrada. Quando usar ele em alguma função, pode forçar tipos com `@decorator_tipo(str, int)` ou `@forca_tipo(float, float)`

✅ **Fim do módulo 14**

---

## 🧱 Módulo 15 - Orientação a Objetos com Python

### 🔹 O que é Orientação a Objetos?

POO é um paradigma de programação que utiliza o mapeamento de objetos do mundo real para modelos computacionais.

### 🔹 Classes

O POO contém classes (entidades) como parte de sua característica que representam objetos do mundo real, como carro, lâmpada etc.

Classes podem conter:

* **Atributos** = características (ex: tamanho, cor)
* **Métodos** = comportamentos (ex: andar, correr, acender)

### 🔹 Atributos

Atributos de instância são declarados dentro do método construtor.

### 🔹 Métodos

São funções dentro da classe. Existem métodos de instância e de classe.

### 🔹 Objetos

São instâncias criadas a partir de uma classe.

### 🔹 Abstração e Encapsulamento

Aprendendo a encapsular atributos de uma classe para que não sejam alterados ou visíveis por quem está fora da classe.

### 📌 Exemplo prático

* **Classe**: Lâmpada → define o que é uma lâmpada
* **Atributos**: cor, voltagem, marca
* **Métodos**: ligar(), desligar()
* **Objeto**: `lampada1`, `lampada2` → lâmpadas reais
* **Instância**: processo de criar os objetos → `lampada1 = Lâmpada(...)`

✅ **Fim do módulo 15**

---

## 🧬 Módulo 16 - Herança e Polimorfismo

### 🔹 Herança

Evita código redundante reutilizando atributos e métodos de classes pai.

### 🔹 Propriedades

Getters e Setters permitem controlar o acesso a atributos (inclusive privados).

### 🔹 Método `super()`

Permite chamar métodos da classe pai dentro da classe filha.

### 🔹 Herança múltipla

Uma classe pode herdar de várias. Exemplo: `Pinguim` herda de `Animal`, `Aquático` e `Terrestre`.

### 🔹 MRO - Method Resolution Order

Define a ordem de execução dos métodos quando há herança múltipla.

### 🔹 Polimorfismo

Sobrescrevemos métodos da classe pai nas filhas para que se comportem de forma diferente.

### 🔹 Métodos mágicos

Permitem modificar o comportamento padrão de funções do Python, como `len()`:

```python
def __len__(self):
    return self.__paginas

print(len(livro))
```

✅ **Fim do módulo 16 - Herança e Polimorfismo**

---

## 📄 Módulo 17 - Manipulando Arquivos CSV e JSON

### 🔹 Lendo arquivos CSV

Para ler arquivos CSV, ele precisa estar no mesmo diretório do projeto. Existem duas formas de abrir: por `Reader` e por `DictReader`. Lembre-se de usar `encoding='utf-8'`. Se o arquivo não for separado por vírgula, use `delimiter='$'` (ou qualquer outro separador).

### 🔹 Escrevendo em Arquivos CSV

Também existe duas formas para escrever: `Writer` e `DictWriter`. O arquivo mostra as duas formas. Para adicionar dados sem sobrescrever, troque o `'w'` de *write* por `'a'` de *append*.

### 🔹 Conhecendo Pickle

Binariza e desbinariza arquivos. Ainda não entendi muito bem o porquê e para que serve.

### 🔹 Trabalhando com JSON e Pickle

Não entendi porra nenhuma mas tá aí 👍

✅ **Fim do módulo 17**

---

## 📆 Módulo 18 - Trabalhando com Data e Hora em Python

### 🔹 Manipulando data e hora

Em toda linguagem de programação, mexer com data e hora é sempre uma dor de cabeça. Em Python, com a biblioteca `datetime`, fica mais simples. Com comandos como `datetime.now()` ou `replace()` é fácil manipular os dados de data e hora.

### 🔹 Trabalhando com Deltas de data e hora

Delta é basicamente `data final - data inicial`. Usamos para saber quantos dias faltam para eventos, vencimentos etc.

### 🔹 Métodos de datas e horas

Mais uma aula sobre manipulação de hora e data.

✅ **Fim do módulo 18**

---

## 🧪 Módulo 19 - Testes com Python

### 🔹 Por que testar nosso código?

Testar códigos ajuda a reduzir bugs e garantir melhor qualidade e longevidade. A metodologia mais famosa é o TDD (desenvolvimento guiado por testes).

### 🔹 Assertions

Em Python, usamos a palavra `assert` para fazer afirmações simples nos testes. Se o programa for executado com o parâmetro `-O`, os `asserts` são ignorados.

### 🔹 DocTests

Colocamos os testes direto na `docstring` das funções/métodos:

```python
"""
>>> funcao(2)
4
"""
```

### 🔹 Introdução ao módulo Unittest

Para criar testes, usamos classes que herdam de `unittest.TestCase`:

```python
class TestRobo(unittest.TestCase):
```

### 🔹 Outros tipos de assertions

* `assertEqual(a, b)`
* `assertNotEqual(a, b)`
* `assertTrue(x)`
* `assertFalse(x)`

### 🔹 Hooks (setup e teardown)

* `setUp()` é executado antes de cada teste
* `tearDown()` é executado depois

✅ **Fim do módulo 19**

---

## 💾 Módulo 20 - Gerenciamento de Memória em Python

### 🔹 Alocação e Gerência de Memória

Python tem gerenciamento automático de memória via Garbage Collector. Isso torna o desenvolvimento mais rápido, mas tem desvantagens como:

* Menos controle sobre a memória
* Não é ideal para sistemas de baixo nível

### 🔹 GIL - Global Interpreter Lock

Aula explica como Python gerencia threads e diferenças de execução com 1 ou 2 threads simultâneas.

✅ **Fim do módulo 20**

---

## 📝 Módulo 21 - Checagem de Tipos em Python

### 🔹 Annotations

Com `print(__annotations__)` é possível ver os type hints das variáveis e atributos.

### 🔹 Checagem de tipos

Com `type hinting`, fica mais fácil identificar erros. Podemos usar o `mypy` para isso.

### ✅ Vantagens

* Facilita encontrar erros
* Melhora a documentação
* Melhora o autocomplete nas IDEs

### ⚠️ Desvantagens

* Estranhamento para iniciantes
* Pequena queda de performance

### 🔹 Comentários com tipo

Outra forma de `type hinting` com comentários:

```python
# type: (float) -> float
```

✅ **Fim do módulo 21**

---

## ✨ Módulo 22 - Novos Recursos do Python

### 🔹 Walrus Operator `:=`

Permite atribuir e retornar um valor na mesma expressão:

```python
print(nome := 'Geek University')
```

### 🔹 Argumentos somente posicionais ou nomeados

```python
# Argumento somente nomeado
def cumprimenta_v5(*, nome):
    return f'Olá, {nome}'

# Argumento somente posicional
def cumprimenta_v2(nome, /):
    return f'Olá, {nome}'
```

✅ **Fim do módulo 22**

---

🎉 **Curso finalizado!**
Se você chegou até aqui, parabéns! 🚀
Esses resumos são 100% do meu entendimento pessoal e refletem a minha jornada no aprendizado de Python com a Geek University. 🧠💻

