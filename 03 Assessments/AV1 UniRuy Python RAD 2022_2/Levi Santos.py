# vendas apartamentos

import os
listaCont = []
listaNome = []
listaApartamento = []
listaCondominio = []
listaMoradores = []
loop = "sim"
# Ler
with open('crud.txt', 'r+') as arquivo:
    lista = []
    for dados in arquivo:
        lista.append(dados[:-1])
    for i in range(int(len(lista)/5)):
        listaCont.append(int(lista[(i*5)]))
        listaNome.append(lista[(i*5)+1])
        # listaApartamento.append(int(lista[(i*5)+2]))
        listaApartamento.append(int(lista[(i*5)]))
        listaCondominio.append(lista[(i*5)+3])
        # listaMoradores.append(int(lista[(i*5)+4]))
        listaMoradores.append(int(lista[(i*5)]))
menu = input("Você quer entrar no menu? Utilize sim ou não\n")
if (menu == "não"):
    print("Essas são as últimas listas armazenadas, obrigado por utilizar o nosso sistema!")
    print(listaCondominio)
    print(listaNome)
    print(listaApartamento)
    print(listaMoradores)
    menu = input("Você quer entrar no menu? Utilize sim ou não\n")
while (menu == "sim"):
    decida = int(input(
        "Selecione a opção que deseja: \n Cadastrar Morador (1)\n Editar (2)\n Remover (3)\n  Exibir (4)\n"))
    #Adicionando morador#
    if decida == 1:
        Condominio = (input("Qual o nome do seu condomínio?\n"))
        Nome = (input("Qual o seu nome?\n"))
        Apartamento = int(input("Qual o número do seu apartamento?\n"))
        Moradores = int(input("Quantas pessoas moram na sua casa?\n"))
        registro = (len(listaCont))+1
        listaCondominio.append(Condominio)
        listaApartamento.append(Apartamento)
        listaNome.append(Nome)
        listaMoradores.append(Moradores)
        listaCont.append(registro)
        with open('crud.txt', 'r+')as arquivo:
            for i in range(len(listaCont)):
                arquivo.write(str(listaCont[i])+'\n')
                arquivo.write(str(listaCondominio[i])+'\n')
                arquivo.write(str(listaApartamento[i])+'\n')
                arquivo.write(str(listaNome[i])+'\n')
                arquivo.write(str(listaMoradores[i])+'\n')
        os.system('cls')
        print("Cadastro feito com sucesso!")
        # Editando morador pelo nome
    if decida == 2:
        edit = int(input(
            "O que você quer mudar? Nome (1) Apartamento (2) Condominio (3) Quantidade de moradores (4)\n"))
        if edit == 1:
            numeroId = int(input("Qual o seu id?"))
            if numeroId in listaCont:
                mude = input("Digite a sua alteração \n")
                posit = listaCont.index(numeroId)
                listaNome[posit] = mude
                os.system('cls')
                print("Mudança efetuada!")
        else:
            os.system('cls')
            print("ID inválido")
            # Editando morador por apartamento
        if edit == 2:
            numeroId = int(input("Qual o seu id?"))
            for x in listaCont:
                if x == numeroId:
                    mude = int(input("Digite a sua alteração \n"))
                    posit = listaCont.index(numeroId)
                    listaApartamento[posit] = mude
                    os.system('cls')
                    print("Mudança efetuada!")
            else:
                print("ID inválido")
            # Editando morador por condominio
        if edit == 3:
            numeroId = int(input("Qual o seu id?"))
            for x in listaCont:
                if x == numeroId:
                    mude = input("Digite a sua alteração \n")
                    posit = listaCont.index(numeroId)
                    listaCondominio[posit] = mude
                    os.system('cls')
                    print("Mudança efetuada")
            else:
                print("ID inválido")
        if edit == 4:
            numeroId = int(input("Qual o seu id?"))
            for x in listaCont:
                if x == numeroId:
                    mude = int(input("Digite a sua alteração \n"))
                    posit = listaCont.index(numeroId)
                    listaMoradores[posit] = mude
                    os.system('cls')
                    print("Mudança efetuada!")
            else:
                print("ID inválido")
        with open('crud.txt', 'w')as arquivo:
            for i in range(len(listaCont)):
                arquivo.write(str(listaCont[i])+'\n')
                arquivo.write(str(listaCondominio[i])+'\n')
                arquivo.write(str(listaApartamento[i])+'\n')
                arquivo.write(str(listaNome[i])+'\n')
                arquivo.write(str(listaMoradores[i])+'\n')
            # Excluindo informações na lista
    if decida == 3:
        numeroId = int(input("Qual o seu ID?\n"))
        for numeroId in listaCont:
            mude = 0
            posit = listaCont.index(numeroId)
            listaNome[posit] = mude
            listaNome[posit] = mude
            listaCondominio[posit] = mude
            listaApartamento[posit] = mude
            listaMoradores[posit] = mude
        if numeroId > len(listaNome):
            print("Esse ID está inválido")
        with open('crud.txt', 'w')as arquivo:
            for i in range(len(listaCont)):
                arquivo.write(str(listaCont[i])+'\n')
                arquivo.write(str(listaCondominio[i])+'\n')
                arquivo.write(str(listaApartamento[i])+'\n')
                arquivo.write(str(listaNome[i])+'\n')
                arquivo.write(str(listaMoradores[i])+'\n')
        # Excluindo através do apartamento
    if decida == 4:
        os.system('cls')
        print(listaCondominio)
        print(listaNome)
        print(listaApartamento)
        print(listaMoradores)
        print(listaCont)
