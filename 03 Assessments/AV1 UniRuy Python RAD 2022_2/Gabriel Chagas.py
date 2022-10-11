# https://github.com/chagas-rgb/sistema-de-emprestimo/blob/main/prova%20python.py?classId=27bd03ab-65b6-4263-90af-50d093a0956a&assignmentId=13d15b99-4d64-423e-8899-741ed1d1f38b&submissionId=f9c75c68-b501-8270-dc5e-77803e7ea2b9
# SISTEMA de emprestimo
import os


def sub_usuários(usuários):
    opção = 0
    while opção != "6":
        print("\n---------------------------\n"
              "    Submenu de Usuários:\n"
              "---------------------------\n"
              "1. Listar todos\n"
              "2. Listar elemento \n"
              "3. Incluir\n"
              "4. Alterar\n"
              "5. Excluir\n"
              "6. Voltar\n")
        opção = input("Digite a opção desejada: ")
        while opção not in "123456":
            opção = input("Opção inválida! Digite a opção desejada de 1 à 6: ")

        if opção == "1":
            contagem = 1
            for pessoa in usuários.keys():
                print(f"\n  -- Usuário {contagem} --\n")
                print(f"CPF: {pessoa}\n"
                      f"Nome: {usuários[pessoa][0]}\n"
                      f"Rua: {usuários[pessoa][1]}\n"
                      f"Número: {usuários[pessoa][2]}\n"
                      f"CEP: {usuários[pessoa][3]}")
                print("E-mail(s):")
                for endereço in usuários[pessoa][4]:
                    print(f"\t{endereço}")
                print("Telefone(s):")
                for telefone in usuários[pessoa][5]:
                    print(f"\t{telefone}")
                print(f"Data de nascimento: {usuários[pessoa][6]}\n"
                      f"Profissão: {usuários[pessoa][7]}")
                contagem += 1
            if len(usuários) == 0:
                print("Não existem usuários cadastrados")

        if opção == "2":
            pessoa = input("\nDigite o CPF: ").strip()
            if pessoa not in usuários.keys():
                print("CPF não cadastrado.")
            else:
                print(f"\nNome: {usuários[pessoa][0]}")
                print(f"Rua: {usuários[pessoa][1]}")
                print(f"Número: {usuários[pessoa][2]}")
                print(f"CEP: {usuários[pessoa][3]}")
                print("E-mail(s): ")
                for end in usuários[pessoa][4]:
                    print(f"\t{end}")
                print("Telefone(s):")
                for num in usuários[pessoa][5]:
                    print(f"\t{num}")
                print(f"Data de nascimento: {usuários[pessoa][6]}")
                print(f"Profissão: {usuários[pessoa][7]}")

        if opção == "3":
            num_cpf = input("CPF (somente números): ").strip()
            while len(num_cpf) != 11 or num_cpf.isdigit() == False:
                num_cpf = input(
                    "CPF inválido. Digite o CPF (somente números): ").strip()
            if num_cpf in usuários.keys():
                print("CPF já cadastrado.")
            else:
                usuários[num_cpf] = []
                usuários[num_cpf].append(input("Nome: "))
                usuários[num_cpf].append(input("Rua: "))
                usuários[num_cpf].append(input("Número: "))
                num_cep = input("CEP (somente números): ").strip()
                while len(num_cep) != 8 or num_cep.isdigit() == False:
                    num_cep = input(
                        "CEP inválido. Digite o CEP (somente números): ").strip()
                usuários[num_cpf].append(num_cep)
                lista_emails = []
                resp = "S"
                while resp in "S":
                    end_email = input("E-Mail: ")
                    if end_email in lista_emails:
                        print("E-Mail já cadastrado")
                    else:
                        lista_emails.append(end_email)
                    resp = input(
                        "Cadastrar outro e-mail? [S/N] ").strip().upper()
                usuários[num_cpf].append(lista_emails)
                lista_telefones = []
                resp = "S"
                while resp in "S":
                    num_telefone = input("Telefone: ")
                    if num_telefone in lista_telefones:
                        print("Telefone já cadastrado.")
                    else:
                        lista_telefones.append(num_telefone)
                    resp = input(
                        "Cadastrar outro telefone? [S/N] ").strip().upper()
                usuários[num_cpf].append(lista_telefones)
                usuários[num_cpf].append(input("Data de nascimento: "))
                usuários[num_cpf].append(input("Profissão: "))
                if os.path.exists('usuario.keys.txt'):
                    with open('usuario.keys.txt', 'r+') as arquivo:
                        # HELENO
                        for pessoas in usuários.keys():
                            arquivo.write(str(pessoas))

        if opção == "4":
            pessoa = input("Digite o CPF: ").strip()
            if pessoa not in usuários.keys():
                print("CPF não cadastrado.")
            else:
                print(f"\nUsuário: {usuários[pessoa][0]}\n"
                      "-- Digite apenas os dados que serão alterados: ")
                nome = input("Nome: ").strip()
                if len(nome) > 0:
                    usuários[pessoa][0] = nome
                rua = input("Rua: ").strip()
                if len(rua) > 0:
                    usuários[pessoa][1] = rua
                número = input("Número: ").strip()
                if len(número) > 0:
                    usuários[pessoa][2] = número
                CEP = input("CEP: ")
                if len(CEP) > 0:
                    while len(CEP) != 8 or CEP.isdigit() == False:
                        CEP = input(
                            "CEP inválido. Digite o CEP (somente números): ").strip()
                    usuários[pessoa][3] = CEP
                email = input("E-mail: ").strip()
                if email not in usuários[pessoa][4]:
                    if len(email) != 0:
                        usuários[pessoa][4].append(email)
                else:
                    print("E-mail já cadastrado.")
                telefone = input("Telefone: ")
                if telefone not in usuários[pessoa][5]:
                    if len(telefone) != 0:
                        usuários[pessoa][5].append(telefone)
                else:
                    print("Telefone já cadastrado.")
                data_nascimento = input("Data de nascimento: ")
                if len(data_nascimento) > 0:
                    usuários[pessoa][6] = data_nascimento
                profissão = input("Profissão: ")
                if len(profissão) > 0:
                    usuários[pessoa][7] = profissão
                print("Dados alterados com sucesso!")

        if opção == "5":
            pessoa = input("Digite o CPF: ").strip()
            if pessoa not in usuários:
                print("CPF não cadastrado.")

            else:
                print(f"\nExcluir usuário: {usuários[pessoa][0]}")
                resposta = input("Confirmar? [S/N]: ").upper().strip()
                while resposta not in "SN":
                    resposta = input(
                        "Resposta inválida. Responda S ou N: ").upper().strip()
                if resposta == "S":
                    print(
                        f"Usuário --{usuários[pessoa][0]}-- excluído com sucesso.")
                    del usuários[pessoa]


def sub_livros(livros):
    opção = 0
    while opção != "6":
        print("\n---------------------------\n"
              "     Submenu de Livros:\n"
              "---------------------------\n"
              "1. Listar todos\n"
              "2. Listar elemento \n"
              "3. Incluir\n"
              "4. Alterar\n"
              "5. Excluir\n"
              "6. Voltar\n")
        opção = input("Digite a opção desejada: ")
        while opção not in "123456":
            opção = input("Opção inválida! Digite a opção desejada de 1 à 6: ")

        if opção == "1":
            contagem = 1
            for livro in livros:
                print(f"\n  -- Livro {contagem} --\n"
                      f"ISBN: {livro}\n"
                      f"Título: {livros[livro][0]}\n"
                      f"Gênero: {livros[livro][1]}\n"
                      "Autor(es):")
                for autor in livros[livro][2]:
                    print(f"\t{autor}")
                print(f"Número de páginas: {livros[livro][3]}")
                contagem += 1
            if len(livros) == 0:
                print("Não existem livros cadastrados.")

        if opção == "2":
            isbn = input("\nDigite o ISBN do livro que deseja listar: ")
            if isbn not in livros.keys():
                print("ISBN não cadastrado.")
            else:
                print(f"Título: {livros[isbn][0]}")
                print(f"Gênero: {livros[isbn][1]}")
                print(f"Autores: ")
                for autor in livros[isbn][2]:
                    print(f"\t{autor}")
                print(f"Número de páginas: {livros[isbn][3]}")

        if opção == "3":
            isbn = input("\nISBN do livro a ser cadastrado: ").strip()
            while len(isbn) != 13 or isbn.isdigit() == False:
                isbn = input(
                    "ISBN inválido. Digite o ISBN do Livro (somente números): ").strip()
            if isbn in livros.keys():
                print('ISBN já cadastrado')
            else:
                livros[isbn] = []
                livros[isbn].append(str(input("Insira o Título do livro: ")))

                list_autores = []
                escolha = "S"
                while escolha in "S":
                    autores = input("Insira o Autor do livro: ")
                    list_autores.append(autores)
                    escolha = input(
                        "Este livro possui mais de um autor? [S/N] ").strip().upper()
                livros[isbn].append(list_autores)

                print("\nLivro Adicionado com Sucesso!")

        if opção == "4":
            isbn = input("Digite o ISBN do livro: ").strip()
            if isbn not in livros.keys():
                print("ISBN não cadastrado.")
            else:
                titulo = input("Título do livro: ").strip()
                if len(titulo) > 0:
                    livros[isbn][0] = titulo
                genero = input("Gênero do livro: ").strip()
                if len(genero) > 0:
                    livros[isbn][1] = genero
                autores = input("Autor(es) do livro: ")
                if autores not in livros[isbn][2]:
                    livros[isbn][2].append(autores)
                else:
                    print("Este autor já está registrado: ")
                num_pag = input("Número de páginas do livro: ")
                if len(num_pag) > 0:
                    livros[isbn][3] = num_pag
                print("\n Dados alterados com sucesso!")

        if opção == "5":
            isbn = input(
                "Digite o ISBN do livro que deseja deletar da lista: ")
            if isbn not in livros:
                print("ISBN não cadastrado.")
            else:
                print(f"\nExcluir livro: {livros[isbn][0]}")
                resposta = input("Confirmar? [S/N]: ").upper().strip()
                while resposta not in "SN":
                    resposta = input(
                        "Resposta inválida. Responda S ou N: ").upper().strip()
                if resposta == "S":
                    print(f"Livro --{livros[isbn][0]}-- excluído com sucesso.")
                    del livros[isbn]


def sub_empréstimos(usuários, livros):
    print("\n---------------------------\n"
          "  Submenu de Empréstimos:\n"
          "---------------------------\n"
          "1. Listar todos\n"
          "2. Listar elemento \n"
          "3. Incluir\n"
          "4. Alterar\n"
          "5. Excluir\n"
          "6. Voltar\n")
    opção = input("Digite a opção desejada: ")
    while opção not in "123456":
        opção = input("Opção inválida! Digite a opção desejada de 1 à 6: ")

    if opção == "1":
        contagem = 1
        for empréstimo in empréstimos:
            print(f"\n  -- Empréstimo {contagem} --\n")
            print("CPF: ", empréstimo[0])
            print(f"ISBN: {empréstimo[1]}\n"
                  f"Data de Retirada: {empréstimo[2]}\n"
                  f"Data de Devolução: {empréstimos[empréstimo][0]}\n"
                  f"Valor Diário da Multa por atraso: R${empréstimos[empréstimo][1]:.2f}")
            contagem += 1
        if len(empréstimos) == 0:
            print("Não existem empréstimos cadastrados.")

    if opção == "2":
        list_emprest = ()
        cpf_emprest = input(
            "Digite o CPF da pessoa que realizou o Empréstimo: ")
        isbn_list = input("Digite o ISBN do livro que foi emprestado: ")
        ret_list = input(
            "Digite a data de retirada do empréstimo(xx/xx/xxxx): ")
        list_emprest = (cpf_emprest, isbn_list, ret_list)
        if list_emprest in empréstimos:
            print("\nAqui estão as informações que você solicitou:\n")
            print("CPF:", list_emprest[0])
            print(f"ISBN: {list_emprest[1]}\n"
                  f"Data de Retirada: {list_emprest[2]}\n"
                  f"Data de Devolução: {empréstimos[list_emprest][0]}\n"
                  f"Valor Diário da Multa por atraso: {empréstimos[list_emprest][1]}")
        else:
            print("Este Empréstimo não está nos registros de empréstimos.")

    if opção == "3":
        empréstimo = ()
        cpf = input("Digite o CPF (somente números): ")
        while len(cpf) < 11 or cpf.isdigit() == False or cpf not in usuários.keys():
            if len(cpf) < 12 or cpf.isdigit() == False:
                cpf = input("CPF inválido. Digite o CPF (somente números): ")
            elif cpf not in usuários.keys():
                cpf = ("CPF não cadastrado. Digite o CPF (somente números): ")
        print(f"Usuário: -- {usuários[cpf][0]} --")
        isbn = input("Digite o ISBN do livro: ")
        while len(isbn) != 13 or isbn.isdigit() == False or isbn not in livros.keys():
            if len(isbn) == 13 or isbn.isdigit() == False:
                isbn = input("ISBN inválido. Digite o ISBN: ")
            elif isbn not in livros.keys():
                isbn = input("ISBN não cadastrado. Digite o ISBN: ")
        print(f"Livro: -- {livros[isbn][0]} --")
        data_retirada = input("Data de retirada[xx/xx/xxxx]: ")
        empréstimo = (cpf, isbn, data_retirada)
        # print(empréstimo)
        empréstimos[empréstimo] = []
        empréstimos[empréstimo].append(
            input("Data de devolução[xx/xx/xxxx]: "))
        empréstimos[empréstimo].append(
            float(input("Valor diário da Multa por Atraso: R$")))
        print(empréstimos)

    if opção == "4":
        alter_emprest = ()
        cpf_alter = input("Digite o CPF da pessoa que realizou o Empréstimo: ")
        isbn_alter = input("Digite o ISBN do livro referente ao empréstimo: ")
        data_alter = input(
            "Digite a Data em que o livro foi retirado(xx/xx/xxxx): ")
        alter_emprest = (cpf_alter, isbn_alter, data_alter)
        if alter_emprest in empréstimos:
            data_dev = input(
                "Digite a nova data de devolução se deseja alterá-la: ")
            if len(data_dev) > 0:
                empréstimos[alter_emprest][0] = data_dev
            valor_mul = input(
                "Digite o novo valor da multa de atraso caso deseja alterá-la: R$")
            if len(valor_mul) > 0:
                empréstimos[alter_emprest][1] = float(valor_mul)
        else:
            print("Empréstimo não cadastrado")

    if opção == "5":
        emprest_del = ()
        cpf_del = input(
            "Digite o CPF da pessoa que realizou empréstimo que deseja deletar da lista: ")
        isbn_del = input(
            "Digite o ISBN do livro referente à esse empréstimo: ")
        data_del = input(
            "Digite a data de retirada referente à esse empréstimo: ")
        emprest_del = (cpf_del, isbn_del, data_del)
        if emprest_del not in empréstimos:
            print("Empréstimo não cadastrado.")
        elif emprest_del in empréstimos:
            print(f"\nExcluir Empréstimo: {empréstimos[emprest_del]}")
            resposta = input("Confirmar? [S/N]: ").upper().strip()
            while resposta not in "SN":
                resposta = input(
                    "Resposta inválida. Responda S ou N: ").upper().strip()
            if resposta == "S":
                print("Empréstimo excluído com sucesso.")
                del empréstimos[emprest_del]


def usuários_idade(usuários, idade):
    from datetime import datetime
    quantidade = 0
    for pessoa in usuários.keys():
        idade_usuário = datetime.now().year - int(usuários[pessoa][6][-4:])
        if idade_usuário > idade:
            print(f"\nNome: {usuários[pessoa][0]}\n"
                  f"Rua: {usuários[pessoa][1]}\n"
                  f"Número: {usuários[pessoa][2]}\n"
                  f"CEP: {usuários[pessoa][3]}\n"
                  "E-mail(s):")
            for end in usuários[pessoa][4]:
                print(f"\t{end}")
            print("Telefone(s): ")
            for tel in usuários[pessoa][5]:
                print(f"\t{tel}")
            print(f"Data de nascimento: {usuários[pessoa][6]}\n"
                  f"Profissão: {usuários[pessoa][7]}")
            quantidade += 1
    print(
        f"\nQuantidade de usuários com idade maior que {idade} anos: {quantidade}.")
    if quantidade == 0:
        print(f"Não existem usuários cadastrados com mais de {idade} anos.")


def dados_empréstimos(usuários, livros, empréstimos, data_inicial, data_final):
    from datetime import datetime
    data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y').date()
    data_final = datetime.strptime(data_final, '%d/%m/%Y').date()
    for empréstimo in empréstimos.keys():
        data = datetime.strptime(empréstimo[2], '%d/%m/%Y').date()
        if data > data_inicial and data <= data_final:
            cpf = empréstimo[0]
            print(f"\nCPF: {cpf}")
            for info in usuários.keys():
                if info == cpf:
                    print(f"Nome: {usuários[info][0]}")
            isbn = empréstimo[1]
            print(f"ISBN: {isbn}")
            for info in livros.keys():
                if info == isbn:
                    print(f"Título: {livros[info][0]}")
            data_retirada = empréstimo[2]
            print(f"Data de retirada: {data_retirada}")
            lista_empréstimo = (cpf, isbn, data_retirada)
            for empréstimo in empréstimos.keys():
                if lista_empréstimo == empréstimo:
                    print(
                        f"Data de devolução: {empréstimos[lista_empréstimo][0]}")
                    print(
                        f"Valor diário da multa por atraso: R${empréstimos[lista_empréstimo][1]:.2f}")


def sub_relatórios(usuários, livros, empréstimos):
    print("\n---------------------------\n"
          "   Submenu de Relatórios:\n"
          "---------------------------\n"
          "1. Listar os usuários com mais de X anos de idade\n"
          "2. Listar os livros que tenham mais do que X autores\n"
          "3. Listar dados de empréstimos\n"
          "4. Voltar\n")
    opção = input("Digite a opção desejada: ")
    while opção not in "1234":
        opção = input("Opção inválida! Digite a opção desejada de 1 à 4: ")

    if opção == "1":
        idade = int(input(
            "\nLista de todos os usuários com idade maior que (digite a idade desejada): "))
        usuários_idade(usuários, idade)

    if opção == "2":
        quantidade = int(input(
            "\nLista de todos os livros que possuem a quantidade de autores maior que (digite a quantidade desejada): "))
        autores_livro(livros, quantidade)

    if opção == "3":
        print("Digite as datas inicial e final para ver os empréstimos que devem ser devolvidos entre tais datas:")
        data_inicial = input("Data inicial [xx/xx/xxxx]: ")
        data_final = input("Data final [xx/xx/xxxx]: ")
        dados_empréstimos(usuários, livros, empréstimos,
                          data_inicial, data_final)


# programa principal
usuários = {

}
livros = {'1234567890567': ['Harry Potter', 'Ficção', ['J.K.Rolling'], '234'],
          '6754356789876': ['Jane Eyre', 'Romance', ['Charlotte Bronte', 'Emily Bronte'], '345']}
empréstimos = {

}
opção = 0
while opção != "5":
    print("\n---------------------------\n"
          "      Menu de opções:\n"
          "---------------------------\n"
          "1. Submenu de Usuários\n"
          "2. Submenu de Livros\n"
          "3. Submenu de Empréstimos\n"
          "4. Submenu de Relatórios\n"
          "5. Sair\n")
    opção = input("Digite a opção desejada: ")
    while opção not in "12345":
        opção = input("Opção inválida! Digite a opção desejada de 1 à 5: ")

    if opção == "1":
        sub_usuários(usuários)

    if opção == "2":
        sub_livros(livros)

    if opção == "3":
        sub_empréstimos(usuários, livros)

    if opção == "4":
        sub_relatórios(usuários, livros, empréstimos)

    if opção == "5":
        print("\n  ---  ENCERRANDO  ---")
