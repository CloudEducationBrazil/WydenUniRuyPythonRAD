# https://github.com/JV1T0R/Python-projects/blob/master/CRUD(sem%20banco%20de%20dados%20-%20lista)?classId=27bd03ab-65b6-4263-90af-50d093a0956a&assignmentId=13d15b99-4d64-423e-8899-741ed1d1f38b&submissionId=363b6045-7e8f-965c-e325-10b566102bb4
# cadastro de alunos
print("Bem vindo ao sistema de cadastro de alunos!")

lista_alunos = []

opcao = 0

while opcao != 7:
    print('''    [1] Create
    [2] Read
    [3] Update
    [4] Delete
    [5] Save to txt
    [6] Import from txt
    [7] Exit''')
    opcao = int(input("insira o número da opção para executa-la: "))

    # [1] Create: inserts an element into the list.
    if opcao == 1:
        print("")

        matricula = input(
            "Qual a matrícula do aluno(a) a ser inserida no cadastro? ")

        for aluno in lista_alunos:
            if matricula in aluno:
                print("A matricula inserida já existe no cadastro.")
                break

        else:
            nome = input(
                "Qual o nome do aluno(a) a ser inserido no cadastro? ")
            curso = input(
                "Qual o curso do aluno(a) a ser inserido no cadastro? ")
            lista_alunos.append([nome, matricula, curso])

    # [2] Read: Shows a list item or the all the items in the list.
    elif opcao == 2:
        print("")

        escolha = 0

        while escolha != 3:
            print(
                "[1] cadastro do aluno(a) / [2] banco de cadastros / [3] Voltar ao menu principal")
            escolha = int(input("Qual informação deseja consultar? "))

            if escolha == 1:
                print("")

                matricula = input(
                    "Insira a matrícula do aluno(a) para acessar seu cadastro ")

                for aluno in lista_alunos:
                    if aluno[1] == matricula:
                        print(
                            f"Nome: {aluno[0]} / Matrícula: {aluno[1]} / Curso: {aluno[2]}")
                        break
                else:
                    print("A matrícula inserida não existe no cadastro.")

            elif escolha == 2:
                print("")

                print("CADASTROS:")
                for aluno in lista_alunos:
                    print(
                        f"Nome: {aluno[0]} / Matrícula: {aluno[1]} / Curso: {aluno[2]}")

            elif escolha == 3:
                print("")

            else:
                print("Opção inválida.")

    # [3] Update: changes an index of a list element.
    elif opcao == 3:
        print("")
        escolha = 0

        while escolha != 3:
            print("[1] Nome / [2] Curso / [3] Voltar ao menu principal")
            escolha = int(
                input("Qual informação deseja alterar no cadastro? "))

            if escolha == 1:
                print("")

                matricula = input(
                    "Qual a matricula do aluno(a) a ter o nome alterado no cadastro? ")

                for aluno in lista_alunos:
                    if aluno[1] == matricula:
                        nome_new = input(
                            "Qual o novo nome do aluno(a) a ser inserido no cadastro? ")
                        aluno[0] = nome_new
                        print("Cadastro alterado com sucesso!")
                        break

                else:
                    print("A matrícula inserida não existe no cadastro.")

            elif escolha == 2:
                print("")

                matricula = input(
                    "Qual a matricula do aluno(a) a ter o curso alterado no cadastro? ")

                for aluno in lista_alunos:
                    if aluno[1] == matricula:
                        curso_new = input(
                            "Qual o novo curso do aluno(a) a ser inserido no cadastro? ")
                        aluno[2] = curso_new
                        print("Cadastro alterado com sucesso!")
                        break

                else:
                    print("A matrícula inserida não existe no cadastro.")

            elif escolha == 3:
                print("")

            else:
                print("Opção inválida.")

    # [4] Delete: erases an element of the list.
    elif opcao == 4:
        print("")

        matricula = input(
            "Qual a matrícula do aluno(a) a ser removido do cadastro? ")

        for aluno in lista_alunos:
            if aluno[1] == matricula:
                lista_alunos.remove(aluno)
                print("Cadastro excluido com sucesso!")
                break

        else:
            print("A matrícula inserida não existe no cadastro.")

    # [5] Save: saves the current list to a txt document.
    elif opcao == 5:
        print("")

        str_aluno = ""

        for aluno in lista_alunos:
            str_aluno = ",".join(map(str, lista_alunos))

        with open("lista-alunos.txt", "w") as arquivo:
            arquivo.write(str_aluno)

        print("Salvando informações para o arquivo txt...")

    # [6] Import from txt:
    elif opcao == 6:
        print("")

        with open("lista-alunos.txt", "r") as arquivo:
            cadastros = arquivo.read()

        lista_alunos = eval(cadastros)

        print("Carregando informações...")

    # [7] Exit: finishes the program.
    elif opcao == 7:
        print("")

        print("Encerrando o programa...")

    # Shows if an invalid option was typed.
    else:
        print("Opção inválida. Tente novamente.")
