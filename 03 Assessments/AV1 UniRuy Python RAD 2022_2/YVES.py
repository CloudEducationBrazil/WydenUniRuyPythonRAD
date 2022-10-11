# Aplicação de Hóspedes de Hotel
#Matricula: 202108665703
# Aluno:Yves Lucas
# GITHUB - NÃO POSTOU

import os
import time
listaNome = []
listaValor = []

Total_a_ser_pago = listaValor
Total_a_ser_pago = listaNome


def manu():

    print('O que deseja fazer')
    print('1- cadastrar_hospede')
    print('2- Alterar')
    print('3- Pesquisar')
    print('4- Excluir')
    print('5- Sair')


def manuAlteração():

    print('Tipo de Alteração')
    print('1- Indice')
    print('2- Por Nome')
    print('3- Sair')


def cadastrar_hospede():

    print('Modulo Cadastramento')
    nome = str(input('Informe nome:'))
    valor_do_pagamento = float(input('Informe valor do quarto de hospedagem:'))

    if valor_do_pagamento >= 0:
        listaNome.append(nome)
        listaValor.append(valor_do_pagamento)

        while True:
            resp = str(input('Quer Continuar? [S/N]'))
            if resp in 'Nn':
                return manu

        while True:
            resp = str(input('Quer Continuar? [S/N]'))
            if resp in 'Ss':
                return cadastrar_hospede

        while valor_do_pagamento:
            print()
            nome = str(input('Informe Nome:'))
            valor_do_pagamento = float(input('Informe valor do pagamento'))
            if valor_do_pagamento > 0:
                listaNome.append(nome)
                listaValor.append(valor_do_pagamento)


def alterar():

    print('Modulo da Alteracao')
    while True:
        manuAlteração()

        try:
            opcao = int(input('Selecione uma opcao:'))
        except ValueError as e:
            print('Nao e permitido!')
        if opcao == 1:
            indice = int(input('Informe a posicao para alterar:'))

            if indice > len(listaNome):
                print('Nao existe!')
                time.sleep(1)
            else:
                nome = str(input('Informe novo nome:'))
                valor_do_pagamento = float(
                    input('Informe novo valor de pagamento:'))
                while valor_do_pagamento < 0:
                    print('Valor nao pode ser nagativo')
                    valor_do_pagamento = float(
                        input('Informe novo valor de pagamento:'))

                listaNome[indice] = nome
                listaValor[indice] = valor_do_pagamento

        elif opcao == 2:
            print('Alteracao por nome')
            nome = str(input('Informe nome:'))

            for indice in range(len(listaNome)):
                if nome == listaNome[indice]:

                    valor_do_pagamento = float(input('Informe novo valor'))
                    while valor_do_pagamento < 0:
                        print('Valor nao pode ser negativo!')
                        valor_do_pagamento = float(
                            input('Informe o novo valor de pagamento:'))

                    listaNome[indice] = nome
                    listaValor[indice] = valor_do_pagamento
                    break
                else:
                    print('Nome inexitente')

        elif opcao == 3:
            break
        else:
            print('Opcao invalida')

        while True:
            resp = str(input('Quer Continuar? [S/N]'))
            if resp in 'Nn':
                return manu


def excluir():
    print('Excluindo')
    print(listaNome)
    print(listaValor)

    listaNome.clear()
    listaValor.clear()

    while True:
        resp = str(input('Quer Continuar? [S/N]'))
        if resp in 'Nn':
            return manu


def consultar():
    print('Consultando')
    print(listaNome)
    print(listaValor)


listaNome = []
listaValor = []

opcao = -1

while True:
    manu()

    try:
        opcao = int(input('Selecione opcao:'))
    except ValueError as e:
        print('Nao e permitido')

    if opcao == 1:
        cadastrar_hospede()
    elif opcao == 2:
        alterar()
    elif opcao == 3:
        consultar()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        print('Obrigado pela preferencia!')

        break
    else:
        print('Opcao inexiteste')

    time.sleep(1)
