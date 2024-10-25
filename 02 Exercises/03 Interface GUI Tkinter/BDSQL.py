# pip install mysql-connector
# pip install mysql-connector-python
# pip install python-dotenv

import os
from dotenv import load_dotenv
import mysql.connector 
from mysql.connector import Error

load_dotenv()

conn = None 
# tratamento d exceção = erro
try:
    # Objeto de conexão // mysql+mysqlconnector://root:5555@localhost:3305
    # os.getenv("HOST"), os.getenv("DATABASE"), os.getenv("USERNAME"), os.getenv("PASSWD")
    # os.getenv("host"), os.getenv("database"), os.getenv("user"), os.getenv("password")
    print(os.getenv("HOST"))
    print(os.getenv("DATABASE"))
    print(os.getenv("USERNAME"))
    print(os.getenv("PASSWD"))
    
    # host="localhost", database="clinicamedica", user="root", password=None, port=3306
    conn = mysql.connector.connect(host="localhost", database="clinicamedica", user="root", password=None, port=3306)
    if conn.is_connected():
        print("conectado")
        print(conn.get_server_info())

    cursor = conn.cursor()
    cursor.execute("select database(); ")
    linha = cursor.fetchone()
    print("conectado ao banco de dados: ", linha)

    #cursor = conn.cursor()
    nome = "Nome fulano de tal"
    sql = f"insert into tb_sellers (Name) values ('{nome}')"
    cursor.execute(sql)
    conn.commit()
    print("Inserido com sucesso")

    nome = "recursos humanos"
    sql = f"update tb_sellers set Name = '{nome}' where Id = 63"  # escolher um id do BD da tab.
    cursor.execute(sql)
    conn.commit()
    print("Atualizado com sucesso")

    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão encerrada")
except Error as e:
    print('Error:', e)
finally:
    # Verifica se o BD está conectado
    if conn != None:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print('\nConexão encerrada com o MySQL')
