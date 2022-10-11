# https://github.com/Artheml/Python/blob/main/CRUD
# estoque

estoque = ["cerveja", "vinho", "vodka", "água", "caipirinha", "tequila"]
numestoque = [0, 100]

print("--------- Bem vindo(a) ao sistema de Estoque --------- ")

while True:

    escolha = 0

    if escolha != 6:

        print('''Escolha uma das opções abaixo
          1- Verificar estoque ou rebastecer estoque \n
          2- Alterar produto \n
          3- Remover produto \n
          4- Gravar em arquivo \n
          5- Importar em arquivo \n
          6- Sair \n''')
        escolha = int(input("Digite o número da opção escolhida: "))

        if escolha == 1:

            numestoque = [0, 100]
            a = int(input("Digite a quantidade de produtos: "))

    for a in numestoque:
        if a >= (100) in numestoque:
            print(" produto suficiente")

    else:
        print(" reabastecer estoque ")
        print("Deseja reabastecer estoque?sim ou não? ")
        sim_or_nao = input("sim ou não: ")

    if sim_or_nao == "não":
        print("Você escolheu não")
        break

    elif sim_or_nao == "sim":

        s = str(input(
            "Qual produto você deseja reabastecer? cerveja, vinho, vodka, água, caipirinha ou tequila ?:  "))
        estoque.append(s)

        estoque = [0, 100]

        a = int(input("O quanto você deseja reabastecer? "))
        numestoque.append(str(input("Estoque reabastecido com {}".format(a))))
        print(a)

escolha = 0
if escolha == 2:

    for alterar in estoque:
        estoque = ["cerveja", "vinho", "vodka",
                   "água", "caipirinha", "tequila"]
print(estoque)

alterar = str(input("Digite o que deve ser alterado: "))
count = int(
    input("Selecione a posição (Observação: a posição começa da contagem 0): "))
if count == 1:
    count = 0
estoque[count] = alterar
print(estoque)

else:
    estoque[count] = alterar
    print(estoque)


if escolha == 3:

    for remove in estoque:
        estoque = ["cerveja", "vinho", "vodka",
                   "água", "caipirinha", "tequila"]

print(estoque)

remove = str(input("Digite o que você quer remover: "))

if remove in estoque:
    estoque.remove(remove)
    print(estoque)
else:
    print("Erro")
    exit()


if escolha == 4:

    estoque = ['cerveja', 'vinho', 'vodka', 'água', 'caipirinha', 'tequila']
    print(estoque)
arquivo = open("estoque,txt", "w")
arquivo.writelines(lines + "\n" for lines in estoque)


if escolha == 5:

    estoque = ['cerveja', 'vinho', 'vodka', 'água', 'caipirinha', 'tequila']
    print(estoque)
    arquivo = open("estoque,txt", "r")
estoque = arquivo.readline()
print(estoque)


if escolha == 6:

    print("Encerrando o programa...")

else:

    print("Tente novamente!")
