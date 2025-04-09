# Controle de Estoque

estoque = []
numestoque = []

print("--------- Bem vindo(a) ao sistema de Estoque --------- ")

while True:

    print('''Escolha uma das opções abaixo \n \
     1- Inserir produto \n  \
    2- Consultar produto \n  \
    3- Alterar produto \n  \
    4- Remover produto \n  \
    5- Gravar arquivo \n  \
    6- Importar em arquivo \n  \
    7- Sair \n''')
    escolha = int(input("Digite o número da opção escolhida: "))

    if escolha == 1:

        insira = str(input(" Insira uma bebida:  "))
        qtd = int(input(" Insira a quantidade: "))
        estoque.append(insira)
        numestoque.append(qtd)
        print("Bebida inserida com sucesso! \n")
        print(estoque)
        print(numestoque)

    elif escolha == 2:
        consultar = input("Digite a bebida que deseja consultar: ")
        if consultar in estoque:
            print(" Essa bebida não está na lista! ")
        else:
            consulta = consultar + numestoque
            if consultar in estoque:
                print(
                    " A bebida está na lista e possui {} bebida(s).".format(numestoque))

            else:
                print(" A bebida não está na lista. Deseja adicionar? ")
                print(" Digite 1 para sim e a quantidade e 2 para não.")
                selec = int(input("Selecione: "))
            if selec == 1:
                estoque.append(consultar)
                numestoque.append(consulta)
                print("Bebida Adcionada!")
                print(estoque)

            else:
                print("voltar para o menu.")

    if escolha == 3:
        print(estoque)
        print(numestoque)
        alterar = input("Digite qual bebida deseja substituir: ")
        count = int(input(
            "Selecione a posição de troca da bebida.(OBS:A contagem começa do zero!): "))
        estoque[count] = alterar
        print(estoque)
        print(numestoque)
        qtd_alterar = int(
            input("Digite a quantidade de bebida que deseja alterar: "))
        count = int(input(
            "Selecione a posição de troca da bebida.(OBS:A contagem começa do zero!): "))
        numestoque[count] = qtd_alterar
        print(numestoque)

    if escolha == 4:
        print(estoque)
        print(numestoque)
        remover = input("Digite a bebida à ser removida: ")
        if remover in estoque:
            estoque.remove(remover)
            print(estoque)

        else:
            print(numestoque)
            delete = input("Digite a quantidade da bebida à ser removida: ")
        if delete in estoque:
            estoque.remove(delete)
            print(numestoque)

    if escolha == 5:
        print(estoque)
        print(numestoque)
        arquivo = open("texto.txt", "a")
        arquivo.writelines(line + '\n' for line in estoque and numestoque)
        print("Arquivo salvo!")

    elif escolha == 6:
        arquivo = open("texto.txt", "r")
        estoque = arquivo.readlines()
        numestoque = arquivo.readlines()
        print(estoque)
        print(numestoque)
        print("Arquivo importado!")
    else:
        print("Voltar para o menu.")

    if escolha == 7:
        exit()
