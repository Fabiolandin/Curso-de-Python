# 🐍 Curso de Python - Resumo Pessoal

Repositório com anotações e resumos que escrevi com minhas próprias palavras durante o curso de Python da Geek University. Organizado por módulos para facilitar revisões e consultas rápidas.

---
## 🧰 Módulo 6 - Coleções em Python

### 🔹 Listas

Listas em python, funcionam como vetores/matrizes, com a diferença de serem dinâmicos e também podemos colocar qualquer tipo de dados.
As listas em Python são representadas por colchetes: []

### 🔹 Tuplas

Tuplas são bem parecidas com listas, existem 2 diferenças bases:

1- As tuplas são representadas por parenteses (4,) e virgula ,
2- As tuplas são imutáveis: não podem ser mudadas, tota alteração em uma tupla gera uma nova tupla
3- As tuplas são mais rápidas do que as listas
4- Tuplas deixam seu código mais seguro

### 🔹 Dicionários

Em algumas linguagens dicionários são iguais a mapas em Python dicionários são representados por chaves {}.

### 🔹 Conjuntos

- Conjuntos em python é uma referencia a teoria dos conjuntos matemática.
- Em python são chamados de Sets, e não possuem valores duplicados e nem ordenados.

### 🔹 Módulo Collections - Counter
Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com dicionário.

### 🔹 Módulo Collections - Default Dict

Default dict -  ao criar um dicionário nós informamos um valor default, podendo utilizar lambda para isso. Caso tentamos acessar uma chave que não existe, essa chave será criada e o valor default será atribuído.

### 🔹 Módulo Collections - Ordered Dict

Nada mais é que um definir a ordenação de um dicionário usando OrderedDict

### 🔹 Módulo Collections - Named Tuple

São tuplas diferenciadas onde especificamos um nome para a mesma e parâmetros.
Exemplo: ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

### 🔹 Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance, tirando isso é a mesma finalidade.

✅ **Fim do módulo 6**

---
## 🧠 Módulo 7 - Funções em Python

### 🔹 Definindo funções
Funções são pequenos partes de códigos que realizam tarefas especificas.
- Pode ou não receber entradas de dados e retornar uma saída de dados.
- Util para utilizar e reutilizar por repetidas vezes afins de reduzir o código.

### 🔹 Funções com retorno
Nada mais são que funções que possuem a linha 'return', o return finaliza a função e retorna algum valor ou string especificado

Exemplo de função que retorna valor da conta 7 * 7
```python
def quadrado_de_7():
    return 7 * 7
```

### 🔹 Funções com parâmetro
Funções que recebem dados para serem processados dentro da mesma

### 🔹 Funções com parâmetro padrão
Funções onde a passagem de parâmetros seja opcional, se você passar pode executar uma parte da função, se não passar ela executa da mesma forma.

### 🔹 Documentando funções com Docstrings
é um """ oque a função faz """ dentro da função, podemos ainda fazer o acesso a documentação com a função help()

### 🔹 Entendendo Args
Args é um parâmetro como outro qualquer, isso significa que você poderá chamar qualquer outra coisa, desde que comece com o *asterisco.
Args é um parâmetro utilizado em funções, e como se não quisesse definir quantos parâmetros deseja receber então como como *args, só que recebe como tupla

### 🔹 Entendendo Kwargs
Igual a args porém ele coloca os valores extras em um dicionário, os parâmetros args e kwargs não são obrigatórios.

✅ **Fim do módulo 7**

---
## 🔁 Módulo 8 - List Comprehension e Coleções

### 🔹 List Comprehension - Parte 1
Utilizando list comprehension nos podemos gerar novas listas com dados processados a partir de outro iterável. Basicamente é você iterar lista dentro da própria lista.

Sintaxe da list comprehension
```python
[ dado  for dado in iterável ]
```

### 🔹 List Comprehension - Parte 2
Também é possível adicionar condicionais dentro das lists comprehension
Exemplo:
```python
numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
```

### 🔹 Listas aninhadas
Listas aninhadas são listas dentro de listas, como uma matriz 3x3

### 🔹 Dictionary Comprehension
A mesma coisa do list comprehension só que com dicionário da pra iterar dentro do dicionário e até mesmo usar estruturas condicionais.

✅ **Fim do módulo 8**

---

🧠 Módulo 9 - Expressões Lambdas e Funções Integradas
🔹 Utilizando Lambdas
Conhecidas por expressões lambdas, ou simplesmente lambdas, são funções sem nome, ou seja, funções anônimas. Lambdas são usadas para coisas mais simples, sem muitas linhas e complexidade sendo assim melhor que função para o caso.

🔹 Map
Map é uma função que recebe dois parâmetros: O primeiro a função, e o segundo um iterável. Retorna um map object. É uma das ferramentas mais práticas do Python, você passa a função e uma lista de iteráveis e o map passa a função em cada elemento da lista, é como um iterável próprio de função.

🔹 Filter
filter() -> Serve para filtrar dados de uma determinada coleção.

🔹 Reduce
A partir do Python 3 a função reduce não é mais uma função integrada, agora precisa importar functools.

🔹 Any e All
all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
any() -> Retorna True se qualquer elemento for verdadeiro, se o iterável estiver vazio retorna False.

🔹 Generators
Tuple comprehension se chamam generators, generators são mais leves e mais performáticos.

🔹 Sorted
Apesar do nome, não é igual à função sort(), o sorted() só funciona em listas. Ele serve para ordenar elementos, porém não modifica a lista.

🔹 Min e Max
Funciona pra tupla, conjunto, dicionário, lista.
max() -> retorna o maior valor
min() -> retorna o menor valor

🔹 Reversed
A função reversed() funciona com qualquer iterável, é basicamente inverter o iterável.

🔹 Len, Abs, Sum e Round
len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.
abs() -> Retorna o valor absoluto de um número inteiro ou real
sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos
round() -> Retorna um número arredondado para um n dígito de precisão. Se n não for informado, retorna o inteiro mais próximo da entrada.

🔹 Zip
zip() -> Cria um iterável (Zip Object) que agrega elementos de cada um dos iteráveis passados como entrada em pares.

✅ Fim do módulo 9
---

🛠️ Módulo 10 - Debugando e Tratando Erros
🔹 Erros mais comuns em Python

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe, você escreveu algo que o Python não reconhece como parte da linguagem.

NameError -> Ocorre quando uma variável/função não foi definida.

TypeError -> Ocorre quando uma função/operação é aplicada a um tipo errado.

IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido.

ValueError -> Ocorre quando uma função/operação built-in recebe um argumento com tipo correto mas valor inapropriado.

🔹 Levantando os próprios erros com raise
raise é uma palavra reservada como def. Raise é útil para criar nossas próprias mensagens de erro.
Exemplo:

python
Copiar
Editar
raise TipoDoErro('Mensagem de erro')
raise TypeError('O texto deve ser string')
🔹 O bloco Try/Except
Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código, prevenindo que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

🔹 Try, Except, Else e Finally

finally: Sempre será executado ao final, geralmente utilizado para fechar ou desalocar recursos.

🔹 Debugando código com PDB
PDB -> Python Debugger
Para utilizar o PDB precisamos importar a biblioteca e então utilizar a função set_trace().

✅ Fim do módulo 10
---

📦 Módulo 11 - Trabalhando com Módulos Python
🔹 O módulo Random
Módulo random -> Possui várias funções para geração de números pseudo-aleatórios, bom para sorteios de números aleatórios e geração dos mesmos.

🔹 Trabalhando com módulos Built-In
Módulos Built-in (módulos integrados que já vêm instalados no Python)

🔹 Módulos customizados
Como módulos Python nada mais são que arquivos .py, então todos os arquivos que criamos no curso são módulos prontos para serem utilizados. Podemos criar arquivos com funções e importar em outros arquivos, tendo assim módulos customizados.

🔹 Instalando e utilizando Módulos Externos
Utilizamos o gerenciador de pacotes do Python chamado Pip - Python Installer Package.
O exemplo utilizado na aula foi o colorama, utilizado para permitir impressão de textos coloridos no terminal.

🔹 Pacotes

Módulo -> É apenas um arquivo em Python que pode ter diversas funções para utilizarmos.

Pacote -> É um diretório contendo uma coleção de módulos.

🔹 Dunder Main e Dunder Name
Em Python são utilizados dunders para criar funções/atributos usando Double Under (__) para não gerar conflito com nomes.

__name__

__main__

✅ Fim do módulo 11

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

