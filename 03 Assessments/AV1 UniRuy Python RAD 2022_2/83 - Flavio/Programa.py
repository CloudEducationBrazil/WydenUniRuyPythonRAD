# https://github.com/Flavioadm/Cartao?classId=27bd03ab-65b6-4263-90af-50d093a0956a&assignmentId=13d15b99-4d64-423e-8899-741ed1d1f38b&submissionId=b1f9976e-eae8-13b2-6b4a-33016dec52e4
# cartão de crédito

import re
import colorama
import funcoes
import imagens
import time
import os
import sys
import csv

visa = []
master = []
elo = []
outros_nome = []
outros_numero = []

if os.path.exists('visa.csv'):
    with open('visa.csv', 'r') as arquivo:
        visas = csv.reader(arquivo, delimiter=" ")
        for line in visas:
            visa.append(line)

if os.path.exists('master.csv'):
    with open("master.csv", "r") as arquivo:
        masters = csv.reader(arquivo, delimiter=",")
        for line in masters:
            master.append(line)

if os.path.exists('elo.csv'):
    with open("elo.csv", "r") as arquivo:
        elos = csv.reader(arquivo, delimiter=",")
        for line in elos:
            elo.append(line)

if os.path.exists('outros_nome.csv'):
    with open("outros_nome.csv", "r") as arquivo:
        outros_nomes = csv.reader(arquivo, delimiter=",")
        for line in outros_nomes:
            outros_nome.append(line)

if os.path.exists('outros_numero.csv'):
    with open("outros_numero.csv", "r") as arquivo:
        outros_numeros = csv.reader(arquivo, delimiter=",")
        for line in outros_numeros:
            outros_numero.append(line)

imagens.cartao()
funcoes.aguardar()
funcoes.limpar()
imagens.abertura()
funcoes.aguardar()

while(True):

    funcoes.limpar()
    funcoes.opcao()

    try:
        opcao = int(input("Qual a sua opção? \n\n"))

        if (opcao <= 4 and opcao > 0):

            try:
                # ******************************Inicio opção de cadastramento Visa******************************************************
                if (opcao == 1):

                    while(opcao <= 4 and opcao > 0):
                        funcoes.limpar()
                        funcoes.cadastro_cartao()
                        escolha = int(input("Qual a sua escolha?\n\n"))

                        if (escolha == 1):
                            funcoes.limpar()
                            imagens.visa_cartao()
                            funcoes.limpar()

                            numero_visa = input("Qual o número do cartão \n")

                            if (numero_visa in visa):
                                print("Numero do cartão já cadastrado na posição ", visa.index(
                                    numero_visa) + 1, "\n\n")
                                funcoes.pausar()

                            else:

                                visa.append(numero_visa)
                                indice_visa = visa.index(numero_visa)
                                print("Cadastramos seu cartão Visa número ",
                                      numero_visa, " na poisção", indice_visa + 1, "\n\n\n")
                                funcoes.pausar()
# *************************************** Termino cadastramento Visa*********************************************************
# *************************************** Início cadastramento Master*********************************************************
                        elif (escolha == 2):
                            funcoes.limpar()
                            imagens.master_cartao()
                            funcoes.aguardar()
                            funcoes.limpar()
                            numero_master = input("Qual o número do cartão \n")

                            if (numero_master in master):
                                print("Numero do cartão já cadastrado na posição ", master.index(
                                    numero_master) + 1, "\n\n")
                                funcoes.pausar()

                            else:

                                master.append(numero_master)
                                indice_master = master.index(numero_master)
                                print("Cadastramos seu cartão MasterCard número ",
                                      numero_master, " na poisção", indice_master + 1)
                                funcoes.pausar()
# ******************************************** Termino cadastramento Master*********************************************************
# ********************************************** Início cadastramento Elo***********************************************************
                        elif (escolha == 3):
                            funcoes.limpar()
                            imagens.elo_cartao()
                            funcoes.aguardar()
                            funcoes.limpar()

                            numero_elo = input("Qual o número do cartão \n")

                            if (numero_elo in elo):
                                print("Numero do cartão já cadastrado na posição ", elo.index(
                                    numero_elo) + 1, "\n\n")
                                funcoes.pausar()

                            else:

                                elo.append(numero_elo)
                                indice_elo = elo.index(numero_elo)
                                print("Cadastramos seu cartão Elo número ",
                                      numero_elo, " na poisção", indice_elo + 1)
                                funcoes.pausar()
# ******************************************** Termino cadastramento Elo*********************************************************
# *************************************** Início cadastramento Outros Cartões ****************************************************
                        elif (escolha == 4):
                            funcoes.limpar()
                            imagens.cartao()
                            funcoes.aguardar()
                            funcoes.limpar()

                            nome_cartao = input(
                                "Informe o nome do cartão \n\n")
                            numero_outros = input(
                                "\n\n Qual número do cartão \n\n")

                            if(numero_outros in outros_numero):
                                print("Numero do cartão já cadastrado na posição ", elo.index(
                                    numero_elo) + 1, "\n\n")
                                funcoes.pausar()

                            else:
                                outros_nome.append(nome_cartao)
                                outros_numero.append(numero_outros)

                            indice_outros_nome = outros_nome.index(nome_cartao)
                            indice_outros_numero = outros_numero.index(
                                numero_outros)

                            if(indice_outros_nome != indice_outros_numero):
                                print("Lista corrompida, chame o adm de sistema")
                                funcoes.pausar()

                            print("Cadastramos seu cartão", nome_cartao, " número ",
                                  numero_outros, " na posição", indice_outros_nome + 1)
                            funcoes.pausar()
# *************************************** Termino cadastramento Outros Cartões ****************************************************

                        elif (escolha == 5):  # Retornar para o menu anterior
                            funcoes.limpar()
                            break

                        else:  # Entrada de dados invalida
                            imagens.meme()

# ******************************************* Início consulta de cartões***********************************************************
# ******************************************* Início consulta cartões Visa*********************************************************
                elif (opcao == 2):
                    funcoes.limpar()
                    funcoes.consulta_cartao()
                    opcao_consulta = int(input("Qual a sua escolha? \n\n"))

                    if (opcao_consulta == 1):
                        funcoes.limpar()
                        for x in range(len(visa)):
                            novo = visa[x]
                            print("Seu cartão Visa cadastrado na posição ",
                                  x + 1, " é o de número ", visa[x], "\n\n\n")

                        funcoes.pausar()
                        funcoes.limpar()
# ******************************************* Início consulta cartões Master*********************************************************
                    elif (opcao_consulta == 2):
                        funcoes.limpar()
                        for x in range(len(master)):
                            print("Seu cartão Master cadastrado na posição ",
                                  x + 1, " é o de número ", master[x], "\n\n\n")

                        funcoes.pausar()
                        funcoes.limpar()
# ******************************************* Início consulta cartões Elo *********************************************************
                    elif (opcao_consulta == 3):
                        funcoes.limpar()
                        for x in range(len(elo)):
                            print("Seu cartão Elo cadastrado na posição ",
                                  x + 1, " é o de número ", elo[x], "\n\n\n")

                        funcoes.pausar()
                        funcoes.limpar()
# ******************************************* Início consulta cartões Outros cartões**************************************************
                    elif (opcao_consulta == 4):
                        funcoes.limpar()
                        for x in range(len(outros_numero)):
                            print("Seu cartão", (outros_nome[x]), "cadastrado na posição ",
                                  x + 1, " é o de número ", (outros_numero[x]), "\n\n\n")

                        funcoes.pausar()
                        funcoes.limpar()
# ******************************************* Início consulta todos os cartões*********************************************************
                    elif(opcao_consulta == 5):
                        funcoes.limpar()
                        for x in range(len(visa)):
                            print("Seu cartão Visa cadastrado na posição ",
                                  x + 1, " é o de número ", visa[x], "\n\n\n")

                        funcoes.pausar()
                        funcoes.limpar()

                        for x in range(len(master)):
                            print("Seu cartão Master cadastrado na posição ",
                                  x + 1, " é o de número ", master[x], "\n\n\n")

                        funcoes.pausar()
                        funcoes.limpar()

                        for x in range(len(elo)):
                            print("Seu cartão Elo cadastrado na posição ",
                                  x + 1, " é o de número ", elo[x], "\n\n\n")

                        funcoes.pausar()
                        funcoes.limpar()

                        for x in range(len(outros_numero)):
                            print("Seu cartão", (outros_nome[x]), "cadastrado na posição ",
                                  x + 1, " é o de número ", (outros_numero[x]), "\n\n\n")

                        funcoes.pausar()
                        funcoes.limpar()

                    elif(opcao_consulta == 6):  # Retornar para o menu anterior
                        funcoes.limpar()
                        # break

                    else:
                        imagens.meme()  # Entrada de dados invalida

# ******************************************* Termino da função de consulta de cartões***************************************************
# ******************************************* Inicio da função de exlusão de cartões*****************************************************
                elif (opcao == 3):  # Inicio Visa****************************************************************************************
                    funcoes.limpar()
                    funcoes.exclusao_cartao()
                    escolha = int(input("Qual a sua opção?\n\n"))

                    if (escolha == 1):

                        funcoes.exclusao_cartao2()

                        tipo_exclusao = int(input("Informe o número "))

                        if (tipo_exclusao == 1):

                            numero_excluir = int(
                                input("Informe o número do cartão visa a ser excluido. \n\n"))

                            if (numero_excluir in visa):

                                posicao = visa.index(numero_excluir)

                                print("Tem certeza que deseja excluir o cartão Visa número ",
                                      numero_excluir, " o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    visa.remove(numero_excluir)
                                    print("Cartão excluido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não ")
                                    funcoes.pausar()
                            else:
                                print(
                                    "Não existe cartão com esse número, favor repetir a operação ")
                                funcoes.pausar()

                        elif(tipo_exclusao == 2):

                            posicao = int(
                                input("Qual a posição do cartão Visa? \n"))

                            posicao = posicao - 1

                            if posicao in range(len(visa)):
                                print("Tem certeza que deseja excluir o cartão Visa número ",
                                      visa[posicao], " o cartão está cadastrado na posição: ", posicao + 1)

                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    visa.pop(posicao)
                                    print("Cartão excluido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:

                                print("Não existe a posição ", posicao + 1,
                                      " no cartão escolhido, a maior posição é a posição ", (len(visa)) + 1)
                                funcoes.pausar()

                        elif(tipo_exclusao == 3):
                            print(
                                "Tem certeza que deseja excluir todos os cartões Visa? ")

                            confirmacao = input("Digite Sim ou Não ")

                            if(confirmacao.upper() == "SIM"):
                                visa.clear()
                                print("Cartões excluido com sucesso ")
                                funcoes.pausar()

                            elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                print("Cartão não excluido ")
                                funcoes.pausar()

                            else:
                                print(
                                    "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                funcoes.pausar()

                        else:
                            imagens.meme()
# ******************************************* Termino da função de exclusão de cartões Visa**********************************************
# ******************************************* Inicio da função de consulta de exlusão de Master******************************************
                    elif (escolha == 2):
                        funcoes.limpar()
                        funcoes.exclusao_cartao2()

                        tipo_exclusao = int(input("Informe o número"))

                        if (tipo_exclusao == 1):

                            numero_excluir = int(
                                input("Informe o número do cartão Mastercard a ser excluido. \n\n"))

                            if (numero_excluir in master):

                                posicao = master.index(numero_excluir)

                                print("Tem certeza que deseja excluir o cartão Master número ",
                                      numero_excluir, " o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    master.remove(numero_excluir)
                                    print("Cartão excluido com sucesso ")

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")

                            else:
                                print(
                                    "Não existe cartão com esse número, favor repetir a operação ")
                                funcoes.pausar()

                        elif(tipo_exclusao == 2):

                            posicao = int(
                                input("Qual a posição do cartão Master? \n"))

                            posicao = posicao - 1

                            if posicao in range(len(master)):
                                print("Tem certeza que deseja excluir o cartão Master número ",
                                      master[posicao], " o cartão está cadastrado na posição: ", posicao + 1)

                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    master.pop(posicao)
                                    print("Cartão excluido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:

                                print("Não existe a posição ", posicao + 1,
                                      " no cartão escolhido, a maior posição é a posição ", (len(master)) + 1)
                                funcoes.pausar()

                        elif(tipo_exclusao == 3):
                            print(
                                "Tem certeza que deseja excluir todos os cartões Master? ")

                            confirmacao = input("Digite Sim ou Não ")

                            if(confirmacao.upper() == "SIM"):
                                master.clear()
                                print("Cartões excluido com sucesso ")
                                funcoes.pausar()

                            elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                print("Cartão não excluido ")
                                funcoes.pausar()

                            else:
                                print(
                                    "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                funcoes.pausar()
                        else:
                            imagens.meme()
# ******************************************* Termino da função de exclusão de cartões Master**********************************************
# ******************************************* Inicio da função de consulta de exlusão de Elo******************************************
                    elif (escolha == 3):

                        funcoes.exclusao_cartao2()

                        tipo_exclusao = int(input("Informe o número"))

                        if (tipo_exclusao == 1):

                            numero_excluir = int(
                                input("Informe o número do cartão Elo a ser excluido. \n\n"))

                            if (numero_excluir in elo):

                                posicao = elo.index(numero_excluir)

                                print("Tem certeza que deseja excluir o cartão Elo número ",
                                      numero_excluir, " o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    elo.remove(numero_excluir)
                                    print("Cartão excluido com sucesso ")

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")

                            else:
                                print(
                                    "Não existe cartão com esse número, favor repetir a operação ")
                                funcoes.pausar()

                        elif(tipo_exclusao == 2):

                            posicao = int(
                                input("Qual a posição do cartão Elo? \n"))

                            posicao = posicao - 1

                            if posicao in range(len(elo)):
                                print("Tem certeza que deseja excluir o cartão Elo número ",
                                      elo[posicao], " o cartão está cadastrado na posição: ", posicao + 1)

                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    elo.pop(posicao)
                                    print("Cartão excluido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:

                                print("Não existe a posição ", posicao + 1,
                                      " no cartão escolhido, a maior posição é a posição ", (len(elo)) + 1)
                                funcoes.pausar()

                        elif(tipo_exclusao == 3):
                            print(
                                "Tem certeza que deseja excluir todos os cartões Elo? ")

                            confirmacao = input("Digite Sim ou Não ")

                            if(confirmacao.upper() == "SIM"):
                                elo.clear()
                                print("Cartões excluido com sucesso ")
                                funcoes.pausar()

                            elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                print("Cartão não excluido ")
                                funcoes.pausar()

                            else:
                                print(
                                    "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                funcoes.pausar()
                        else:
                            imagens.meme()
# ******************************************* Termino da função de exclusão de cartões Elo**********************************************
# ******************************************* Inicio da função de consulta de exlusão de Outros******************************************
                    elif (escolha == 4):

                        funcoes.exclusao_cartao2()

                        tipo_exclusao = int(input("Informe o número"))

                        if (tipo_exclusao == 1):

                            numero_excluir = int(
                                input("Informe o número do cartão a ser excluido. \n\n"))

                            if (numero_excluir in outros_numero):

                                posicao = outros_numero.index(numero_excluir)

                                print("Tem certeza que deseja excluir o cartão ",
                                      nome_cartao[posicao], "número ", numero_excluir, " o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    outros_nome.pop(posicao)
                                    outros_numero.pop(posicao)
                                    print("Cartão excluido com sucesso ")

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")

                            else:
                                print(
                                    "Não existe cartão com esse número, favor repetir a operação ")
                                funcoes.pausar()

                        elif(tipo_exclusao == 2):

                            posicao = int(
                                input("Qual a posição do cartão Master? \n"))

                            posicao = posicao - 1

                            if posicao in range(len(master)):
                                print("Tem certeza que deseja excluir o cartão ",
                                      nome_cartao[posicao], "número ", numero_excluir, " o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    outros_nome.pop(posicao)
                                    outros_numero.pop(posicao)
                                    print("Cartão excluido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:

                                print("Não existe a posição ", posicao + 1,
                                      " no cartão escolhido, a maior posição é a posição ", (len(master)) + 1)
                                funcoes.pausar()

                        elif(tipo_exclusao == 3):
                            print(
                                "Tem certeza que deseja excluir todos os cartões? ")
                            confirmacao = input("Digite Sim ou Não ")

                            if(confirmacao.upper() == "SIM"):
                                outros_nome.clear()
                                outros_numero.clear()
                                print("Cartões excluido com sucesso ")
                                funcoes.pausar()

                            elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                print("Cartão não excluido ")
                                funcoes.pausar()

                            else:
                                print(
                                    "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                funcoes.pausar()

# ******************************************* Termino da função de exclusão de cartões Outros**********************************************
                        else:  # Entrada de dados invalida
                            imagens.meme()

# ******************************************* Termino da função de exclusão de cartões ****************************************************
# ******************************************* Inicio da função de substituição de cartões*****************************************************
                elif (opcao == 4):  # Inicio Visa****************************************************************************************

                    funcoes.substituir_cartao()
                    escolha = int(input("Qual a sua opção?\n\n"))

                    if (escolha == 1):

                        funcoes.substituir_cartao2()

                        tipo_substituicao = int(
                            input("Informe sua escolha \n\n"))

                        if (tipo_substituicao == 1):

                            numero_substituir = int(
                                input("Informe o número do cartão visa a ser substituido. \n\n"))
                            novo_cartao = int(
                                input("Informe o novo número do cartão "))

                            if (numero_substituir in visa):

                                posicao = visa.index(numero_substituir)

                                print("Tem certeza que deseja substituir o cartão Visa número ", numero_substituir,
                                      " por cartão visa número ", novo_cartao, "o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    visa[posicao] = novo_cartao
                                    print("Cartão substituido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não substituido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:
                                print(
                                    "Não existe cartão com esse número, favor repetir a operação ")
                                funcoes.pausar()

                        elif(tipo_substituicao == 2):

                            posicao = int(
                                input("Qual a posição do cartão Visa? \n"))

                            posicao = posicao - 1

                            if posicao in range(len(visa)):
                                print("Tem certeza que deseja substituir o cartão Visa número ",
                                      visa[posicao], " o cartão está cadastrado na posição: ", posicao + 1)

                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    novo_cartao = int(
                                        input("Informe o novo número do cartão "))
                                    visa[posicao] = novo_cartao
                                    print("Cartão substituido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não substituido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:

                                print("Não existe a posição ", posicao + 1,
                                      " no cartão escolhido, a maior posição é a posição ", (len(visa)) + 1)
                                funcoes.pausar()
                        else:
                            imagens.meme()
# ******************************************* Termino da função de substituição de cartões Visa**********************************************
# ******************************************* Inicio da função de consulta de substituição de Master******************************************

                    elif (escolha == 2):

                        funcoes.substituir_cartao2()

                        tipo_substituicao = int(
                            input("Informe o sua escolha \n\n"))

                        if (tipo_substituicao == 1):

                            numero_substituir = int(
                                input("Informe o número do cartão Master a ser substituido. \n\n"))
                            novo_cartao = int(
                                input("Informe o novo número do cartão "))

                            if (numero_substituir in master):

                                posicao = master.index(numero_substituir)

                                print("Tem certeza que deseja substituir o cartão Master número ", numero_substituir,
                                      " por cartão Master número ", novo_cartao, "o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    master[posicao] = novo_cartao
                                    print("Cartão substituido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não substituido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:
                                print(
                                    "Não existe cartão com esse número, favor repetir a operação ")
                                funcoes.pausar()

                        elif(tipo_substituicao == 2):

                            posicao = int(
                                input("Qual a posição do cartão Master? \n"))

                            posicao = posicao - 1

                            if posicao in range(len(master)):
                                print("Tem certeza que deseja substituir o cartão Visa número ",
                                      master[posicao], " o cartão está cadastrado na posição: ", posicao + 1)

                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    novo_cartao = int(
                                        input("Informe o novo número do cartão "))
                                    master[posicao] = novo_cartao
                                    print("Cartão substituido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não substituido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:

                                print("Não existe a posição ", posicao + 1,
                                      " no cartão escolhido, a maior posição é a posição ", (len(visa)) + 1)
                                funcoes.pausar()
                        else:
                            imagens.meme()

# ******************************************* Termino da função de substituição de cartões Master**********************************************
# ******************************************* Inicio da função de consulta de substituição de Elo******************************************

                    elif (escolha == 3):

                        funcoes.substituir_cartao2()

                        tipo_substituicao = int(
                            input("Informe o sua escolha \n\n"))

                        if (tipo_substituicao == 1):

                            numero_substituir = int(
                                input("Informe o número do cartão a ser substituido. \n\n"))

                            if (numero_substituir in elo):

                                nome_novo_cartao = input(
                                    "Informe o nome do novo cartão \n\n")
                                novo_cartao = int(
                                    input("Informe o novo número do cartão \n\n"))
                                posicao = elo.index(numero_substituir)

                                print("Tem certeza que deseja substituir o cartão Elo número ", numero_substituir,
                                      " por cartão Elo número ", novo_cartao, "o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    elo[posicao] = novo_cartao
                                    print("Cartão substituido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não substituido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:
                                print(
                                    "Não existe cartão com esse número, favor repetir a operação ")
                                funcoes.pausar()

                        elif(tipo_substituicao == 2):

                            posicao = int(
                                input("Qual a posição do cartão elo? \n"))

                            posicao = posicao - 1

                            if posicao in range(len(elo)):
                                print("Tem certeza que deseja substituir o cartão Visa número ",
                                      elo[posicao], " o cartão está cadastrado na posição: ", posicao + 1)

                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    novo_cartao = int(
                                        input("Informe o novo número do cartão "))
                                    elo[posicao] = novo_cartao
                                    print("Cartão substituido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não substituido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:

                                print("Não existe a posição ", posicao + 1,
                                      " no cartão escolhido, a maior posição é a posição ", (len(visa)) + 1)
                                funcoes.pausar()
                        else:
                            imagens.meme()

# ******************************************* Termino da função de substituição de cartões Elo**********************************************
# ******************************************* Inicio da função de consulta de substituição de Outros******************************************
                    elif (escolha == 4):

                        funcoes.substituir_cartao2()

                        tipo_substituicao = int(
                            input("Informe sua escolha \n\n"))

                        if (tipo_substituicao == 1):

                            numero_substituir = int(
                                input("Informe o número do cartão a ser substituido. \n\n"))

                            if (numero_substituir in outros_numero):

                                posicao = outros_numero.index(
                                    numero_substituir)

                                print("Tem certeza que deseja substituir o cartão ",
                                      nome_cartao[posicao], "número ", numero_substituir, " o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    novo_nome_cartao = input(
                                        "Informe o nome do novo cartão \n\n")
                                    novo_numero_cartao = int(
                                        input("Informe o novo número do cartão \n\n"))
                                    outros_nome[posicao] = novo_nome_cartao
                                    outros_numero[posicao] = novo_numero_cartao
                                    print("Cartão substituido com sucesso ")

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não substituido ")

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")

                            else:
                                print(
                                    "Não existe cartão com esse número, favor repetir a operação ")
                                funcoes.pausar()

                        elif(tipo_substituicao == 2):

                            posicao = int(
                                input("Qual a posição do cartão ? \n"))

                            posicao = posicao - 1

                            if posicao in range(len(outros_numero)):
                                print("Tem certeza que deseja substituir o cartão ",
                                      nome_cartao[posicao], "número ", numero_substituir, " o cartão está cadastrado na posição: ", posicao + 1)
                                confirmacao = input("Digite Sim ou Não ")

                                if(confirmacao.upper() == "SIM"):
                                    novo_nome_cartao = input(
                                        "Informe o nome do novo cartão \n\n")
                                    novo_numero_cartao = int(
                                        input("Informe o novo número do cartão \n\n"))
                                    outros_nome[posicao] = novo_nome_cartao
                                    outros_numero[posicao] = novo_numero_cartao
                                    print("Cartão substituido com sucesso ")
                                    funcoes.pausar()

                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não substituido ")
                                    funcoes.pausar()

                                else:
                                    print(
                                        "Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    funcoes.pausar()
                            else:

                                print("Não existe a posição ", posicao + 1,
                                      " no cartão escolhido, a maior posição é a posição ", (len(master)) + 1)
                                funcoes.pausar()
# ******************************************* Termino da função de substituição de cartões Outros**********************************************
                        else:  # Entrada de dados invalida
                            imagens.meme()

                else:  # Entrada de dados invalida

                    imagens.meme()
# ******************************************* Termino da função de substituição de cartões ****************************************************

            except:
                imagens.meme()

        elif(opcao == 9):

            funcoes.limpar()
            with open("visa.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever = csv.writer(
                    arquivo, delimiter=',', lineterminator='\n')
                for x in range(len(visa)):
                    numero = visa[x]
                    escrever.writerow(numero)

            with open("master.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever = csv.writer(
                    arquivo, delimiter=',', lineterminator='\n')
                for x in range(len(master)):
                    numero = master[x]
                    escrever.writerow(numero)

            with open("elo.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever = csv.writer(
                    arquivo, delimiter=',', lineterminator='\n')
                for x in range(len(elo)):
                    numero = elo[x]
                    escrever.writerow(numero)

            with open("outros_nome.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever = csv.writer(
                    arquivo, delimiter=',', lineterminator='\n')
                for x in range(len(outros_nome)):
                    numero = outros_nome[x]
                    escrever.writerow(numero)

            with open("outros_numero.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever = csv.writer(
                    arquivo, delimiter=',', lineterminator='\n')
                for x in range(len(outros_numero)):
                    numero = master[x]
                    escrever.writerow(numero)

            print("Até a proxima\n\n\n")
            imagens.sair()
            funcoes.aguardar()
            funcoes.limpar()
            break

        else:
            imagens.meme()

    except:
        imagens.meme()
