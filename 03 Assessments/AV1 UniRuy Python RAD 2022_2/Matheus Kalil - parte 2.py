#   Aplicação Financeira
#   Por: Matheus - 15/10/2020
# https://github.com/Khalil808/Aplica-o.Financeira.segunda-chance/blob/main/segundavers%C3%A3o.py
# pip install Rich
# python -m rich

from os import system
from time import sleep
#from rich import print
ppl  = []
calc = []
file = [ppl, calc]
USER_CHOOSE = ''


# COMMMAND TO CLEAN TERMINAL
def cls():
    system('cls')


# WELCOME FUNCTION
def welcome():
    cls()

    print("""
                       [green]-[ Olá, bem vindo ao [gold1][bold]AppFinanceiro[/bold][/gold1] ]-[/green]
        
    [green]Aqui voçê pode organizar pessoas que precisam quitar dividas com você
    Selecione uma das opções abaixo:[/green] 
    [blue][1][/blue] -> Inserir pessoas
    [blue][2][/blue] -> consultar pessoas
    [blue][3][/blue] -> Alterar pessoas 
    [blue][4][/blue] -> Excluir
    [blue][9][/blue] -> Sair   
    """)


# ADD PEOPLE ON DB
def add_peopple():
    cls()
    name = str(input('Insira um nome\n'))
    ppl.append(name)
    cls()
    db_message(f'\nO nome {name} foi registrado com sucesso!\n')
    print()
    input('Pressione ENTER para continuar...')

    realizar_opc()
    record_calculation()


# MAKE OPERATION    
def realizar_opc():
    cls()

    print('Agora selecione a opção referente a situação da divida do individuo')
    print()
    print('[1] -> Capitalização')
    print('[2] -> Descapitalização')
    print()

    USER_INPUT = int(input('Digite uma das opções: '))

    def capitalization():
        cls()

        print('Capitalization Calc')
        print()

        present_value   = float(input('informe o capital inicial aplicado: R$ '))
        tax             = float(input('informe a taxa de juros da aplicação: '))
        time            = float(input('informe o tempo que essa divida será quitada (em meses): '))

        print()            
        print(f'Capital inicial: {present_value}')
        print(f'taxa: {tax}')
        print(f'tempo de divida: {time}')
        print()

        confirm = str(input('Voce confirma os dados a cima ? (S/N): ')).lower()
        cls()

        if confirm.isalpha():
            if confirm == 's':
                future_value = present_value*((1+(tax/100))**time)                
                print()
                print(f'O valor necessário para pagar daqui a {time} meses com {tax}% de taxa de juros será R$ {future_value:.2f}')
                       
                calc.append(future_value) # NEW
                print(f'\nO valor da divida de {future_value:.2f}R$ foi registrado com sucesso!\n')
                print()
                input('Pressione ENTER para continuar...')
                
            elif confirm == 'n':
                print('Altere os valores colocados anteriormente')
                input('Pressione ENTER para continuar...')
                capitalization()
                
            else:
                print("Por favor selecione uma opção valida")
                sleep(3)
                capitalization()            

        else: 
            print("Por favor selecione uma opção valida")
            sleep(4)
            capitalization()

    def despitalization():
        cls()
        print('Descapitalization Calc')
        print()

        future_value    = float(input('Informe o valor futuro da aplicação: R$'))
        tax             = float(input('Informe a taxa de juros da aplicação: '))
        time            = float(input('Informe o tempo em que essa divida será quitada (em meses): '))

        print()
        print(f'Valor futuro da aplicação: {future_value}')
        print(f'Taxa: {tax}')
        print(f'Tempo de divida: {time} ')
        print()

        confirm = str(input('Voce confirma os dados a cima ? (S/N): ')).lower()
        cls()
        if confirm.isalpha():
            if confirm == 's':
                present_value = future_value/((1+(tax/100))**time)
                print()
                print(f'O valor necessário para pagar daqui a {time} meses com {tax}% de taxa de juros será R$ {future_value:.2f}')
                
                calc.append(present_value) # NEW
                print(f'\nO valor da divida de {present_value:.2f}R$ foi registrado com sucesso!')
                print()
                print()
                input('Pressione ENTER para continuar...')
                

            elif confirm == 'n':
                sleep(3)
                despitalization()
                
        else: 
            print("Por favor selecione uma opção valida")
            sleep(4)
            despitalization()

    match USER_INPUT:
        case 1: 
            capitalization() # Capitalizacao

        case 2: 
            despitalization() # Descapitalizacao

        case _:
            print('Por favor Selecione uma opção válida')
            realizar_opc()


   

#TXT.NUMBER(REAIS)  
def record_calculation():
    cls()
    with open('afe.txt', 'w') as stream:
        lines = (f'{file}')
        stream.writelines((lines))


# CONSULTY
def select_user():
    cls()
    db_message(file[0])
    consulty = input('\nQual o nome da pessoa que voçê deseja buscar?\n')
    if consulty in ppl:
        cls()
        print(f'Cliente: {file[0]} | Divida: {file[1]}')
        input('Pressione ENTER para continuar...')
    else:
        consulty2 = consulty
        if consulty2 in ppl:
            db_message('O nome já consta na lista')
            sleep(3)
        else:
            print('O nome não esta na lista. Gostaria de adicionar ?')
            print()
            print('1 -> Sim')
            print('2 -> Não')
            print()
            cond_consu = int(input('Selecione: '))
            if cond_consu == 1:
                ppl.append(consulty)
                print()
                db_message('Nome adicionado')
                print()
                sleep(3)
            elif cond_consu == 2:
                return
            else:
                add_peopple()

# DELETE USER
def delete():
    cls()
    print('Qual nome deseja deletar ?')
    print()
    print(ppl)
    print()
    delete_name = input('Digite o nome que deseja deletar: ')
    if delete_name in ppl:
        ppl.remove(delete_name)
        print()
        db_message('Nome deletado com sucesso')
        print()
        print(ppl)
        print()
        input('Pressione ENTER para continuar...')
    else:
        db_message('Nome não encontrado')
        print()
        input('Pressione ENTER para continuar...')
        delete()


# ALTERATION
def alter():
    cls()
    if ppl == []:
        db_message('Banco de dados vazio !')
        print(ppl, calc)
        input('Pressione ENTER para continuar...')
    else:
        print('Qual nome deseja alterar ? (x para sair)')
        print()
        print(ppl)
        print()
        alter_name = input('Digite o nome que deseja alterar: ')
        if alter_name == 'x':
            return
        if alter_name in ppl:
            print()
            print('Nome encontrado')
            print()
            print('Qual o novo nome ?')
            print()
            new_name = input('Digite o novo nome: ')
            print()
            db_message('Nome alterado com sucesso')
            if alter_name in ppl:
                ppl.remove(alter_name)
            print(new_name)
            ppl.append(new_name)
            print(ppl)
            print()
            input('Pressione ENTER para continuar...')
        else:
            print()
            db_message('Nome não encontrado')
            print()
            input('Pressione ENTER para continuar...')
            alter()


# QUIT OPERATION
def leave():
    cls()
    exit()

def db_message(warn):
    print(f'[red][DB][/red] {warn}')

# EXECUTE
def run_process(choose):
    match choose:
        case 1:
            add_peopple()
        case 2:
            select_user()
        case 3:
            alter()
        case 4:
            delete()
        case 9:
            leave()
        case _: # default output
            print('Selecione uma opção valida')


# REQUEST USER INPUT
def request_choose():
    USER_CHOOSE = (int(input('selecione a opção desejada: ')))

    if USER_CHOOSE == '':
        print('Por favor escolhe uma das opcoes acima !')
    
    run_process(USER_CHOOSE)


# RUN THE PROGRAM
while True:
    welcome()
    request_choose()