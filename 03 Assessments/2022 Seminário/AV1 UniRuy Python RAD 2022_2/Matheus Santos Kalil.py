# https://github.com/Khalil808/Aplic.Financeira/blob/main/Projeto%20Aplica%C3%A7%C3%A3o%20Financeira.py
# Capitalização
import os
from time import sleep
import json


while (True):
    menu = ('============= Olá pobre, bem vindo ao perfil do agiota Kalil =============\n \n|Aqui você pode calcular de forma simples e prática suas dividas comigo sem me enrolar =D|\n \n-> Capitalização\n-> Descapitalização')
    print(menu)

    coud = int(input(
        '\nCaso a sua aplicação seja uma capitalização digite "1" e se for uma descapitalizaçao digite "2" '))

    # capitalização
    if (coud == 1):
        while (True):
            pv = float(input('informe o capital inicial aplicado: R$'))
            i = float(input('informe a taxa de juros da aplicação: '))
            t = float(input('informe o tempo que essa divida será quitada: '))

            print('-------------------------------------------------')
            print('Capital inicial: ', pv)
            print('taxa: ', i)
            print('tempo de divida: ', t)
            confime = str(input('Voce confirma os dados a cima ? S/N: '))
            if confime == 's':

                valorf = pv*((1+(i/100))**t)

                print('O valor necessário para pagar daqui a {} meses com {}% de taxa de juros será {:.2f}R$'.format(
                    t, i, valorf))

                ''' import sleep  para demorar um tempo antes de apagar a msg, eo os.system para configurar o clear da msg anterior '''
                sleep(10)
                os.system('clear') or None
                break
            if confime == 'n':
                os.system('clear') or None

    # descapitalização
    elif (coud == 2):
        fv = float(input('informe o valor futuro da aplicação: R$'))
        i = float(input('informe a taxa de juros da aplicação: '))
        t = float(input('informe o tempo em que essa divida será quitada: '))
        print('-------------------------------------------------')
        print('Valor futuro da aplicao: ', fv)
        print('taxa: ', i)
        print('tempo de divida: ', t)
        confime = str(input('Voce confirma os dados a cima ? S/N: '))

        if confime == 's':

            valorp = fv/((1+(i/100))**t)

            print('O valor necessário para pagar daqui a {} meses sobre {}% de taxa de juros será {:.2f}R$ '.format(
                t, i, valorp))

            sleep(5)
            os.system('clear') or None
            break
        if confime == 'n':
            os.system('clear') or None

    else:

        print('o valor inserido não corresponde as nossas aplicações ')
        break
