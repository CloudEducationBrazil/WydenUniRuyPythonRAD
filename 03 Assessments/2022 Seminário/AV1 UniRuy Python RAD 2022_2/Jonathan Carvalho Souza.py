# https://github.com/jonathan-souza01/Aplica-o-console-Python/blob/main/Cadastro%20de%20novelas%20exportadas.txt
# Cadastro de novelas exportadas
import os
import time 
novelasexpo = []

while True:
    os.system ('clear')
    
    # MENU INICIAL
    print ('Cadastro de novelas exportadas')
    print ('')
    print (' 1 - Inserir')
    print (' 2 - Consultar')
    print (' 3 - Atualizar')
    print (' 4 - Apagar')
    print (' 5 - Sair do Programa')
    print ('')
    opc = input('Digite a opção desejada: ')
  
    
    os.system("clear")
    
    if opc == '1':
       while True:
           ID = input ('Digite o número do ID: ')
           nov = input('Digite o nome da novela: ')
           qtd_paises = input('Digite a quantidade de paises: ')
           ano = input('Digite o ano da novela: ')
           autor = input('Digite o autor da novela: ')
           os.system("clear")
           print ('Inclusão feita com sucesso!')
           novelasexpo.append ([ID, nov, qtd_paises, ano, autor])
           time.sleep(1)
           break
       
    elif opc == '2':
            ID = input ('Digite o ID que deseja consultar: ')
            for x in range(len(novelasexpo)):
                print (novelasexpo[x])
                time.sleep(2)
         
    elif opc == '3':
        nov = input ('Digite o ID da novela correspondente: ')
        for x in range(len(novelasexpo)):
            print ('o que gostaria de atualizar? ')
            print (' 1 - qtd_paises') 
            print (' 2 - ano') 
            print (' 3 - autor')
            print (' digite uma opção: ')
            time.sleep(5)
        break
        
        
    elif opc == '4' :
        
        ID = input ('Digite o ID que deseja apagar todos os dados: ')
        ind = 1
        for x in range (len(novelasexpo)):
            if ID in novelasexpo [x][0]:
                ind = x
                break
            if ind > 0:
                novelasexpo.pop(ind)
                print ("Novela excluida com sucesso.")
                time.sleep(5)
            else: print ("Novela não encontrada")
        
    elif opc == "5":
        print ('Saindo do Programa, Até Breve!!! ')
        exit()