import pytest
import mariadb
import sys
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

setProduct = TshirtProduct.addToBase('tshirt', [3456, 'Футболка', 45, 'Gucci', 48, 'green'], cur)
statsProduct = TshirtProduct.showStats('manufacturer', 'tshirt', cur)
getProduct = TshirtProduct.getData('price', 3456, cur)