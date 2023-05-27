with open("notas.txt", "wt", encoding = "utf-8") as f:
    f.write("5  rita\n");
    f.write("2  joana\n");
    f.write("8  julia\n");
    f.write("9  josy\n");
    f.write("5  paulo\n");
    f.write("4  antidio\n");
    f.write("7  pedro\n");
    f.write("2  thaun\n");
    f.write("6  brenda\n");
    f.write("8  helder");
    f.close();

f = open("notas.txt", "r");

# split eh da list
lista = f.read().split('\n');

sum = 0
for av1 in lista:
    print(av1)
    sum += int(av1[0])
    
print('quantidade de elementos da lista ', len(lista))
print(sum/len(lista))

