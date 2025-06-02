"""
Módulos customizados

Como módulos python nada mais são que arquivos python, então todos os arquivos que criamos no curso são módulos python
prontos para sere utilizados

#Exemplo
from funcoes_com_parametro import cantar_parabens
print(cantar_parabens('Fabio'))
"""
#Importando o módulo td (temos acesso a todos os elementos do módulo)
import funcoes_com_parametro as fcp

#Estamos acessando e imprimindo uma variável contida no módulo
print(fcp.soma(20, 5))
