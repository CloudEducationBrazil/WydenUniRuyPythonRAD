import colorama
import funcoes
import time
import os
import sys


visa = []
master = []
elo = []
outros_nome = []
outros_numero = []

funcoes.limpar()
print(colorama.Back.WHITE)
print(colorama.Fore.BLACK)
funcoes.cartao()
#funcoes.aguardar()
print(colorama.Back.RESET)
print(colorama.Fore.RESET)
funcoes.limpar()
funcoes.abertura()
#funcoes.aguardar()


while(True):

    funcoes.limpar()
    funcoes.opcao()

    try:
        opcao = int(input("Qual a sua opção? \n\n"))
                                    
        if (opcao <= 4 and opcao > 0):

            try:

                if (opcao == 1):

                    while(opcao <= 4 and opcao > 0):
                        funcoes.limpar()                       
                        funcoes.cadastro_cartao()                   
                        escolha = int(input("Qual a sua escolha?\n\n"))
                        
                        if (escolha == 1):
                            funcoes.limpar()
                            #funcoes.visa_cartao()
                            #funcoes.aguardar()
                            funcoes.limpar()
                    
                            numero_visa = int(input("Qual o número do cartão \n"))

                            if (numero_visa in visa):
                                print("Numero do cartão já cadastrado na posição ", visa.index(numero_visa) + 1, "\n\n")
                                input("Aperte ENTER para continuar")
                                                            
                            else:

                                visa.append(numero_visa)
                                indice_visa = visa.index(numero_visa)
                                print("Cadastramos seu cartão Visa número ", numero_visa, " na poisção", indice_visa + 1, "\n\n\n")
                                input("Aperte ENTER para continuar")
                            
                        elif (escolha == 2):
                            funcoes.limpar()
                            funcoes.master_cartao()
                            #funcoes.aguardar()
                            funcoes.limpar()
                            numero_master = int(input("Qual o número do cartão \n"))

                            if (numero_master in master):
                                print("Numero do cartão já cadastrado na posição ", master.index(numero_master) + 1, "\n\n")
                                input("Aperte ENTER para continuar")

                            else:

                                master.append(numero_master)
                                indice_master = master.index(numero_master)
                                print("Cadastramos seu cartão MasterCard número ", numero_master, " na poisção", indice_master + 1 )
                                input("Aperte ENTER para continuar")

                        elif (escolha == 3):
                            funcoes.limpar()
                            funcoes.elo_cartao()
                            #funcoes.aguardar()
                            funcoes.limpar()

                            numero_elo = int(input("Qual o número do cartão \n"))

                            if (numero_elo in elo):
                                print("Numero do cartão já cadastrado na posição ", elo.index(numero_elo) + 1, "\n\n")
                                input("Aperte ENTER para continuar")

                            else:

                                elo.append(numero_elo)
                                indice_elo = elo.index(numero_elo)
                                print("Cadastramos seu cartão Elo número ", numero_elo, " na poisção", indice_elo + 1 )
                                input("Aperte ENTER para continuar")

                        elif (escolha == 4):
                            funcoes.limpar()
                            funcoes.abertura()
                            #funcoes.aguardar()
                            funcoes.limpar()
                                                        
                            nome_cartao = input("Informe o nome do cartão \n\n")
                            numero_outros = int(input("\n\n Qual número do cartão \n\n"))

                            if(numero_outros in outros_numero):
                                print("Numero do cartão já cadastrado na posição ", elo.index(numero_elo) + 1, "\n\n")
                                input("Aperte ENTER para continuar")

                            else:
                                outros_nome.append(nome_cartao)
                                outros_numero.append(numero_outros)

                            indice_outros_nome = outros_nome.index(nome_cartao)
                            indice_outros_numero = outros_numero.index(numero_outros)

                            if(indice_outros_nome != indice_outros_numero):
                                print("Lista corrompida, chame o adm de sistema")
                                input("Aperte ENTER para continuar")


                            print("Cadastramos seu cartão", nome_cartao," número ", numero_outros, " na posição", indice_outros_nome + 1)
                            input("Aperte ENTER para continuar")

                        elif (escolha == 5):
                            funcoes.limpar()
                            break

                        else:
                            funcoes.meme()

                        
                elif (opcao == 2):
                    funcoes.limpar()
                    funcoes.consulta_cartao()
                    opcao_consulta = int(input("Qual a sua escolha? \n\n"))

                    if (opcao_consulta == 1):

                        x = 0

                        for x in range (len(visa)):
                            print("Seu cartão Visa cadastrado na posição ", x + 1, " é o de número ", visa[x], "\n\n\n")
                    
                        funcoes.pausar()                   
                        funcoes.limpar()

                    elif (opcao_consulta == 2):

                        x = 0

                        for x in range (len(master)):
                            print("Seu cartão Master cadastrado na posição ", x + 1, " é o de número ", master[x], "\n\n\n")
                    
                        funcoes.pausar()                   
                        funcoes.limpar()
                    
                    elif (opcao_consulta == 3):

                        x = 0

                        for x in range (len(elo)):
                            print("Seu cartão Elo cadastrado na posição ", x + 1, " é o de número ", elo[x], "\n\n\n")
                    
                        funcoes.pausar()                   
                        funcoes.limpar()

                    elif (opcao_consulta == 4):

                        x = 0

                        for x in range (len(outros_numero)):
                            print("Seu cartão", (outros_nome[x]), "cadastrado na posição ", x + 1, " é o de número ", (outros_numero[x]), "\n\n\n")
                    
                        funcoes.pausar()                   
                        input("Pessione qualquer tecla")
                        funcoes.limpar()
                    else:
                            funcoes.meme()

                elif (opcao == 3):

                    funcoes.exclusao_cartao()
                    escolha = int(input("Qual a sua opção?\n\n"))
                    
                    if (escolha == 1):

                        funcoes.exclusao_cartao2()

                        tipo_exclusao = int(input("Informe o número "))
                        
                        if (tipo_exclusao == 1):

                            numero_excluir = int(input("Informe o número do cartão visa a ser excluido. \n\n"))

                            if (numero_excluir in visa):

                                posicao = visa.index(numero_excluir)

                                print("Tem certeza que deseja excluir o cartão Visa número ", numero_excluir, " o cartão está cadastrado na posição: ", posicao)
                                confirmacao = input("Digite Sim ou Não ")
                                    
                                if(confirmacao.upper() == "SIM"):
                                    visa.remove(numero_excluir)
                                    print("Cartão excluido com sucesso ")
                                    input("")
                                
                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")
                                    input("")
                                
                                else:
                                    print("Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                    input("")

                        elif(tipo_exclusao == 2):

                            posicao = int(input("Qual a posição do cartão Visa? \n"))

                            posicao = posicao - 1
                            
                            print("Tem certeza que deseja excluir o cartão Visa número ", visa[posicao], " o cartão está cadastrado na posição: ", posicao)

                            confirmacao = input("Digite Sim ou Não ")
                                    
                            if(confirmacao.upper() == "SIM"):
                                visa.pop(posicao)
                                print("Cartão excluido com sucesso ")
                                input("")
                            
                            elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                print("Cartão não excluido ")
                                input("")
                            
                            else:
                                print("Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                input("")
                        else:
                            funcoes.meme()
                                
                    elif (escolha == 2):

                        funcoes.exclusao_cartao2()

                        tipo_exclusao = int(input("Informe o número"))
                        
                        if (tipo_exclusao == 1):

                            numero_excluir = int(input("Informe o número do cartão Mastercard a ser excluido. \n\n"))

                            if (numero_excluir in master):

                                posicao = master.index(numero_excluir)

                                print("Tem certeza que deseja excluir o cartão Master número ", numero_excluir, " o cartão está cadastrado na posição: ", posicao)
                                confirmacao = input("Digite Sim ou Não ")
                                    
                                if(confirmacao.upper() == "SIM"):
                                    master.remove(numero_excluir)
                                    print("Cartão excluido com sucesso ")
                                
                                elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                    print("Cartão não excluido ")
                                
                                else:
                                    print("Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                        
                        elif(tipo_exclusao == 2):

                            posicao = int(input("Qual a posição do cartão Master? \n"))

                            posicao = posicao - 1
                            
                            print("Tem certeza que deseja excluir o cartão Visa número ", master[posicao], " o cartão está cadastrado na posição: ", posicao)

                            confirmacao = input("Digite Sim ou Não ")
                                    
                            if(confirmacao.upper() == "SIM"):
                                master.pop(posicao)
                                print("Cartão excluido com sucesso ")
                                input("")
                            
                            elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                print("Cartão não excluido ")
                                input("")
                            
                            else:
                                print("Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                                input("")
                        else:
                            funcoes.meme()

                    elif (escolha == 3):

                        numero_excluir = int(input("Informe o número do cartão Mastercard a ser excluido. \n\n"))

                        if (numero_excluir in elo):

                            posicao = elo.index(numero_excluir)

                            print("Tem certeza que deseja excluir o cartão Master número ", numero_excluir, " o cartão está cadastrado na posição: ", posicao)
                            confirmacao = input("Digite Sim ou Não ")
                                
                            if(confirmacao.upper() == "SIM"):
                                elo.remove(numero_excluir)
                                print("Cartão excluido com sucesso ")
                            
                            elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                print("Cartão não excluido ")
                            
                            else:
                                print("Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                    
                    elif (escolha == 4):

                        numero_excluir = int(input("Informe o número do cartão Mastercard a ser excluido. \n\n"))

                        if (numero_excluir in elo):

                            posicao = elo.index(numero_excluir)

                            print("Tem certeza que deseja excluir o cartão Master número ", numero_excluir, " o cartão está cadastrado na posição: ", posicao)
                            confirmacao = input("Digite Sim ou Não ")
                                
                            if(confirmacao.upper() == "SIM"):
                                elo.remove(numero_excluir)
                                print("Cartão excluido com sucesso ")
                            
                            elif(confirmacao.upper() == "NÃO" or confirmacao.upper() == "NAO"):
                                print("Cartão não excluido ")
                            
                            else:
                                print("Comando invalido, é necessário escrever a palavra SIM ou NÃO, pode ser maiúsculo ou não")
                    
                            
            
                else:

                    funcoes.limpar()
                    print("Opção inexistente\n\n\n")
            
            except:
                funcoes.opcao_invalida()

        elif(opcao == 9):
            funcoes.limpar()
            print("Até a proxima\n\n\n")
            funcoes.sair()
            funcoes.aguardar()
            funcoes.limpar()
            break

        else:
            funcoes.meme()
            
    except:
        funcoes.meme()
