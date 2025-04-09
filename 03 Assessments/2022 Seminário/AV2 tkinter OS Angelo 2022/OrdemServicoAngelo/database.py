#cria o banco de dados
import sqlite3

database = sqlite3.connect("SERVICES.db")

with database:
    cursor = database.cursor()
    cursor.execute(
        "CREATE TABLE SERVICE(ID INTEGER PRIMARY KEY AUTOINCREMENT, NUMBER_OS INTEGER NOT NULL, TYPE_SERVICE TEXT NOT NULL, DESCRIPTION TEXT NOT NULL, DATE TEXT NOT NULL, PROVIDER TEXT NOT NULL, CLIENT TEXT NOT NULL, VALUE TEXT NOT NULL)"
    )