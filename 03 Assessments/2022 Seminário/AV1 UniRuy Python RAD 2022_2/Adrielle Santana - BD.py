#Aplicação Vendas de Abadás e Camarote 
#pip install mysql-connector-python - instalando a biblioteca MySQL Connector
#pip install pandas - instalando a biblioteca pandas
# https://github.com/adrielesfigueredo/Aplica-o-Vendas-de-Abad-s-e-Camarote-

#Importando as bibliotecas
import mysql.connector
from mysql.connector import Error
import pandas as pd

#Conectando ao MySQL Server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Conexão de banco de dados bem-sucedida")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

    connection = create_server_connection("localhost", "root", pw)

#Criando um novo banco de dados
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Banco de dados criado com sucesso")
    except Error as err:
        print(f"Error: '{err}'")

    create_database_query = "CREATE DATABASE vendas"
    create_database (connection, create_database_query)

#Conectando ao banco de dados
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Conexão de banco de dados bem-sucedida")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#Criando uma função para execução de consultas
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Consulta bem-sucedida")
    except Error as err:
        print(f"Error: '{err}'")

#Criando tabelas
    create_bloco_table = """
    CREATE TABLE bloco (
      bloco_id INT PRIMARY KEY,
      bloco_name VARCHAR(40) NOT NULL,
      circuito VARCHAR(20) NOT NULL,
      atracao VARCHAR(20) NOT NULL,
      dias DATE NOT NULL,
      valor INT NOT NULL
      );
    """

    create_camarote_table = """
    CREATE TABLE camarote (
      camarote_id INT PRIMARY KEY,
      camarote_name VARCHAR(40) NOT NULL,
      circuito VARCHAR(20) NOT NULL,
      dias DATE NOT NULL,
      valor INT NOT NULL
      );
    """

    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, create_bloco_table)
    execute_query(connection, create_camarote_table)

#Preenchendo as tabelas
    pop_bloco = """
    INSERT INTO bloco VALUES
    (1, 'Coruja', 'Barra Ondina', 'Ivete Sangalo', '2023-02-18', 1100),
    (2, 'Vumbora',  'Barra Ondina', 'Bell Marques', '2023-02-17', 850), 
    (3, 'Largadinho', 'Barra Ondina', 'Claudia Leitte', '2023-02-19', 650),
    (4, 'Bloco do Nana',  'Barra Ondina', 'Léo Santana', '2023-02-17',  340),
    (5, 'Cheiro', 'Barra Ondina', 'Banda Cheiro', '2023-02-17',  200);
    """

    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, pop_bloco)

    pop_camarote = """
    INSERT INTO camarote VALUES
    (1, 'Camarote Salvador', 'Barra Ondina', '2023-02-18', 2150),
    (2, 'Camarote Brahma Salvador', 'Barra Ondina', '2023-02-17', 790), 
    (3, 'Camarote Club', 'Barra Ondina', '2023-02-19', 780),
    (4, 'Camarote Planeta Band All Inclusive', 'Barra Ondina', '2023-02-17', 650),
    (5, 'Camarote Premier', 'Barra Ondina', '2023-02-17', 360);
    """

    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, pop_camarote)

#Lendo os dados
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

    consulta = """
    SELECT *
    FROM bloco;
    """

    connection = create_db_connection("localhost", "root", pw, db)
    results = read_query(connection, consulta)

    for result in results:
      print(result)

#Formatando os resultados em uma lista
    from_db = []

    for result in results:
      result = result
      from_db.append(result)

#Atualizando registros
    update = """
    UPDATE camarote 
    SET camarote_name = 'Camarote Planeta Band Open Bar' 
    WHERE camarote_id = 4;
    """

    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, update)

#Adicionando novos dados
    sql = '''
        INSERT INTO bloco (bloco_id, bloco_name, circuito, atracao, dias, valor) 
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        
    val = [
        (6, 'Crocodilo', 'Barra Ondina', 'Daniela Mercury', '2023-02-20', 550)
    ]

    connection = create_db_connection("localhost", "root", pw, db)
    execute_list_query(connection, sql, val)

#Apagando registros
    delete_bloco = """
    DELETE FROM bloco 
    WHERE  bloco_id = 5;
    """

    connection = create_db_connection("localhost", "root", pw, db)
    execute_query(connection, delete_bloco)