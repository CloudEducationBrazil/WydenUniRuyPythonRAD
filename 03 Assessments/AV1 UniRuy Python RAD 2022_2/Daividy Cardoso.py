# OBSERVAÇÕES!!!!!!
# OBTIVE DIFICULDADE EM UTILIZAR A ESTRUTURA WHILE, PORÉM FIZ COM QUE O PROGRAMA FICASSE FUNCIONAL MESMO OBTENDO A AUSENCIA DA ESTRUTURA!
# MINHA APLICAÇÃO ESTÁ RODANDO NORMALMENTE DENTRO DO VS CODE E TAMBÉM NO ONLINE GDB, PORÉM QUANDO EU TENTO RODAR A MESMA NO CMD, ELA ESTÁ FECHANDO O CMD, TALVEZ O PROBLEMA SEJA MEU COMPUTADOR!

# DEFINIÇÕES --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# sem github
# sistema: registro de compras

lista = list()

abada = 324.99
camarote = 117.99
abacama = 430.00

menuAlteração = ('''
[ 1 ] Criar Lista
[ 2 ] Excluir lista
[ 3 ] Sair
''')

menuExcluir = ('''
[ 1 ] Criar nova lista
[ 2 ] Sair
''')

menuComplet = ('''
[ 1 ] Vender
[ 2 ] Alterar
[ 3 ] Pesquisar
[ 4 ] Sair
''')

menuProdutos = ('''
[ 1 ] Ábada
[ 2 ] Camarote
[ 3 ] Ábada e Camarote
''')


# INICIO---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
escolha = int(input(
    f'Seja Bem-vindo a nosso aplicativo de registro de compras, o que deseja fazer?{menuAlteração}'))

if escolha == 1:
    print('Iniciando criação de nova lista...')
    lista.append(input('Insira o nome do Cliente:'))
    venda1 = int(input(f'Qual o produto foi vendido? {menuProdutos}'))

    if venda1 == 1:
        lista.append('Ábada')
        lista.append(abada)

    elif venda1 == 2:
        lista.append('Camarote')
        lista.append(camarote)

    elif venda1 == 3:
        lista.append('Ábada e Camarote')
        lista.append(abacama)

    acesso1 = int(
        input(f'Lista criada com sucesso! O que deseja fazer agora? {menuComplet}'))


# INCLUIR --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if acesso1 == 1:
        print('Inclua aqui os dados da nova venda.')
        lista.append(input('Insira o nome do Cliente:'))
        venda2 = int(input(f'Qual o produto foi vendido? {menuProdutos}'))
        if venda2 == 1:
            lista.append('Ábada')
            lista.append(abada)
            print(
                f'Primeira Venda concluida... Cliente: {lista[0]}, Produto: {lista[1]}, Valor: {lista[2]}')
            print(
                f'Segunda Venda concluida... Cliente: {lista[3]}, Produto: {lista[4]}, Valor: {lista[5]}')

        elif venda2 == 2:
            lista.append('Camarote')
            lista.append(camarote)
            print(
                f'Primeira Venda concluida... Cliente: {lista[0]}, Produto: {lista[1]}, Valor: {lista[2]}')
            print(
                f'Segunda Venda concluida... Cliente: {lista[3]}, Produto: {lista[4]}, Valor: {lista[5]}')

        elif venda2 == 3:
            lista.append('Ábada e Camarote')
            lista.append(abacama)
            print(
                f'Primeira Venda concluida... Cliente: {lista[0]}, Produto: {lista[1]}, Valor: {lista[2]}')
            print(
                f'Segunda Venda concluida... Cliente: {lista[3]}, Produto: {lista[4]}, Valor: {lista[5]}')


# ALTERAR --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif acesso1 == 2:
        lista.clear()

        print('Faça aqui suas alterações.')
        lista.append(input('Insira o novo nome do Cliente:'))
        venda3 = int(
            input(f'Qual o novo produto vendido para o cliente? {menuProdutos}'))

        if venda3 == 1:
            lista.append('Ábada')
            lista.append(abada)
            print(
                f'Alteração concluida... Novo Cliente: {lista[0]}, Novo Produto: {lista[1]}, Novo Valor: {lista[2]}')

        elif venda3 == 2:
            lista.append('Camarote')
            lista.append(camarote)
            print(
                f'Alteração concluida... Novo Cliente: {lista[0]}, Novo Produto: {lista[1]}, Novo Valor: {lista[2]}')

        elif venda3 == 3:
            lista.append('Ábada e Camarote')
            lista.append(abacama)
            print(
                f'Alteração concluida... Novo Cliente: {lista[0]}, Novo Produto: {lista[1]}, Novo Valor: {lista[2]}')


# PESQUISA --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif acesso1 == 3:
        print(
            f'A ultima venda feita foi a do cliente: {lista[0]}, o produto foi um: {lista[1]} no valor de: R${lista[2]}')


# SAIDA --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif acesso1 == 4:
        print('Obrigado por acessar nosso dispositivo, saindo do aplicativo!')
# EXCLUSÃO --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
elif escolha == 2:
    lista.clear()
    print('Todos os itens foram excluidos da lista!')
    acesso2 = int(input(f'O que você deseja fazer agora? {menuExcluir}'))

    if acesso2 == 2:
        print('Obrigado por acessar nosso dispositivo, saindo do aplicativo!')

    elif acesso2 == 1:
        print('Criando nova lista!')
        print('Iniciando criação de nova lista...')
        lista.append(input('Insira o nome do Cliente:'))
        venda3 = int(input(f'Qual o produto foi vendido? {menuProdutos}'))

        if venda3 == 1:
            lista.append('Ábada')
            lista.append(abada)
            print(
                f'Venda concluída... Cliente: {lista[0]}, Produto: {lista[1]}, Valor: {lista[2]}')

        elif venda3 == 2:
            lista.append('Camarote')
            lista.append(camarote)
            print(
                f'Venda concluída... Cliente: {lista[0]}, Produto: {lista[1]}, Valor: {lista[2]}')

        elif venda3 == 3:
            lista.append('Ábada e Camarote')
            lista.append(abacama)
            print(
                f'Venda concluída... Cliente: {lista[0]}, Produto: {lista[1]}, Valor: {lista[2]}')


# OPÇÃO DE SAIDA DO APLICATIVO ----------------------------------------------------------------------------------------------------------------------------------------------------------
elif escolha == 3:
    print('Obrigado por acessar nosso dispositivo, saindo do aplicativo!')
