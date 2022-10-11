
import os
import time
import colorama


def opcao(): #menu principal                                                                                                                                                                                                                                                                 
    print("Digite [1] para cadastrar novo cartão")
    print("Digite [2] para consultar cartão")
    print("Digite [3] para excluir cartão")
    print("Digite [4] para substituir cartão\n")
    print("Digite [9] para encerrar o programa\n\n")

def cadastro_cartao(): #Menu cadastro de cartões
    print("Digite [1] para cadastrar Visa")
    print("Digite [2] para cadastrar Mastercard")
    print("Digite [3] para cadastrar Elo")
    print("Digite [4] para cadastrar Outros")
    print("Digite [5] para retornar o menu anterior\n\n")

def exclusao_cartao(): #Menu principal da exclusão de cartão
    print("Digite [1] para excluir Visa")
    print("Digite [2] para excluir Mastercard")
    print("Digite [3] para excluir Elo")
    print("Digite [4] para excluir Outros")
    print("Digite [5] para retornar o menu anterior\n\n")

def exclusao_cartao2(): #Menu secundario da exclusão de cartão.
    print("Digite [1] para excluir pelo número do cartão")
    print("Digite [2] para excluir pela posição do cartão")
    print("Digite [3] para excluir todos os cartões")
    print("Digite [5] para retornar o menu anterior\n\n")


def substituir_cartao():
    print("Digite [1] para substituir Visa")
    print("Digite [2] para substituir Mastercard")
    print("Digite [3] para substituir Elo")
    print("Digite [4] para substituir Outros")
    print("Digite [5] para retornar o menu anterior\n\n")

def substituir_cartao2(): #Menu secundario da substituição de cartão.
    print("Digite [1] para excluir pelo número do cartão")
    print("Digite [2] para excluir pela posição do cartão")
    print("Digite [3] para excluir todos os cartões")
    print("Digite [5] para retornar o menu anterior\n\n")

def consulta_cartao():
    print("Digite [1] para consultar Visa")
    print("Digite [2] para consultar Mastercard")
    print("Digite [3] para consultar Elo")
    print("Digite [4] para consultar Outros")
    print("Digite [5] para consultar todos")
    print("Digite [6] para retornar o menu anterior\n\n")

def limpar():
     os.system('cls')

def pausar():
    os.system("pause")

def aguardar():
    time.sleep(1)
