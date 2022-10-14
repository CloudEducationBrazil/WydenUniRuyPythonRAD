import csv

with open("visa.csv", "r") as arquivo:
    verificacao = csv.reader(arquivo, delimiter = ",")
    for linha in verificacao:
        print(linha)





with open("elo.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever=csv.writer(arquivo, delimiter=',', lineterminator='\n')
                for x in range (len(elo)):
                    numero = elo[x]
                    escrever.writerow(numero)

            with open("outros_nome.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever=csv.writer(arquivo, delimiter=',', lineterminator='\n')
                for x in range (len(outros_nome)):
                    numero = outros_nome[x]
                    escrever.writerow(numero)

            with open("outros_numero.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever=csv.writer(arquivo, delimiter=',', lineterminator='\n')
                for x in range (len(outros_numero)):
                    numero = master[x]
                    escrever.writerow(numero)






                    with open("outros_nome.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever=csv.writer(arquivo, delimiter=',', lineterminator='\n')
                for x in range (len(outros_nome)):
                    numero = outros_nome[x]
                    escrever.writerow(numero)

            with open("outros_numero.csv", "w", newline="", encoding="utf-8") as arquivo:
                escrever=csv.writer(arquivo, delimiter=',', lineterminator='\n')
                for x in range (len(outros_numero)):
                    numero = master[x]
                    escrever.writerow(numero)
                