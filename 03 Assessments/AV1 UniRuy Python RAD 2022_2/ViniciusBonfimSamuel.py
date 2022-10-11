# Controle patrimonio
# https://github.com/vinicius-bomfim0328/CrudPython/blob/main/CrudPython.py

nome = input("Digite seu nome: \n")
print("Bem vindo", nome, "ao aplicativo de controle ao seu patrimônio.")
opcoes = 0
while (opcoes < 5):
    print("O que você deseja realizar? ")
    print("1: Inserir ; 5: Sair ;")
    opcoes = int(input("Qual voce deseja acessar? "))
    if opcoes == 1:
        print("Insira abaixo os valores nas seguintes ordens: ")
        print("Qual mês deseja gerir seu patrimônio?")
        mes = input()
        print("Qual foi sua renda deste mês? ")
        renda = float(input())
        print("Quanto você gastou com lazer este mês?")
        lazer = float(input())
        print("Quanto você gastou com alimentação este mês?")
        alimentacao = float(input())
        print("Quanto você gastou com sua casa este mês (ex: aluguel, internet, luz e telefone)?")
        casa = float(input())
        print(
            "Quanto você gastou com saúde este mês (ex: dentista, médico, plano de saúde)?")
        saude = float(input())
        print("Quanto você gastou com transporte este mês (ex: combustível, metrô/ônibus)?")
        transporte = float(input())
        gasto = [mes, renda, lazer, alimentacao, casa, saude, transporte]
        print("Salvo com sucesso!")
        print("Selecione um dos itens abaixo:")
        print("2: Alterar ; 3: Consultar ; 4: excluir ; 5: Sair")
        opcoes = int(input("Qual voce deseja acessar?"))
        if opcoes == 2:
            escolha = 0
            while (opcoes < 9):
                print("Insira qual dado você deseja alterar")
                print(
                    "1: Mês ; 2: Renda ; 3: Lazer ; 4: Alimentação ; 5: Casa ; 6: Saúde ; 7: Transporte ; 8: Voltar ;")
                escolha = int(input("Qual voce deseja acessar?"))
                if escolha == 1:
                    gasto[0] = input("Qual mês deseja gerir seu patrimônio?")
                elif escolha == 2:
                    gasto[1] = float(input("Qual foi sua renda deste mês? "))
                elif escolha == 3:
                    gasto[2] = float(
                        input("Quanto você gastou com lazer este mês?"))
                elif escolha == 4:
                    gasto[3] = float(
                        input("Quanto você gastou com alimentação este mês?"))
                elif escolha == 5:
                    gasto[4] = float(input(
                        "Quanto você gastou com sua casa este mês (ex: aluguel, internet, luz e telefone)?"))
                elif escolha == 6:
                    gasto[5] = float(input(
                        "Quanto você gastou com saúde este mês (ex: dentista, médico, plano de saúde)?"))
                elif escolha == 7:
                    gasto[6] = float(input(
                        "Quanto você gastou com transporte este mês (ex: combustível, metrô/ônibus)?"))
                elif escolha == 8:
                    print("Selecione um dos itens abaixo:")
                    print("3: Consultar ; 4: Excluir ; 5: Sair ;")
                    opcoes = int(input("Qual você deseja acessar?"))
                    if opcoes == 3:
                        print("Mês: ", gasto[0])
                        print("Renda: ", gasto[1])
                        print("Lazer: ", gasto[2])
                        print("Alimentação: ", gasto[3])
                        print("Casa: ", gasto[4])
                        print("Saúde: ", gasto[5])
                        print("Transporte: ", gasto[6])
                        if gasto[1]-gasto[2]-gasto[3]-gasto[4]-gasto[5]-gasto[6] < 0:
                            print("Aff.. O saldo deste mês foi negativo, o valor foi de: ",
                                  gasto[1]-gasto[2]-gasto[3]-gasto[4]-gasto[5]-gasto[6])
                        else:
                            print("Que bom!!, o saldo deste mês foi positivo, o valor foi de: ",
                                  gasto[1]-gasto[2]-gasto[3]-gasto[4]-gasto[5]-gasto[6])
                    if opcoes == 4:
                        del gasto
                        print("Gasto deletado com sucesso")
                    if opcoes == 5:
                        exit
        if opcoes == 3:
            print("Mês: ", gasto[0])
            print("Renda: ", gasto[1])
            print("Lazer: ", gasto[2])
            print("Alimentação: ", gasto[3])
            print("Casa: ", gasto[4])
            print("Saúde: ", gasto[5])
            print("Transporte: ", gasto[6])
            if gasto[1]-gasto[2]-gasto[3]-gasto[4]-gasto[5]-gasto[6] < 0:
                print("Aff.. O saldo deste mês foi negativo, o valor foi de: ",
                      gasto[1]-gasto[2]-gasto[3]-gasto[4]-gasto[5]-gasto[6])
            else:
                print("Que bom!!, o saldo deste mês foi positivo, o valor foi de: ",
                      gasto[1]-gasto[2]-gasto[3]-gasto[4]-gasto[5]-gasto[6])
            print("Selecione um dos itens abaixo:")
            print("2: Alterar ; 3: Consultar ; 4: excluir ; 5: Sair")
            opcoes = int(input("Qual voce deseja acessar?"))
            if opcoes == 2:
                escolha = 0
                while (opcoes < 9):
                    print("Insira qual dado você deseja alterar")
                    print(
                        "1: Mês ; 2: Renda ; 3: Lazer ; 4: Alimentação ; 5: Casa ; 6: Saúde ; 7: Transporte ; 8: Voltar ;")
                    escolha = int(input("Qual voce deseja acessar?"))
                    if escolha == 1:
                        gasto[0] = input(
                            "Qual mês deseja gerir seu patrimônio?")
                    elif escolha == 2:
                        gasto[1] = float(
                            input("Qual foi sua renda deste mês? "))
                    elif escolha == 3:
                        gasto[2] = float(
                            input("Quanto você gastou com lazer este mês?"))
                    elif escolha == 4:
                        gasto[3] = float(
                            input("Quanto você gastou com alimentação este mês?"))
                    elif escolha == 5:
                        gasto[4] = float(input(
                            "Quanto você gastou com sua casa este mês (ex: aluguel, internet, luz e telefone)?"))
                    elif escolha == 6:
                        gasto[5] = float(input(
                            "Quanto você gastou com saúde este mês (ex: dentista, médico, plano de saúde)?"))
                    elif escolha == 7:
                        gasto[6] = float(input(
                            "Quanto você gastou com transporte este mês (ex: combustível, metro/ônibus)?"))
                    elif escolha == 8:
                        print("Selecione um dos itens abaixo:")
                        print("3: Consultar ; 4: Excluir ; 5: Sair ;")
                        opcoes = int(input("Qual voce deseja acessar?"))
                        if opcoes == 3:
                            print("Mês: ", gasto[0])
                            print("Renda: ", gasto[1])
                            print("Lazer: ", gasto[2])
                            print("Alimentação: ", gasto[3])
                            print("Casa: ", gasto[4])
                            print("Saúde: ", gasto[5])
                            print("Transporte: ", gasto[6])
                            if gasto[1]-gasto[2]-gasto[3]-gasto[4]-gasto[5]-gasto[6] < 0:
                                print("Aff.. O saldo deste mês foi negativo, o valor foi de: ",
                                      gasto[1]-gasto[2]-gasto[3]-gasto[4]-gasto[5]-gasto[6])
                            else:
                                print("Que bom!!, o saldo deste mês foi positivo, o valor foi de: ",
                                      gasto[1]-gasto[2]-gasto[3]-gasto[4]-gasto[5]-gasto[6])
                        if opcoes == 4:
                            del gasto
                            print("Gasto deletado com sucesso")
                            exit
                        if opcoes == 5:
                            exit
        if opcoes == 4:
            del gasto
            print("Gasto deletado com sucesso")

        if opcoes == 5:
            exit
