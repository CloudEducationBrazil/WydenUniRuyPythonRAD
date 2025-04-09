# https://github.com/yurinasc21/Agenda-python?classId=27bd03ab-65b6-4263-90af-50d093a0956a&assignmentId=13d15b99-4d64-423e-8899-741ed1d1f38b&submissionId=69b731c6-44eb-d747-a7ee-e5b147d38a81
# agenda
def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input(''' 
    ==========================================
    *********** SEJA BEM VINDO !! ************ 
             AGENDA DE COMPROMISSO
    MENU:
    [1] - CADASTRAR COMPROMISSO;
    [2] - LISTAR AGENDA;
    [3] - DELETAR COMPROMISSO;
    [4] - CONSULTAR COMPROMISSO;
    [5] - ATUALIZAR COMPROMISSO;
    [6] - SAIR.
    ============================================
    ESCOLHA UMA OPÇÃO ACIMA:
    ''')
        if opcao == "1":
            cadastrarcompromisso()
        elif opcao == "2":
            listarcompromisso()
        elif opcao == "3":
            deletarcompromisso()
        elif opcao == "4":
            consultarCompromisso()
        elif opcao == "5":
            atualizarCompromisso()
        else:
            sair()
        voltarMenuPrincipal = input(
            "Deseja voltar ao menu principal ? (digite 's' para sim ou 'n' para não)"'\n').lower()


# INCLUIR
def cadastrarcompromisso():
    codCompromisso = input("Digite o código do compromisso: ")
    data = input("Digite a data do compromisso (xx/xx/xxxx) : ")
    hora = input("Digite o horário (xx:xx) : ")
    titulo = input("Digite o título do compromisso: ")
    local = input("Digite o local do compromisso: ")
    descricao = input("Digite a descrição do compromisso: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{[codCompromisso]};{[data]};{[hora]};{[titulo]};{[local]};{[descricao]} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Compromisso gravado com sucesso !!!!!!')
    except:
        print("ERRO na gravação do compromisso")


# LER
def listarcompromisso():
    agenda = open("agenda.txt", "r")
    for compromisso in agenda:
        print(compromisso)
    agenda.close()


def consultarCompromisso():
    data = input(
        f'Digite a data do compromisso a ser consultada (xx/xx/xxxx): ')
    agenda = open("agenda.txt", "r")
    for compromisso in agenda:
        if data in compromisso.split(";")[1]:
            print(compromisso)
    agenda.close()


# DELETAR
def deletarcompromisso():
    tituloDeletado = input("Digite um titulo para ser deletado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if tituloDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'compromisso deletado com sucesso')
    listarcompromisso()


# ATUALIZAR
def atualizarCompromisso():
    tituloUpdate = input("Digite o titulo cadastrado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if tituloUpdate not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    codCompromisso = input("Digite o código do compromisso atualizado: ")
    data = input("Digite a data do compromisso atualizada (xx/xx/xxxx): ")
    hora = input("Digite o horário do compromisso atualizado (xx:xx): ")
    titulo = input("Digite o título do contato atualizado: ")
    local = input("Digite o local do contato atualizado: ")
    descricao = input("Digite o descrição do contato atualizado: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{[codCompromisso]};{[data]};{[hora]};{[titulo]};{[local]};{[descricao]} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Compromisso Atualizado com sucesso !!!!')
    except:
        print("ERRO na gravação do compromisso")


# SAIR DO PROGRAMA
def sair():
    print(f'Obrigado por utilizar a agenda de compromisso... Até logo !!!')
    exit()


def main():

    menu()


main()
