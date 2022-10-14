# https://github.com/Victor-Full/Avalia-oAV1-Aplica-oConsolePythonRAD?classId=27bd03ab-65b6-4263-90af-50d093a0956a&assignmentId=13d15b99-4d64-423e-8899-741ed1d1f38b&submissionId=4de0ff1b-13b8-04b0-d57c-ec0200b1f7bf
# Cadastro de Clientes
from Funcoes import *

op = ''

while op != '20':
    dataPullAll()
    print('/// MENU DE CADASTRAMENTO')
    print('1 - Cadastrar novo cliente')
    print('2 - Consultar cliente existente')
    print('3 - Atualizar cadastro de cliente')
    print('4 - Excluir cadastro de cliente')
    print('\n/// MENU DE LOCAÇÃO')
    print('5 - Alugar veículos')
    print('6 - Devolução de veículos')
    print('7 - Consultar veículos disponíveis')
    print('8 - Consultar registro de empréstimos efetuados')
    print('9 - Menu de veículos')
    print('\n0 - Sair\n\n')
    op = input("// Digite uma opção do menu acima: ")

    if op == '1':
        menuOp1()
    elif op == '2':
        menuOp2()
    elif op == '3':
        menuOp3()
    elif op == '4':
        menuOp4()
    elif op == '5':
        menuOp5()
    elif op == '6':
        menuOp6()
    elif op == '7':
        menuOp7()
    elif op == '8':
        menuOp8()
    elif op == '9':
        op = ""
        print("/// MENU DE VEÍCULOS")
        print("1 - Cadastrar veículos")
        print("2 - Editar veículos")
        print("3 - Excluir veículos")
        print("0 - Voltar")
        menuOp9()
    elif op == '0':
        break
    else:
        print("OPÇÃO INVÁLIDA!")
    cont = input("Aperte Enter para continuar")
    print("\n" * 30)
