import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='developer',
    password='12',
    database='bdcrud',
)

# CRUD

# CREATE
nome = "João Vítor Pamponet Esteves"
matricula = 1
comando = f'INSERT INTO alunos (nome, matricula) VALUES ("{nome}", {matricula})'
cursor = conexao.cursor()
cursor.execute(comando)
conexao.commit()

# READ
comando = f'SELECT * FROM alunos'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

# UPDATE
nome = "João Vítor Pamponet Esteves"
matricula = 20
comando = f'UPDATE alunos SET matricula = {matricula} WHERE nome = "{nome}"'
cursor.execute(comando)
conexao.commit()

# DELETE
nome = "João Vítor Pamponet Esteves"
comando = f'DELETE FROM alunos WHERE nome = "{nome}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()
