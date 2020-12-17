import pytest
import mariadb
import sys
import Product
import TshirtProduct


# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user='root',
        password='1234',
        host='localhost',
        port=3306,
        database='test'
    )
except mariadb.Error as e:
    print(f'Error connecting to MariaDB Platform: {e}')
    sys.exit(1)
# Get Cursor
cur = conn.cursor()
