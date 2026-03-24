# pip install mysql-connector
import mysql.connector
from mysql.connector import Error

import os

def ConexaoBD():  # conexão com o BD
    con = None
    try:
        con = mysql.connector.connect(host='localhost', user='root', password='1234',
                                      database='vendas'
                                      )
    except Error as ex:
        print(ex)
    return con


def dql(query):  # select
    vcon = ConexaoBD()
    cursor = vcon.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    vcon.close()
    return res

def dml(query):  # transações
    try:
        vcon = ConexaoBD()
        cursor = vcon.cursor()
        cursor.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)

ConexaoBD()
'''
dml("insert into tb_sellers (name) values ('Maria Cardoso2')")
dml("insert into tb_sellers (name) values ('Maria Cardoso')")
dml("insert into tb_sellers (name) values ('Zezinha Cardoso')")
dml("update tb_sellers set name = 'Maria Rita' where name = 'Maria Cardoso'")
dml("delete from tb_sellers where name = 'Maria Cardoso2'")

recordset = dql('select * from tb_sellers')
for linha in recordset:
    print(linha)
'''