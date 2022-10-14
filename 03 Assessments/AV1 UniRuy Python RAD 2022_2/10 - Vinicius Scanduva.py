# https://github.com/XScanx/avaliacao_python/blob/main/CRUD.py
# Imóveis

import time
import os
id = []
name = []
value = []
size = []
homeRoom = []
description = []
loop = "sim"
print("\n______________________Gerenciador de imóveis______________________\n")
while loop == "sim":
    # MENU DE ESCOLHA
    choice = int(input("*----------------------MENU----------------------*\n1 - Consultar\n2 - Cadastrar\n3 - Editar\n4 - Excluir\n5 - Gravar Arquivo TXT\n6 - Importar do arquivo TXT\n7 - Sair\n"))
    # FUNÇÃO DE CONSULTA NO CODIGO
    if choice == 1:
        os.system('cls')
        if len(id) > 0:
            choice2 = int(input(
                "Escolha a forma de consulta:\n1 - ID\n2 - Locador\n3 - Todos os elementos\n"))
            # CONSULTA PELO ID
            if choice2 == 1:
                os.system('cls')
                numID = int(input("Informe o ID:\n"))
                # VERIFICAÇÃO DA EXISTENCIA DO ID
                if numID in id:
                    for search in id:
                        if search == numID:
                            position = id.index(numID)
                            print("ID: {}\nLocador: {}\nValor: R$ {}\nTamanho: {} m²\nCômodo(s): {}\nDescrição: {}\n".format(
                                id[position], name[position], value[position], size[position], homeRoom[position], description[position]))
                    time.sleep(3)
                    print('\n\n\n')
                    loop = "sim"
                else:
                    os.system('cls')
                    print("ID informado inválido !\n")
                    time.sleep(2)
                    os.system('cls')
                    print("Redirecionando ao menu de opções...\n")
                    time.sleep(3)
                    os.system('cls')
            # CONSULTA PELO NOME DE LOCADORES
            elif choice2 == 2:
                os.system('cls')
                nameLocator = input(
                    "Informe o nome do locador do imóvel: \n").lower()
                # VERIFICAÇÃO DA EXISTENCIA DO LOCADOR
                if nameLocator in name:
                    for search in range(len(name)):
                        if name[search] == nameLocator:
                            print("\n")
                            print("ID: {}\nLocador: {}\nValor: R$ {}\nTamanho: {} m²\nCômodo(s): {}\nDescrição: {}\n".format(
                                id[search], name[search], value[search], size[search], homeRoom[search], description[search]))
                            time.sleep(2)
                    print("\n\n\n")
                    time.sleep(3)
                    loop = "sim"
                else:
                    os.system('cls')
                    print("Locador inexistente !\n")
                    time.sleep(2)
                    os.system('cls')
                    print("Redirecionando ao menu de opções...\n")
                    time.sleep(3)
                    os.system('cls')
                    loop = "sim"
            # CONSULTA DE TODOS OS ELEMENTOS CADASTRADOS
            elif choice2 == 3:
                os.system('cls')
                for indexId in range(len(id)):
                    for indexName in range(len(name)):
                        for indexValue in range(len(value)):
                            for indexSize in range(len(size)):
                                for indexHomeRoom in range(len(homeRoom)):
                                    for indexDescription in range(len(description)):
                                        if indexId == indexName == indexValue == indexSize == indexHomeRoom == indexDescription:
                                            print("\n")
                                            print("ID: {}\nLocador: {}\nValor: R$ {}\nTamanho: {} m²\nCômodo(s): {}\nDescrição: {}\n".format(
                                                id[indexId], name[indexName], value[indexValue], size[indexSize], homeRoom[indexHomeRoom], description[indexDescription]))
                                            print("\n")
                                            time.sleep(2)
        else:
            print("Não existe nenhum cadastro no momento !\n")
            time.sleep(2)
            os.system('cls')
            print(
                "Para acessar essa função é necessário um cadastro, redirecionando ao menu...\n")
            time.sleep(4)
            os.system('cls')
            loop = "sim"
    # FUNÇÃO DE CADASTRO DOS IMÓVEIS
    elif choice == 2:
        os.system('cls')
        primaryKey = int(input("Informe o ID do imóvel: \n"))
        if primaryKey in id:
            os.system('cls')
            print("\nEsse código ID já existe, por gentileza cadastrar outro.")
            time.sleep(3)
            os.system('cls')
            loop = "sim"
        else:
            id.append(primaryKey)
            print("\nID válido !\n")
            locator = input("Informe o nome do locador: \n").lower()
            Value = float(input("Informe o valor desejado: \n"))
            Size = float(input("Informe o tamanho em m²: \n"))
            HomeRoom = int(
                input("Informe quantos cômodos existem no imóvel: \n"))
            Description = input("Descreva o imóvel: \n").lower()
            name.append(locator)
            value.append(Value)
            size.append(Size)
            description.append(Description)
            homeRoom.append(HomeRoom)
            os.system('cls')
            print("\nCadastro completo !\n\nNão esqueça de gravar os dados no menu ! :D")
            time.sleep(2)
            os.system('cls')
    # FUNÇÃO DE EDIÇÃO DOS ELEMENTOS
    elif choice == 3:
        os.system('cls')
        if len(id) > 0:
            choiceEdit = int(input(
                "Informe o elemento que será alterado:\n1 - ID\n2 - Locador\n3 - Valor\n4 - Tamanho\n5 - Cômodo(s)\n6 - Descrição\n"))
            if choiceEdit < 0 or choiceEdit > 6:
                os.system('cls')
                print("Opção inválida!")
                time.sleep(2)
                os.system('cls')
                loop = "sim"
            else:
                time.sleep(2)
                os.system('cls')
                edition = int(
                    input("Digite o ID do cadastro a ser editado: \n"))
                # VERIFICAÇÃO DA EXISTENCIA DO ID
                if edition in id:
                    # EDIÇÃO DO ID
                    if choiceEdit == 1:
                        newId = int(input("Informe o novo numero ID: \n"))
                        if newId in id:
                            os.system('cls')
                            print("Esse número de ID já existe, informe outro.\n")
                        else:
                            os.system('cls')
                            for searchEdit in id:
                                if searchEdit == edition:
                                    positionEdit = id.index(edition)
                                    id[positionEdit] = newId
                                    print(
                                        "ID alterado com sucesso !\n\nNão esqueça de gravar os dados no menu ! :D")
                            time.sleep(2)
                            os.system('cls')
                            loop = "sim"
                    # EDIÇÃO DE LOCADOR
                    elif choiceEdit == 2:
                        os.system('cls')
                        newLocator = input(
                            "Informe o nome do novo locador: \n")
                        for searchEdit in id:
                            if searchEdit == edition:
                                positionEdit = id.index(edition)
                                name[positionEdit] = newLocator
                        os.system('cls')
                        print(
                            "Locador alterado com sucesso !\n\nNão esqueça de gravar os dados no menu ! :D")
                        time.sleep(3)
                        os.system('cls')
                        loop = "sim"
                    # EDIÇÃO DO VALOR
                    elif choiceEdit == 3:
                        os.system('cls')
                        newValue = float(
                            input("Informe o novo valor do imóvel: \n"))
                        for searchEdit in id:
                            if searchEdit == edition:
                                positionEdit = id.index(edition)
                                value[positionEdit] = newValue
                        os.system('cls')
                        print(
                            "Valor alterado com sucesso !\n\nNão esqueça de gravar os dados no menu ! :D")
                        time.sleep(3)
                        os.system('cls')
                        loop = "sim"
                    # EDIÇÃO DO TAMANHO
                    elif choiceEdit == 4:
                        os.system('cls')
                        newSize = float(
                            input("Informe o novo tamanho em m²: \n"))
                        for searchEdit in id:
                            if searchEdit == edition:
                                positionEdit = id.index(edition)
                                size[positionEdit] = newSize
                        os.system('cls')
                        print(
                            "Tamanho alterado com sucesso !\n\nNão esqueça de gravar os dados no menu ! :D")
                        time.sleep(3)
                        os.system('cls')
                        loop = "sim"
                    # EDIÇÃO DA QUANTIDADE DE COMODOS
                    elif choiceEdit == 5:
                        os.system('cls')
                        newHomeRoom = input(
                            "Informe o novo número de cômodos: \n")
                        for searchEdit in id:
                            if searchEdit == edition:
                                positionEdit = id.index(edition)
                                homeRoom[positionEdit] = newHomeRoom
                        os.system('cls')
                        print(
                            "Quantidade de cômodos alterada com sucesso !\n\nNão esqueça de gravar os dados no menu ! :D")
                        time.sleep(3)
                        os.system('cls')
                        loop = "sim"
                    # EDIÇÃO DA DESCRIÇÃO
                    elif choiceEdit == 6:
                        os.system('cls')
                        newDescription = input("Informe a nova descrição: \n")
                        for searchEdit in id:
                            if searchEdit == edition:
                                positionEdit = id.index(edition)
                                description[positionEdit] = newDescription
                        os.system('cls')
                        print(
                            "Descrição alterada com sucesso !\n\nNão esqueça de gravar os dados no menu ! :D")
                        time.sleep(3)
                        os.system('cls')
                        loop = "sim"
                else:
                    os.system('cls')
                    print("ID informado inexistente !")
                    time.sleep(2)
                    os.system('cls')
                    print("Retornando ao menu de opções...")
                    time.sleep(3)
                    os.system('cls')
                    loop = "sim"
        else:
            os.system('cls')
            print("Não existe nenhum cadastro no momento !\n")
            time.sleep(2)
            os.system('cls')
            print(
                "Para acessar essa função é necessário um cadastro, redirecionando ao menu...\n")
            time.sleep(4)
            os.system('cls')
            loop = "sim"
    # FUNÇÃO DE EXCLUIR OS ELEMENTOS
    elif choice == 4:
        os.system('cls')
        if len(id) > 0:
            idDelete = int(
                input("Informe o ID do cadastro que deseja excluir:\n"))
            # VERIFICAÇÃO DA EXISTENCIA DO ID
            if idDelete in id:
                for searchDelete in id:
                    if searchDelete == idDelete:
                        positionDelete = id.index(idDelete)
                confirmationDelete = int(input(
                    "O elemento será excluido permanentemente, gostaria de prosseguir ?\n1 - Sim\n2 - Não\n"))
                if confirmationDelete == 1:
                    id.pop(positionDelete)
                    name.pop(positionDelete)
                    value.pop(positionDelete)
                    size.pop(positionDelete)
                    description.pop(positionDelete)
                    homeRoom.pop(positionDelete)
                    os.system('cls')
                    print(
                        "Cadastro removido com sucesso !\n\nNão esqueça de gravar os dados no menu ! :D")
                    time.sleep(2)
                    os.system('cls')
                elif confirmationDelete == 2:
                    os.system('cls')
                    print("Redirecionando ao menu inicial...\n")
                    time.sleep(2)
                    os.system('cls')
                    loop = "sim"
                else:
                    os.system('cls')
                    print("Opção inválida !\n")
                    time.sleep(2)
                    os.system('cls')
                    print("Retornando ao menu...\n")
                    time.sleep(3)
                    os.system('cls')
                    loop = "sim"
            else:
                os.system('cls')
                print("ID informado inexistente !\n")
                time.sleep(2)
                os.system('cls')
                print("Redirecionando ao menu de opções...\n")
                time.sleep(3)
                os.system('cls')
                loop = "sim"
        else:
            os.system('cls')
            print("Não existe nenhum cadastro no momento !\n")
            time.sleep(2)
            os.system('cls')
            print(
                "Para acessar essa função é necessário um cadastro, redirecionando ao menu...\n")
            time.sleep(4)
            os.system('cls')
            loop = "sim"
    # GRAVA OS DADOS NO ARQUIVO TXT
    elif choice == 5:
        if len(id) > 0:
            os.system('cls')
            with open(r'banco.txt', 'w') as arquivo:
                for i in range(len(id)):
                    arquivo.write(str(id[i])+'\n')
                    arquivo.write(str(name[i])+'\n')
                    arquivo.write(str(value[i])+'\n')
                    arquivo.write(str(size[i])+'\n')
                    arquivo.write(str(homeRoom[i])+'\n')
                    arquivo.write(str(description[i])+'\n')
                print("Dados gravados com sucesso !")
                time.sleep(3)
                os.system('cls')
        # VERIFICA SE EXISTE ALGUM ITEM CADASTRADO
        else:
            os.system('cls')
            print("Não existe nenhum cadastro no momento !\n")
            time.sleep(2)
            os.system('cls')
            print(
                "Para acessar essa função é necessário um cadastro, redirecionando ao menu...\n")
            time.sleep(4)
            os.system('cls')
            loop = "sim"
    # IMPORTA OS DADOS DO ARQUIVO TXT
    elif choice == 6:
        os.system('cls')
        with open(r'banco.txt', 'r+') as arquivo:
            lista = []
            for dado in arquivo:
                lista.append(dado[:-1])
            for i in range(int(len(lista)/6)):
                id.append(int(lista[(i*6)]))
                name.append(lista[(i*6)+1])
                value.append(float(lista[(i*6)+2]))
                size.append(float(lista[(i*6)+3]))
                homeRoom.append(int(lista[(i*6)+4]))
                description.append(lista[(i*6)+5])
            print("Dados importados com sucesso !")
            time.sleep(2)
            os.system('cls')
    # FUNÇÃO DE SAIDA
    elif choice == 7:
        os.system('cls')
        questionSave = (int(input(
            "O programa está fechando, não esqueça de gravar os seus dados no menu >.<\nSelecione:\n1 - Sair\n2 - Voltar ao menu")))
        if questionSave == 1:
            os.system('cls')
            print("Saindo...")
            time.sleep(3)
            os.system('cls')
            loop = "nao"
        elif questionSave == 2:
            os.system('cls')
            print("Retornando ao menu...")
            time.sleep(3)
            os.system('cls')
    # CASO NÃO ESCOLHA NENHUMA OPÇÃO VALIDA
    else:
        os.system('cls')
        print("Opção inválida !\n")
        time.sleep(2)
        os.system('cls')
        print("Escolher opções informadas.\n")
        time.sleep(2)
        os.system('cls')
        print("Redirecionando ao menu...")
        time.sleep(2)
        os.system('cls')
