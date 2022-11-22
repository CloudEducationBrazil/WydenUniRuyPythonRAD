import sqlite3 as lite

#criando conexão com o banco
connectdb = lite.connect("SERVICES.db")

#Insert
def insert(service):
    with connectdb:
        cursor = connectdb.cursor()
        query = "INSERT INTO SERVICE(NUMBER_OS, TYPE_SERVICE, DESCRIPTION, DATE, PROVIDER, CLIENT, VALUE) VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, service)


#Select
def select():
    service = []
    with connectdb:
        cursor = connectdb.cursor()
        query = "SELECT ID, NUMBER_OS, TYPE_SERVICE, DESCRIPTION, DATE, PROVIDER, CLIENT, VALUE FROM SERVICE"
        cursor.execute(query)
        result = cursor.fetchall()
        
        for list in result:
            service.append(list)

    return service

#Update
def update(service):
    with connectdb:
        cursor = connectdb.cursor()
        query = "UPDATE SERVICE SET NUMBER_OS = ?, TYPE_SERVICE = ?, DESCRIPTION = ?, DATE = ?, PROVIDER = ?, CLIENT = ?, VALUE = ? WHERE ID = ?"
        cursor.execute(query, service)


#Delete
def delete(id):
    with connectdb:
        cursor = connectdb.cursor()
        query = "DELETE FROM SERVICE WHERE ID = ?"
        cursor.execute(query, id)
