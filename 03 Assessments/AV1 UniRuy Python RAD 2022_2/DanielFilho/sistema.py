# COMPRAS/VENDAS
# https://github.com/Daniel-Filho370/CRUD

from AV01.lib.interface import *
from AV01.lib.metodos import *
from time import sleep


while True:
    resposta = menu(['Consultar pedido', 'Incluir Pedido', 'Alterar Pedido', 'Excluir Pedido',
                     'Gravar em Arquivo TXT', 'Importar do Arquivo TXT', 'Sair'])
    if resposta == 1:
        cabeçalho('LISTA')
        print(lista_compras_e_vendas)
        sleep(2)

    elif resposta == 2:
        cabeçalho('INCLUIR PEDIDO')
        linha()
        cadastrar()

    elif resposta == 3:
        while True:
            escolha = subMenu(
                ['ID', 'Nome do produto', 'Voltar ao menu principal'])
            if escolha == 1:
                print('Funcionalidade indisponivel!')
            elif escolha == 2:
                print('Funcionalidade indisponivel')
            else:
                print('Retornando ao menu principal...')
                sleep(2)
                break

    elif resposta == 4:
        excluir()

    elif resposta == 5:
        gravarArquivo()

    elif resposta == 6:
        importarArquivo()

    elif resposta == 7:
        print('saindo... Até logo!')
        sleep(2)
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
        sleep(2)
