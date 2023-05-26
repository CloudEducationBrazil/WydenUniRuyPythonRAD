arqLog = open("financeiro.log", "r")
saldo = 0

for linha in arqLog:
    print(linha.split()[0])
    saldo = saldo + int(linha.split()[0])

print("Saldo da Empresa =", saldo)

arqLog.close()