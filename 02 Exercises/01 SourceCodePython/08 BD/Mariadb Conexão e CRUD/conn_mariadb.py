import mariadb
import sys

try:
    conn = mariadb.connect(
        host="localhost",
        port=3306,
        user="root",
        password=None,
        database="clinicamedica")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)