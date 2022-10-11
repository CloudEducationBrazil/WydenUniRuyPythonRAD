import time
import os
x = 0
soma = 0
rdeposito = 0
result = 0
rsaldo = 0
menuprincipal = 0
menuprincipall = 0
menucliente = 0
menunaocliente = 0
saque = 0
saldo = 0
# MENU
# aplicação bancária
# https://github.com/yMarques/Thiago_ProjetoWYDEN/blob/main/Projeto%20Aplica%C3%A7%C3%A3o%20bancaria?classId=27bd03ab-65b6-4263-90af-50d093a0956a&assignmentId=13d15b99-4d64-423e-8899-741ed1d1f38b&submissionId=ffd43aa0-298d-4919-edcb-ecbe9866ce97


while (menuprincipal != 4):
    # menuprincipall()
    os.system("cls")
    menuprincipal = int(input(
        "############## Bem vindo ao pyBanking ############## \n \nDigite a opcao desejada \n \n1 - Acessar minha conta \n2 - Finalizar aplicação \n \n"))
    os.system("cls")
    time.sleep(0.5)
    # MENU CLIENTE DEPOSITO
    if (menuprincipal == 1):
        log = open('log01.txt', 'w')
        log.write("log de dados do sistema\n")
        log.write("Seu saldo disponivel é R$ {}\n".format(rdeposito))
        log.write("Você realizou o saque no valor de R$ {} \n \n \nSeu saldo disponivel é R$ {}\n.".format(
            saque, rdeposito))
        log.write("Fim do log!\n")
        log.close()

        # Lendo o arquivo criado:
        log = open('log01.txt', 'r')
        for linha in log:
            linha = linha.rstrip()
            print(linha)
        log.close()
        os.system("cls")
        menucliente = int(input(
            "############## Bem vindo ao pyBanking ############## \n \nDigite a opcao desejada \n \n1 - Deposito \n2 - Saque \n3 - Saldo \n4 - Voltar ao menu principal \n \n"))
        if(menucliente == 1):
            if(saque == 0):
                os.system("cls")
                saldo = float(
                    input("Digite o valor que deseja depositar \n \n"))
                os.system("cls")
                soma = saldo+rdeposito
                rdeposito += saldo
                print('Seu saldo atual é de R${}'.format(rdeposito))
                time.sleep(3)
                menucliente == 0
                os.system("cls")

            elif(saque != 0):
                os.system("cls")
                saldo = float(
                    input("Digite o valor que deseja depositar \n \n"))
                os.system("cls")
                soma = saque-rdeposito
                rdeposito += saldo
                print('Seu saldo atual é de R${}'.format(rdeposito))
                time.sleep(3)
                menucliente == 0
                # MENU CLIENTE SAQUE
        elif(menucliente == 2):
            os.system("cls")
            saque = float(
                input("Digite o valor que deseja realizar o saque \n \n"))
            result = saque - rdeposito
            if(saque > rdeposito):
                os.system("cls")
                print(
                    'Falha na operação! \n Voce não possui saldo suficiente para esse saque, por favor digite um valor valido')
                time.sleep(3)
                os.system("cls")
                menucliente == 0
            else:
                sub = rdeposito - saque
                rdeposito -= saque
                os.system("cls")
                print('Realizado saque de R${}\n \nSeu saldo atual é de R${}'.format(
                    saque, rdeposito))
                time.sleep(3)
                os.system("cls")
                rdeposito == 0
                # MENU CLIENTE SALDO
        elif(menucliente == 3):
            if (saque == 0):
                os.system("cls")
                print('Seu saldo atual é de R${}'.format(saldo))
                time.sleep(3)
                menucliente == 0
                os.system("cls")
            elif(saque != 0):
                os.system("cls")
                print('Seu saldo atual é de R${}'.format(rdeposito))
                time.sleep(3)
                menucliente == 0
                # MENU CLIENTE VOLTAR AO MENU PRINCIPAL
        elif(menucliente == 4):
            os.system("cls")
            menucliente == 0

        elif(menucliente >= 5):
            os.system("cls")
            print('Por favor digite uma opção válidaa')
            time.sleep(3)
            os.system("cls")

    elif(menuprincipal == 2):
        print('A aplicação foi finalizada')
        break
    if menuprincipal >= 3:
        os.system("cls")
        print('Por favor digite uma opção válida')
        time.sleep(3)
        os.system("cls")
