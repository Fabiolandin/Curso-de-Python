from models.cliente import Cliente
from models.conta import Conta

marcos: Cliente = Cliente('Marcos', 'marcos@gmail.com', '123.456.778-87', '13/05/2002')
carlos: Cliente = Cliente('Marcos', 'carlos@gmail.com', '153.499.778-01', '15/12/2002')

print(marcos)
print(carlos)

contaf: Conta = Conta(marcos)
contaa: Conta = Conta(carlos)

print(contaf)
print(contaa)