import mariadb
import sys
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="1234",
        host="localhost",
        port=3306,
        database="test"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
# Get Cursor
cur = conn.cursor()

keys = ['type', 'brand', 'amount', 'manufacturer', 'price', 'size']
columns = dict.fromkeys(keys, None)
try:
    cur.execute('CREATE TABLE test')
except mariadb.Error as e:
    print(f"Не создал таблицу {e}")

try:
    for value in keys:
        

while 1:
    newData = columns
    print('Введите тип товара:')
    tpe = input()
    print('Введите бренд товара:')
    brand = input()
    print('Введите количество товара:')
    amount = input()
    print('Введите производителя:')
    manufacturer = input()
    print('Введите цену:')
    price = input()
    print('Введите размер:')
    size = input()
    addToBase(database, tpe, brand, amount, manufacturer, price, size)
    print(database)