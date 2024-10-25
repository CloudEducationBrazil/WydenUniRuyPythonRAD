# https://youtu.be/cbtluIkqhiw
import os
from conn_mariadb import conn

def menu():
    print("Cadastro de Departamento")
    print("1-Inclusão")
    print("2-Alteração")
    print("3-Exclusão")
    print("4-Exibir")
    print("9-Sair")

def limpar_tela():
        # Comando para Windows
    if os.name == 'nt':
        os.system('cls')
    # Comando para Linux e Mac
    else:
        os.system('clear')

def fInsertDepartamento():
    try:
        nomeDepart = input("Informe departamento: ")
        
        cursor = conn.cursor()
        sql = "insert into departamentos (nome) values (?)"
        
        if ( nomeDepart != "" ): 
          cursor.execute(sql, [nomeDepart])
          conn.commit()

        print("cadastrado")
    except:
        print("error")

def fDeleteDepartamento():
    try:
        idDepart = int(input("Informe o código do departamento: "))

        cursor = conn.cursor()
        sql = "delete from departamentos where id = ?"
        cursor.execute(sql, [idDepart])
        conn.commit()

        print("exclusão com sucesso")
    except:
        print("error")

def fUpdateDepartamento():
    try:
        idDepart = int(input("Informe o código do departamento: "))
        nomeDepart = input("Informe NOVO departamento: ")

        cursor = conn.cursor()
        sql = "update departamentos set nome = ? where id = ?"
        cursor.execute(sql, [nomeDepart, idDepart])
        conn.commit()

        print("alteração com sucesso")
    except:
        print("error")

def fReadDepartamento():
    try:
        cursor = conn.cursor()
        sql = "select * from departamentos"
        cursor.execute(sql)
        lista = cursor.fetchall()
        print(lista)
        
        pause = input("Pressione Enter para continuar...")
    except:
        print("error")

menu()

op = '0'
while (op != '9'):
   op = input("Opção? ")
   if ( op == '1' ):
      fInsertDepartamento()
   elif ( op == '2'):
      fUpdateDepartamento()
   elif ( op == '3'):
      fDeleteDepartamento()
   elif ( op == '4'):
      fReadDepartamento()
   
   limpar_tela()
   menu()

conn.close()
