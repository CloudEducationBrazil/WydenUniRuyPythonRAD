# https://github.com/KNSVita/Crud_Python/blob/main/CRUD.py
# https://github.com/KNSVita/CRUD_2_Listas
# Biblioteca de Jogos
lista = []

# MENU INICIO
while True:

    print("Bem Vindo a sua bliblioteca de jogos!!!\n")
    print("Abaixo estão listadas algumas funções. Comece adicionando alguns jogos a sua bliblioteca basta digitar 1\n")

    print("[1] Inserir game")
    print("[2] Consultar games")
    print("[3] Alterar game")
    print("[4] Excluir game")
    print("[5] Salvar bliblioteca")
    print("[6] Importar bliblioteca (Só utilize essa opção se já tiver salvo sua bliblioteca.)")
    print("[7] Sair\n")

    resposta = int(input("Digite a opção desejada : "))
# MENU FIM

# INSERT
    if resposta == 1:
        insira = str(input("\nO insira um game ?\n"))
        lista.append(insira)
        print("Game inserido com sucesso!!!\n")
        print(lista)

# Select
    elif resposta == 2:
        consultar = str(input("\nQual game quer buscar ?\n"))
        if consultar in lista:
            print("O jogo está na lista\n")
        else:
            consultarn = consultar+'\n'
            if consultarn in lista:
                print("O jogo está na lista\n")
            else:
                print("O item não esta na lista. Gostaria de adicionar ?\n")
                print("[1] Sim")
                print("[2] Não\n")
                cond_consu = int(input("Selecione : "))
                if cond_consu == 1:
                    lista.append(consultar)
                    print("\nJogo adicionado\n")
                    print(lista, "\n")
                else:
                    print("\nVoltando para o menu\n")

# Alterar
    elif resposta == 3:
        print(lista)
        alteracao = str(
            input("\nEscreva o jogo para fazer a substituição : \n"))
        count = int(input(
            "Selecione a posição do game que deseja alterar (ATENÇÃO : A CONTAGEM COMEÇA DO 0)\n"))
        lista[count] = alteracao
        print(lista)

# Delete
    elif resposta == 4:
        print(lista, '\n')
        remover = str(
            input("Digite o game para ser removido (NÃO ESCREVA : '\-n') : \n"))
        if remover in lista:
            lista.remove(remover)
        else:
            removern = remover+'\n'
            lista.remove(removern)
        print(lista)

# Gravar arquivo
    elif resposta == 5:
        arquivo = open("texto.txt", "a")
        arquivo.writelines(line + "\n" for line in lista)
        print("Bliblioteca salva!! (Ao fechar o programa para importar basta digitar a opção 6)")

# Importar arquivo
    elif resposta == 6:
        arquivo = open("texto.txt", "r")
        lista = arquivo.readlines()
        print(lista)
        print("Bliblioteca importada!!")


# Exit
    elif resposta == 7:
        exit()
