"""
Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um mét0do para imprimir os dados de uma pessoa.
"""
from datetime import date

class Pessoa:
    def __init__(self, nome: str, data_nascimento: date, email: str) -> None:
        self._nome = nome  # Atributo privado inicializado diretamente
        self._data_nascimento = data_nascimento  # Atributo privado
        self._email = email  # Atributo privado

    # Getter para nome
    @property
    def nome(self) -> str:
        return self._nome

    # Setter para nome
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    # Getter para data nascimento
    @property
    def data_nascimento(self) -> date:
        return self._data_nascimento

    # Setter para data nascimento
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        self._data_nascimento = data_nascimento

    # Getter para email
    @property
    def email(self) -> str:
        return self._email

    # Setter para email
    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    def imprimi_dados(self) -> str:
        return f'Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}, Email: {self.email}'

# Teste
pessoa1 = Pessoa('Fabio', date(2002, 9, 13), 'flandin1990@gmail.com')
print(pessoa1.imprimi_dados())

"""
Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
armazenar_contato(contato: Contato);
remover_contato(contato: Contato);
buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""
from datetime import date


class Agenda:
    def __init__(self):
        self._contatos: list[Pessoa] = []  # Atributo privado

    @property
    def contatos(self) -> list[Pessoa]:
        return self._contatos

    def armazenar_contato(self, contato: Pessoa) -> None:
        self._contatos.append(contato)

    def remover_contato(self, contato: Pessoa) -> None:
        if contato in self._contatos:
            self._contatos.remove(contato)
        else:
            print(f"Contato {contato.nome} não encontrado na agenda.")

    def buscar_contato(self, nome: str) -> int:
        for indice, contato in enumerate(self._contatos):
            if contato.nome == nome:
                return indice
        return -1  # Retorna -1 se não encontrar

    def imprimir_agenda(self) -> None:
        if not self._contatos:
            print("Agenda vazia.")
            return

        print("\n--- CONTATOS NA AGENDA ---")
        for contato in self._contatos:
            print(contato.imprimi_dados())
        print("--------------------------\n")

    def imprimir_contato(self, indice: int) -> None:
        try:
            print(self._contatos[indice].imprimi_dados())
        except IndexError:
            print(f"Erro: Índice {indice} não existe na agenda.")


if __name__ == '__main__':
    # Criação dos contatos
    contato1 = Pessoa('Fabio', date(2002, 9, 13), "flandin1990@GMAIL.com")
    contato2 = Pessoa('Alexa', date(1994, 11, 4), "alexa@amazon.com")

    # Criação e uso da agenda
    agenda = Agenda()

    # Adiciona contatos
    agenda.armazenar_contato(contato1)
    agenda.armazenar_contato(contato2)

    # Imprime toda a agenda
    agenda.imprimir_agenda()

    # Busca e imprime contato específico
    posicao = agenda.buscar_contato("Alexa")
    if posicao != -1:
        print(f"Alexa encontrada na posição {posicao}")
        agenda.imprimir_contato(posicao)
    else:
        print("Contato não encontrado.")

    # Teste com índice inválido
    agenda.imprimir_contato(10)  # Deve mostrar mensagem de erro

