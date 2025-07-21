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

(continuação nos próximos módulos...)


