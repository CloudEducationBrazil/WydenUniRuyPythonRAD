#IMPORTS
# Angelo Nascimento
# https://github.com/A21n13g0/Ordem-de-Servico?classId=27bd03ab-65b6-4263-90af-50d093a0956a&assignmentId=13d15b99-4d64-423e-8899-741ed1d1f38b&submissionId=c8d74fc2-cf79-d081-ba95-2d70b350f67c
# CRUD - Ordem de Serviço

from os import system
from time import sleep
import locale
import datetime
import validation

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#VARIAVEIS GLOBAIS
services = dict()
id = 1

#MENU PRINCIPAL DA APLICAÇÃO
def Main():
    system("cls")
    print("\n.:APLICAÇÃO DE CADASTRO DE ORDEM DE SERVIÇO:.\n")

    print("1-Cadastrar Ordem de Serviço \n2-Pesquisar Ordem de Serviço \n3-Atualizar Ordem de Serviço")
    print("4-Excluir Ordem de Serviço \n5-Exportar Ordens de Serviço Para TXT \n6-Visualizar Serviços Exportados")
    print("7-Sair")
    op = input("\nOpção: ")

    if op == '1':
        createService()
    elif op == '2':
        menuFind()
    elif op == '3':
        updateService()
    elif op == '4':
        deleteService()
    elif op == '5':
        exportaTxt()
    elif op == '6':
        readTxt()
    elif op == '7':
        exitApp()
    else:
        print("\nOpção Invalida, Tente Novamente!")
        sleep(3)
        Main()

# CADASTRA ORDEM DE SERVIÇO
def createService():
    system("cls")
    print("\n.:CADASTRO DE ORDEM DE SERVIÇO:.\n")
    global id

    while(id != 0):
        typeService = input("Informe o Tipo de Serviço: ")
        descriptionService = input("Descreva o Serviço: ")
        date = input("Data de Realização do Serviço: ")
        provider = input("Informe o Prestador do Serviço: ")
        client = input("Informe o Cliente que Receberá o Serviço: ")
        value = input('Informe o valor do Serviço: ')

        if validation.isData(date) == False:
            print("\nA Data Deve Ser Informada como dd/mm/aaaa!")
            sleep(3)
            createService()
        else:
            dateService = datetime.datetime.strptime(str(date), '%d/%m/%Y').strftime('%d/%m/%Y')

        if validation.isNumeric(value) == False:
            print("\nValor do serviço invalido, digite apenas valores numericos!")
            sleep(3)
            createService()
        else:
            valueService = validation.coin(value)

        services[id] = {'ID': id, 'TIPO_SERVICO' : typeService, 'DESCRICAO_SERVICO' : descriptionService, 'DATA_SERVICO' : dateService, 'PRESTADOR' : provider, 'CLIENTE' : client, 'VALOR' : valueService}

        id+=1

        print("\nCadastro Realizado Com Sucesso!")
        sleep(3)
        menuCreate()


#LISTA TODAS AS ORDENS DE SERVIÇO
def listAll():
    system('cls')
    print("\n.:ORDENS DE SERVIÇO:.\n")
    service = 1

    for service in services.keys():
        print("\n")
        print("ID: " + str(services[service]['ID']))
        print("TIPO DE SERVICO: " + services[service]['TIPO_SERVICO'])
        print("DESCRICAO DO SERVICO: " + services[service]['DESCRICAO_SERVICO'])
        print("DATA DO SERVICO: " + services[service]['DATA_SERVICO'])
        print("PRESTADOR DO SERVICO: " + services[service]['PRESTADOR'])
        print("CLIENTE: " + services[service]['CLIENTE'])
        print("VALOR: " + services[service]['VALOR'])
        print("------------------------")
        service+=1
    
    menuFind()

#PESQUISA ORDEM DE SERVIÇO POR ID
def findId():
    system('cls')
    print("\n.:ORDEM DE SERVIÇO:.\n")
    service = input("Informe o ID do Serviço: ")

    if validation.isInt(service) == False:
            print("ID invalido, Tente Novamente!")
            sleep(3)
            findId()
    else:
        idService = int(service)

    if idService in services:
        for service in services.items():
            print("\n")
            print("ID: " + str(services[idService]['ID']))
            print("TIPO DE SERVICO: " + services[idService]['TIPO_SERVICO'])
            print("DESCRICAO DO SERVICO: " + services[idService]['DESCRICAO_SERVICO'])
            print("DATA DO SERVICO: " + services[idService]['DATA_SERVICO'])
            print("PRESTADOR DO SERVICO: " + services[idService]['PRESTADOR'])
            print("CLIENTE: " + services[idService]['CLIENTE'])
            print("VALOR: " + services[idService]['VALOR'])
            print("------------------------")
    else:
        print("\nOrdem de Serviço Inexistente!")
        sleep(3)

    menuFind()

#ATUALIZA ORDEM DE SERVIÇO
def updateService():
    system('cls')
    print("\n.:ATUALIZAR ORDEM DE SERVIÇO:.\n")
    service = input("Informe o ID do Serviço: ")

    if validation.isInt(service) == False:
            print("ID invalido, Tente Novamente!")
            sleep(3)
            findId()
    else:
        idService = int(service)

    for service in services.items():
        if idService in service:
            print("\n")
            print("ID: " + str(services[idService]['ID']))
            print("TIPO DE SERVICO: " + services[idService]['TIPO_SERVICO'])
            print("DESCRICAO DO SERVICO: " + services[idService]['DESCRICAO_SERVICO'])
            print("DATA DO SERVICO: " + services[idService]['DATA_SERVICO'])
            print("PRESTADOR DO SERVICO: " + services[idService]['PRESTADOR'])
            print("CLIENTE: " + services[idService]['CLIENTE'])
            print("VALOR: " + services[idService]['VALOR'])
            print("------------------------")

            print("\n1-Atualizar Tipo de Serviço \n2-Atualizar Descrição do Serviço \n3-Atualizar Data do Serviço")
            print("\n4-Atualizar Prestador do Serviço \n5-Atualizar Cliente \n6-Atualizar Valor do Serviço")
            op = input('\nOpção: ')

            if op == '1':
                services[idService]['TIPO_SERVICO'] = input("\nInforme o Tipo de Serviço: ")
            elif op == '2':
                services[idService]['DESCRICAO_SERVICO'] = input("\nDescreva o Serviço: ")
            elif op == '3':
                services[idService]['DATA_SERVICO'] = input("\nData de Realização do Serviço: ")

                if validation.isData(services[idService]['DATA_SERVICO']) == False:
                    print("\nA Data Deve Ser Informada como dd/mm/aaaa!")
                    sleep(3)
                    updateService()
                else:
                    dateService = datetime.datetime.strptime(str(services[idService]['DATA_SERVICO']), '%d/%m/%Y').strftime('%d/%m/%Y')

            elif op == '4':
                services[service]['PRESTADOR'] = input("\nInforme o Prestador do Serviço: ")
            elif op == '5':
                services[idService]['CLIENTE'] = input("\nInforme o Cliente que Receberá o Serviço: ")
            elif op == '6':
                value = input('\nInforme o valor do Serviço: ')

                if validation.isNumeric(value) == False:
                    print("\nValor do serviço invalido, digite apenas valores numericos!")
                    sleep(3)
                    updateService()
                else:
                    services[idService]['VALOR'] = validation.coin(value)

            else:
                print("\nOpção Invalida, Tente Novamente!")
                sleep(3)
                updateService()
        else:
            print("\nOrdem de Serviço Inexistente!")
            sleep(3)

    menuUpdate()

#REMOVE ORDEM DE SERVIÇO
def deleteService():
    system('cls')
    print("\n.:EXCLUIR DE ORDEM DE SERVIÇO:.\n")
    service = input("Informe o ID do Serviço: ")

    if validation.isInt(service) == False:
            print("ID invalido, Tente Novamente!")
            sleep(3)
            findId()
    else:
        idService = int(service)

    if idService in services:
        services.pop(idService)
        print("\nOrdem de Serviço Removida com Sucesso!")
    else:
        print("\nOrdem de Serviço Inexistente!")

    menuDelete()

#SALVA ORDEM DE SERVIÇO EM ARQUIVO .TXT
def exportaTxt():
    with open("servicos.txt", "w") as arquivo:
        service = 1
        for service in services.keys():
            print("\n")
            arquivo.write("ID: " + str(services[service]['ID']) + '\n')
            arquivo.write("TIPO DE SERVICO: " + services[service]['TIPO_SERVICO'] + '\n')
            arquivo.write("DESCRICAO DO SERVICO: " + services[service]['DESCRICAO_SERVICO'] + '\n')
            arquivo.write("DATA DO SERVICO: " + services[service]['DATA_SERVICO'] + '\n')
            arquivo.write("PRESTADOR DO SERVICO: " + services[service]['PRESTADOR'] + '\n')
            arquivo.write("CLIENTE: " + services[service]['CLIENTE'] + '\n')
            arquivo.write("VALOR: " + services[service]['VALOR'] + '\n\n')
            service+=1
    print("\nInformações Salvas com Sucesso!\n")
    sleep(3)
    menuExportaTxt()
            

#EXIBE DADOS DO ARQUIVO .TXT
def readTxt():
    system('cls')
    try:
        with open("servicos.txt", "r") as arquivo:
            service = arquivo.read()
            print('\n' + service)
    except:
        print("Exporte os Dados Cadastrados para Ler o Arquivo!")
        
    wait = input("\nPressione Enter para Continuar\n")
    menuReadTxt()

#MENU DE CADASTRO DA ORDEM DE SERVIÇO
def menuCreate():
    system('cls')
    print("\n1-Repetir Operação")
    print("2-Retornar ao Menu")
    op = input("\nOpção: ")

    if op == '1':
        createService()
    elif op == '2':
        Main()
    else:
        print("\n\nOpção Invalida!\nApenas é Possivel Selecionar de 1 ou 2.\n")
        sleep(3)
        system("cls")
        menuCreate()

#MENU DE CONSULTA DA ORDEM DE SERVIÇO
def menuFind():
    print("\n1-Listar Todos os Registros")
    print("2-Procurar Ordem de Serviço")
    print("3-Retornar ao Menu")
    op = input("\nOpção: ")

    if op == '1':
        listAll()
    elif op == '2':
        findId()
    elif op == '3':
        Main()
    else:
        print("\n\nOpção Invalida!\nApenas é Possivel Selecionar de 1 ou 2.\n")
        sleep(3)
        system("cls")
        menuFind()

#MENU DE ATUALIZAÇÃO DA ORDEM DE SERVIÇO
def menuUpdate():
    system('cls')
    print("\n1-Repetir Operação")
    print("2-Retornar ao Menu")
    op = input("\n Opção: ")

    if op == '1':
        updateService()
    elif op == '2':
        Main()
    else:
        print("\n\nOpção Invalida!\nApenas é Possivel Selecionar de 1 ou 2.\n")
        sleep(3)
        system("cls")
        menuUpdate()

#MENU DE EXCLUSÃO DA ORDEM DE SERVIÇO
def menuDelete():
    system('cls')
    print("\n1-Repetir Operação")
    print("2-Retornar ao Menu")
    op = input("\n Opção: ")

    if op == '1':
        deleteService()
    elif op == '2':
        Main()
    else:
        print("\n\nOpção Invalida!\nApenas é Possivel Selecionar de 1 ou 2.\n")
        sleep(3)
        system("cls")
        menuDelete()

#MENU DE EXPORTAÇÃO DA ORDEM DE SERVIÇO
def menuExportaTxt():
    system('cls')
    print("\n1-Repetir Operação")
    print("2-Retornar ao Menu")
    op = input("\n Opção: ")

    if op == '1':
        exportaTxt()
    elif op == '2':
        Main()
    else:
        print("\n\nOpção Invalida!\nApenas é Possivel Selecionar de 1 ou 2.\n")
        sleep(3)
        system("cls")
        menuExportaTxt()

#MENU DE LEITURA DO ARQUIVO TXT
def menuReadTxt():
    system('cls')
    print("\n1-Repetir Operação")
    print("2-Retornar ao Menu")
    op = input("\n Opção: ")

    if op == '1':
        readTxt()
    elif op == '2':
        Main()
    else:
        print("\n\nOpção Invalida!\nApenas é Possivel Selecionar de 1 ou 2.\n")
        sleep(3)
        system("cls")
        menuReadTxt()

#SAIR DA APLICAÇÃO
def exitApp():
    system('cls')
    exit()

#EXECUTA A APLICAÇÃO
Main()