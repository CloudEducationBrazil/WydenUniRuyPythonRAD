import re;
import time;

dataCliente = {};

BD = "BD_Cliente.txt";


#BD
def pullData():
    with open(BD, "r+") as Arquivo:
        for k in Arquivo:
            read = k.split("|");
            read.pop(len(read) - 1);
            read[10] = int(read[10]);
            dataCliente[read[3]] = read[:];

def saveData():
    conteudo = "";
    with open(BD, "a+") as arquivo:
        arquivo.seek(0);
        arquivo.truncate();
        for i in dataCliente:
            for k in range(len(dataCliente[i])):
                conteudo += str(dataCliente[i][k]) + "|";
            conteudo += "\n";
        arquivo.writelines(conteudo);


#Validação Cadastro Cliente
def cpfExistente(p):
    return bool(p in dataCliente);

def valCpf(cpf):
    while cpfExistente(cpf) is True:
        cpf = input("CPF já utilizado!\nDigite um CPF válido: ");
    if len(cpf) != 11:
        return False;
    else:
        if not re.match("[0-9]", cpf):
            return False;
        cpf = list(cpf);
        for o in range(len(cpf)):
            cpf[o] = int(cpf[o]);
        mult = [10, 9, 8, 7, 6, 5, 4, 3, 2];
        mult2 = [11] + mult;
        soma = 0;
        soma2 = 0;
        for o in range(len(mult)):
            soma += cpf[o] * mult[o];
        d1 = 11 - (soma % 11);
        if d1 == 10 or d1 == 11:
            d1 = 0;
        cpf.append(d1);
        for o in range(len(mult2)):
            soma2 += cpf[o] * mult2[o];
        d2 = 11 - (soma2 % 11);
        if d2 == 10 or d2 == 11:
            d2 = 0;
        cpf.append(d2);
        return bool(d1 == cpf[9] and d2 == cpf[10]);

def valOthers(variavel, qtd_letras):
    return bool(re.match("[0-9]{" + str(qtd_letras) + "}", variavel));

def valEndereco(p):
    while bool(re.match("[A-Za-z0-9ãõẽíóáç .,º" "]{5,25}", p)) is False:
        p = input("Endereço Inválido!\nDigite um endereço válido, no formato (Rua, Número, Cidade-Estado): ");

def valFone(p):
    while bool(re.match("^\([1-9]{2}\)[2-9]{2,3}[0-9]{2}\-[0-9]{4}$", p)) is False:
        p = input("Número errado!\nDigite um número de telefone válido: ");

def valEmail(email):
    while bool(re.match("[a-z0-9\-\_\.]+\@[\w\-\_\.]+[a-z]{2,4}", email)) is False:
        email = input("Email Inválido!\nDigite um email válido: ");

def valNome(p, l):
    while bool(re.match("[^0-9][a-zA-Zãõçóúáéí ]{2,}", p)) is False:
        p = input(l + " Inválido!\nDigite um válido " + l + ": ");

def valDate(p):
    try:
        date = time.strptime(p, "%d/%m/%Y");
        return bool(date.tm_year <= (int(time.strftime("%Y")) - 18));
    except:
        return False;


#Consulta 
def search(term):
    if term in dataCliente:
        print(dataCliente[term]);
    else:
        print("Usuário não existe!");

def showClientes():
    g = 1;
    for i in dataCliente:
        print(g, " - ", dataCliente[i][0], dataCliente[i][1]);
        g += 1;


#Ediçao de Cadastro
def checkUserExist(p):
    while bool(p not in dataCliente) is True:
        p = input("CPF não existe nos registros!\nDigite um CPF existente: ");

def deleteCliente(p):
    del dataCliente[p];
    saveData();
    print("Cadastro excluído com sucesso!");

def editCPF(p, l, v):
    dataCliente[l] = dataCliente[p][:];
    dataCliente[p][v - 1] = l;
    deleteCliente(p);

def editCliente(p, l, v):
    dataCliente[p][int(v) - 1] = l;
    saveData();
    

def sendEmail(email, cpf, nomeCarro, preco, dia, dateEntrga , by):
    import smtplib;

    #Email Locadora.
    remetente = "vendasonline02023@gmail.com";
    senha = "Fornecedor2022";

    #Destino e Confirmação.
    destinatario = email;
    assunto = 'Confirmação de ' + by;
    if by == "Aluguel":
        texto = "Olá, " + dataCliente[cpf][
            0] + "\nVocê alugou o veículo " + nomeCarro + " na data de hoje (" + dia + "), com prazo de entrega até o dia " + dateEntrga + ".\nValor a ser pago na devolução do veículo: R$" + str(
            preco) + " reais.\nAgradecemos a preferência.";
    else:
        texto = "Olá, " + dataCliente[cpf][
            0] + "\nAviso de devoloção do veículo " + nomeCarro + "!\nAgradecemos a preferência.";

    msg = '\r\n'.join([
        'From: %s' % remetente,
        'To: %s' % destinatario,
        'Subject: %s' % assunto,
        '',
        '%s' % texto
    ]);
    try:
        server = smtplib.SMTP("smtp.gmail.com:587");
        server.starttls();
        server.login(remetente, senha);
        server.sendmail(remetente, destinatario, msg.encode('utf-8'));
        server.quit();
    except:
        print("Erro ao enviar o email!\nVerifique sua conexão com a internet ou o email do usuário se está correto!");





class newCliente(object):
    def __init__(self, a, b, c, d, e, f, g, h, i, j, l):
        dataCliente[d] = [a, b, c, d, e, f, g, h, i, j, l];
        saveData();