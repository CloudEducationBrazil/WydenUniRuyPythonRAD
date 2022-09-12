import time
import os

print("Bem vindo ao sistema de cadastro de alunos!")

map_alunos = {}
opcao = 0

while opcao != 5:
    os.system("cls")
    print('''    [1] Create
    [2] Read
    [3] Update
    [4] Delete
    [5] Save & Exit''')
    opcao = int(input("insira o número da opção para executa-la: "))

    # [1] Create: inserts an element into the list.
    if opcao == 1:
        matricula = str(
            input("Insira a matrícula do aluno que deseja cadastrar: "))

        if matricula in map_alunos:
            print("Matrícula já existente.")
            continue

        nome = str(input("Insira o nome do aluno que deseja cadastrar: "))

        map_alunos[matricula] = nome
        # map_alunos.keys()
        # map_alunos.values()
        # map_alunos.get(key)
    # [2] Read: Shows the list.
    elif opcao == 2:
        print("Listando os alunos")
        print(map_alunos)
        # for mat in map_alunos.keys():
        # print("Nome:", map_alunos[nome], "/",
        #      "Matrícula:", map_alunos[matricula])
        time.sleep(2)
        print("fim")

    # [3] Update: changes a list element.
    elif opcao == 3:
        escolha = 0

        while escolha != 3:
            print('''            [1] Nome
            [2] Matrícula
            [3] Voltar ao menu principal''')
            escolha = int(
                input("Insira o número da opção que deseja alterar no cadastro: "))

            if escolha == 1:
                nome = str(input(
                    "Insira o nome do aluno a ser alterado no cadastro: "))
                bAlterar = False
                for nome_cad in map_alunos.values():
                    if nome in nome_cad:
                        # print("O nome inserido Não existe no cadastro.")
                        bAlterar = True
                        mat = map_alunos.keys(nome)
                        print('aqui ', mat)

                        break
                        # continue
                if bAlterar:
                    nome_new = str(
                        input("Insira o novo nome a ser inserido no cadastro: "))
                    # map_alunos[matricula] = {
                    #    'nome': nome_new}
                    map_alunos[mat] = nome_new
                    print(map_alunos)
                    time.sleep(2)
                else:
                    print("O nome inserido Não existe no cadastro.")

            elif escolha == 2:
                matricula = str(
                    input("Insira a matrícula do aluno a ser alterada no cadastro: "))
                if matricula not in map_alunos:
                    print("A matrícula inserida não existe no cadastro.")
                    continue

                matricula_new = str(
                    input("Insira a nova matrícula a ser inserida no cadastro"))
                map_alunos[matricula] = {
                    'matricula': matricula_new}

            elif escolha == 3:
                print("Encerrando update e voltando ao menu principal...")

            else:
                print("Opção inválida. Tente novamente.")

    # [4] Delete: erases an element of the list.
    elif opcao == 4:
        matricula = str(input("Qual a matricula a ser apagada do cadastro? "))
        if matricula in map_alunos:
            del map_alunos[matricula]
            continue
        print("Matricula não existente.")

    # [5] Save & Exit: closes the program and saves the current list to a txt document.
    elif opcao == 5:
        stralunos = "REGISTROS:\n"
        for aluno in map_alunos.values():
            stralunos = stralunos + "Nome: " + \
                aluno['nome'] + " / " + "Matrícula: " + \
                aluno['matricula'] + "\n"
        arquivo = open("lista-alunos", "w")
        arquivo.write(stralunos)

        print("Salvando informações e encerrando o programa...")

    # Shows if an invalid option was typed.
    else:
        print("Opção inválida. Tente novamente.")
