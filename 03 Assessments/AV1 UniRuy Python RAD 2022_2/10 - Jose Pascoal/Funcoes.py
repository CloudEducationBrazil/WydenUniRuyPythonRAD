import Cliente as C;
import Veiculos as V;

BD = ["BD_Veiculos.txt", "BD_VeiculosAlugados.txt", "BD_Cliente.txt"];

#BD
def creatFileIfNotExist():
    for i in BD:
        file = open(i, 'a+').close();

def dataPullAll():
    creatFileIfNotExist();
    C.pullData();
    V.pullData();
    V.pullDataAlugados();


#Cadastro Novo Cliente
def menuOp1():
    NomeCliente = input("Nome: ");
    C.valNome(NomeCliente, "Nome");

    SobrenomeCliente = input("Sobrenome: ");
    C.valNome(SobrenomeCliente, "Sobrenome");

    dataN = input("Digite a data de nascimento (dd/mm/aaaa): ");
    while C.valDate(dataN) is False:
        dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ");

    CPF = input("CPF: ");
    while not C.valCpf(CPF):
        CPF = input("CPF Inválido!\nDigite um CPF válido: ");

    NomeMae = input("Nome da Mãe: ");
    C.valNome(NomeMae, "Nome");

    RG = input("RG: ");
    while C.valOthers(RG, 9) is False:
        RG = input("RG Inválido!\nDigite um RG válido: ");

    Email = input("Email:");
    C.valEmail(Email);

    CNH = input("CNH: ");
    while C.valOthers(CNH, 10) is False:
        CNH = input("CNH Inválida!\nDigite um CNH válido: ");

    Endereco = input("Endereço, no formato (Rua, Número, Cidade-Estado): ");
    C.valEndereco(Endereco);

    Fone = input("Telefone (xx)xxxxx-xxxx: ");
    C.valFone(Fone);

    C.newCliente(NomeCliente, SobrenomeCliente, dataN, CPF, NomeMae, RG, Email, CNH, Endereco, Fone, 0);
    print("Cadastro efetuado com sucesso!");


#Busca Cliente
def menuOp2():
    termo = input("Digite o CPF do cliente que deseja buscar: ");
    C.search(termo);


#Edição Cliente
def menuOp3():
    cpf = input("Digite o CPF do cliente que deseja editar: ");
    C.checkUserExist(cpf);
    print("O que deseja alterar?");
    print("1 - Nome");
    print("2 - Sobrenome");
    print("3 - Data de nascimento");
    print("4 - CPF");
    print("5 - Nome da mãe");
    print("6 - RG");
    print("7 - Email");
    print("8 - Habilitação");
    print("9 - Endereço");
    print("10 - Telefone");
    print("0 - Voltar");

    alt = input("Qual campo deseja alterar? ");

    if alt == '1':
        NomeCliente = input("Digite o novo nome: ");
        C.valNome(NomeCliente, "Nome");
        C.editCliente(cpf, NomeCliente, alt);
    elif alt == '2':
        SobrenomeCliente = input("Digite o novo sobrenome: ");
        C.valNome(SobrenomeCliente, "Sobrenome");
        C.editCliente(cpf, SobrenomeCliente, alt);
    elif alt == '3':
        dataN = input("Digite a nova data de nascimento (dd/mm/aaaa): ");
        while C.valDate(dataN) is False:
            dataN = input("Data inválida!\nDigite a data de nascimento no formato (dd/mm/aaaa): ");
        C.editCliente(cpf, dataN, alt);
    elif alt == '4':
        CPF = input("Digite o novo CPF: ");
        while C.valCpf(CPF) is False:
            CPF = input("CPF Inválido!\nDigite um CPF válido: ");
        C.editCliente(cpf, CPF, alt);
    elif alt == '5':
        NomeMae = input("Digite o novo nome da Mãe: ");
        C.valNome(NomeMae, "Nome");
        C.editCliente(cpf, NomeMae, alt);
    elif alt == '6':
        RG = input("RG: ");
        while C.valOthers(RG, 9) is False:
            RG = input("RG Inválido!\nDigite um RG válido: ");
        C.editCliente(cpf, RG, alt);
    elif alt == '7':
        Email = input("Email:");
        C.valEmail(Email);
        C.editCliente(cpf, Email, alt);
    elif alt == '8':
        CNH = input("CNH: ")
        while C.valOthers(CNH, 10) is False:
            CNH = input("CNH Inválida!\nDigite uma CNH válida: ");
        C.editUser(cpf, CNH, alt);
    elif alt == '9':
        Endereco = input("Endereço, no formato (Rua, Número, Cidade-Estado): ");
        C.valEndereco(Endereco);
        C.editCliente(cpf, Endereco, alt);
    elif alt == '10':
        Fone = input("Telefone (xx)xxxxx-xxxx: ");
        C.valFone(Fone)
        C.editCliente(cpf, Fone, 10);
    else:
        print("Opção invalida!");
    print("\nModificado com sucesso!\n");


#Excluir Cliente
def menuOp4():
    optDel = input("Informe o CPF do usuário que deseja excluir do nosso banco de dados: ");
    C.deleteUser(optDel);


#Alugar Carro
def menuOp5():
    cpfCLiente = input("Digite o CPF do usuário que deseja alugar o carro: ");
    while V.CheckExistente(cpfCLiente, C.dataCliente) is False:
        cpfCLiente = input("CPF não encontrado!\nDigite o CPF do usuário que deseja alugar o carro: ");

    V.showCarros();

    placaCarro = input("Digite a placa do carro á ser alugado: ");
    while V.CheckExistente(placaCarro, V.dadosVeiculos) is False:
        placaCarro = input("Placa não encontrada!\nDigite uma Placa válida: ");

    if V.dadosVeiculos[placaCarro][8] == 0:
        print("Veículo não disponível no momento!\n Status: ALUGADO!");
    else:
        V.calendarShow();

        dateDevolution = input("Data de entrega[dd/mm/aaaa]: ");
        while V.valDate(dateDevolution) == False:
            dateDevolution = input("Data Inválida! Data de entrega[dd/mm/aaaa]: ");

        preco = V.diffDias(dateDevolution) * int(V.dadosVeiculos[placaCarro][3]);

        print("O preço do aluguel é", preco);
        cont = input("Continuar(S/n)? ");

        if cont.upper() == "S":
            pay = input("Pagamento á vista(S/n)? ");

            if pay.upper() == "S":
                preco = 0;

            C.dataCliente[cpfCLiente][10] += 1;
            V.dadosVeiculos[placaCarro][7] += 1;
            V.dadosVeiculos[placaCarro][8] -= 1;
            V.veiculosAlugados[placaCarro] = cpfCLiente, preco, V.todayDate(), dateDevolution, placaCarro;
            
            V.saveData(V.BD_VeiculosAlugados, V.veiculosAlugados);

            C.saveData();

            email = C.dataCliente[cpfCLiente][6];
            cpf = C.dataCliente[cpfCLiente][3];
            nomeCarro = V.dadosVeiculos[placaCarro][0];
            print("Enviando e-mail de confirmação...");
            C.sendEmail(email, cpf, nomeCarro, preco, V.todayDate(), dateDevolution, "Aluguel");
            V.saveData(V.BD_Veiculos, V.dadosVeiculos);
            print("E-mail enviado!");
            cont= input("Aperte Enter para continuar...");


#Pagamento E Devolução
def menuOp6():
    placaCarro = input("Digite a placa do carro: ");
    dataDeEntrega = V.veiculosAlugados[placaCarro][3];
    diff = V.diffDias2(dataDeEntrega);

    if diff >= 1:
        print("Você irá pagar Juros!\nVocê agora deve: ", V.veiculosAlugados[placaCarro][1] * diff);
        cont = input("Aperte Enter para confirmar o pagamento e a devolução!");

    cpf = V.veiculosAlugados[placaCarro][0];
    email = C.dataCliente[cpf][6];
    nomeCarro = V.dadosVeiculos[placaCarro][0];
    V.veiculosAlugados.pop(placaCarro);
    V.dadosVeiculos[placaCarro][8] += 1;
    V.saveData(V.BD_VeiculosAlugados, V.veiculosAlugados);
    V.saveData(V.BD_Veiculos, V.dadosVeiculos);
    print(nomeCarro, "devolvido.");
    print("Enviando e-mail de confirmação...");
    C.sendEmail(email, cpf, nomeCarro, "", "", "", "Devolução");
    print("E-mail enviado!");
    cont = input("Aperte Enter para confirmar a devolução!");
    

#Veículos Disponíveis e Indisponíveis 
def menuOp7():
    g = 1;
    for i in V.dadosVeiculos:
        if V.dadosVeiculos[i][8] != 0:
            print('\t', g, '-', V.dadosVeiculos[i][0],"- DISPONÍVEL");
            g += 1;
        else:
            print('\t', g, '-', V.dadosVeiculos[i][0],"- INDISPONÍVEL");
            g += 1;


#Emprestimos Feitos
def menuOp8():
    for i in V.veiculosAlugados:
        placa = V.veiculosAlugados[i][4];
        print("-",V.dadosVeiculos[placa][0]);


#Menu Veículos
def menuOp9():
    V.pullData()
    op = input("Digite uma opção do menu acima: ")

    if op == '1':
        CarModelo = input("Qual o modelo do veículo? ");
        V.valModelo(CarModelo);
        CarCor = input("Qual a cor do veículo? ");
        V.valCor(CarCor);
        CarAno = input("Qual o ano do veículo? ");
        V.valAno(CarAno);
        CarPreco = input("Qual o preço do veículo no formato '000' ou '0000'? ");
        V.valPreco(CarPreco);
        CarPlaca = input("Qual a placa de veículo no formato 'XXX-0000'? ");
        V.valPlaca(CarPlaca);
        CarRenavam = input("Qual o número renavam do veículo? ");
        V.valRenavan(CarAno, CarRenavam);
        CarKM = input("Digite os quilômetros rodados do veículo no formato '000000': ");
        V.valKM(CarKM);
        V.newCarro(CarModelo, CarCor, CarAno, CarPreco, CarPlaca, CarRenavam, CarKM, 0, 1);
        print("Cadastro efetuado com sucesso!");


#Edição Cadastro Veículo
    elif op == '2':
        editar = input("Digite a placa do veículo que deseja modificar cadastro no foramto 'XXX-0000': ");
        V.checkCarroExistente(editar);
        print("O que deseja alterar?");
        print("1 - Cor do veículo");
        print("2 - Preço do aluguel");
        print("3 - Quilômetros rodados do veículo");
        print("0 - Voltar");
        while op != '10':
            op = input("Qual campo deseja alterar? ");

            if op == "1":
                CarCor = input("Qual a cor do veículo? ");
                V.valCor(CarCor);
                V.editCarro(editar, CarCor, 2);
            elif op == "2":
                CarPreco = input("Qual o preço do veículo no formato '000.00' ou '0000.00'? ");
                V.valPreco(CarPreco)
                V.editCarro(editar, CarPreco, 4);
            elif op == "3":
                CarKM = input("Digite os quilômetros rodados do veículo no formato '000000': ");
                V.valKM(CarKM)
                V.editCarro(editar, CarKM, 7);
            elif op == "0":
                break;