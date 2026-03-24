with open("listaNiver.txt", "w", encoding="utf-8") as f:
    f.write("Julia,17\n")
    f.write("Maria,69\n")
    f.write("josy,51\n")
    f.close()

with open("listaNiver.txt") as text_file:
    lista = text_file.read().splitlines()
    print(lista)
    f.close()

with open("listaNiver.txt") as text_file:
    count = sum(1 for _ in text_file)
    print('line count:', count)
    f.close()

with open("listaNiver.txt") as text_file:
    for line in text_file:
        if line.startswith("josy"):
            print("oiiii", line)
    f.close()

fname = input('Digite o nome do arquivo: ')
try:
    with open(fname) as text_file:
        conteudo = text_file.read()
        print('aqui', conteudo)
        f.close()

except Exception as e:
    print(f'Erro na abertura do arquivo {fname}: {e}')
    f.close()
    quit()