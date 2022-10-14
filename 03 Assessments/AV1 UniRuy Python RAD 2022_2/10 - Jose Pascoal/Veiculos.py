import calendar;
import re;
from datetime import datetime;

dadosVeiculos = {};
veiculosAlugados = {};

BD_Veiculos = "BD_Veiculos.txt";
BD_VeiculosAlugados = "BD_VeiculosAlugados.txt"

#BD
def saveData(BD, lista):
    conteudo = '';
    with open(BD, 'a+') as arquivo:
        arquivo.seek(0);
        arquivo.truncate();
        for i in lista:
            for q in range(len(lista[i])):
                conteudo += str(lista[i][q]) + '|';
            conteudo += '\n';
        arquivo.writelines(conteudo);

def pullData():
    with open(BD_Veiculos, 'r+') as Arquivo:
        for q in Arquivo:
            read = q.split('|');
            read[7] = int(read[7]);
            read[8] = int(read[8]);
            read.pop(len(read) - 1);
            dadosVeiculos[read[4]] = read[:];

def pullDataAlugados():
    with open(BD_VeiculosAlugados, 'r+') as Arquivo:
        for q in Arquivo:
            read = q.split('|');
            read.pop(len(read) - 1);
            veiculosAlugados[read[4]] = read[:];
            
#Carros Alugados
def CarrosAlugados():
    g = 1;
    print("Carros alugados: ");
    
    for i in dadosVeiculos:
        print(g, "-", veiculosAlugados[i][0]);
        g += 1;


#Disponível Para Alugar
def showCarros():
    g = 1;
    print("Carros disponíveis: ");
    
    for i in dadosVeiculos:
        if dadosVeiculos[i][8] == 1:
            print(g, "-", dadosVeiculos[i][0], "| R$: ", dadosVeiculos[i][3], "| Placa: ", dadosVeiculos[i][4]);
            g += 1;


#Validação Cadastro Veiculos
def valModelo(m):
    while bool(re.match('[a-zA-Z0-9çãõẽéêíóá .,' ']{2,30}', m)) is False:
        m = input("Modelo de veículo inválido!\nDigite um modelo válido: ");

def valCor(c):
    while bool(re.match('[a-zA-Z .' ']{4,8}', c)) is False:
        c = input("Cor inválida!\nDigite uma cor válida: ");

def valAno(a):
    while bool(re.match('[1-2][0-9][0-9][0-9]', a)) is False:
        a = input("Ano inválido!\nDigite um ano válido: ");

def valPreco(p):
    while bool(re.match('[0-9]{2,5}', p)) is False:
        p = input("Preço inválido!\nDigite um preço válido no formato '000' ou '0000': ");

def OthrsExistente(p):
    return not bool(p in dadosVeiculos);

def CheckExistente(p, v):
    return bool(p in v);

def valPlaca(p):
    while bool((re.match("^\w{3}-\d{4}$", p) and OthrsExistente(p))) is False:
        p = input("Placa do veículo inválida!\nDigite a placa do veículo no formato 'XXX-0000': ");

def valRenavan(o, t):
    while bool((int(o) < 2013 and len(t) == 9) or (int(o) >= 2013 and len(t) == 11)) is False:
        t = input("Número renavam inválido!\nDigite um número renavam válido: ");

def valKM(km):
    while bool(re.match('[0-9]{1,6}', km)) is False:
        km = input("Quilometragem inválida!\nDigite uma quilometragem válida no formato '000000': ");


#Data
def valDate(p):
    if (re.match('[0-9]{2}/[0-9]{2}/[0-9]{4}', p)):
        p = datetime.strptime(p, "%d/%m/%Y");
        d = datetime.strptime(todayDate(), "%d/%m/%Y");
        if p > d:
            return True;
        else:
            return False;
    else:
        return False;


def diffDias(data):
    data2 = datetime.now().date();
    data = datetime.strptime(data, "%d/%m/%Y").date();
    dif = data - data2;
    dif = dif.days;
    return int(dif);

def diffDias2(data):
    data2 = datetime.now().date();
    data = datetime.strptime(data, "%d/%m/%Y").date();
    dif = data2 - data;
    dif = dif.days;
    return int(dif);

def todayDate():
    now = datetime.now();
    return ("%s/%s/%s" % (now.day, now.month, now.year));

def calendarShow():
    now = datetime.now();
    cal = calendar.month(now.year, now.month);
    print("Aqui está o calendário:");
    print(cal);


# Ediçao Cadastro Veículos
def checkCarroExistente(p):
    while bool(p not in dadosVeiculos) is True:
        p = input("A placa do carro não existe nos registros!\nDigite uma placa válida no formato 'XXX-0000': ");

def editCarro(p, l, v):
    dadosVeiculos[p][v - 1] = l;
    saveData(BD_Veiculos, dadosVeiculos);

def deleteCar(p):
    del dadosVeiculos[p];
    saveData(BD_Veiculos, dadosVeiculos);
    
    
    
    

class newCarro(object):
    def __init__(self, a, b, c, d, e, f, g, h, i):
        dadosVeiculos[e] = [a, b, c, d, e, f, g, h, i];
        saveData(BD_Veiculos, dadosVeiculos);
