import mariadb
import sys


class TshirtProduct:
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


    try:
        cur.execute('USE test IF EXISTS;')
    except mariadb.Error as e:
        print(f'Не получилось использовать БД {e}')

    try:
        cur.execute('CREATE TABLE IF NOT EXISTS tshirt('
                    'sku MEDIUMINT NOT NULL AUTO_INCREMENT, '
                    'price FLOAT, '
                    'name VARCHAR(255), '
                    'quantity MEDIUMINT, '
                    'brand VARCHAR(255), '
                    'size MEDIUMINT NOT NULL, '
                    'colour VARCHAR(255)'
                    ');')
    except mariadb.Error as e:
        print(f'Не создал таблицу{e}')

    def addToBase(table, data, cur):
        try:
            cur.execute(f'INSERT INTO {table} VALUES ({data});')
        except mariadb.Error as e:
            print(f'INSERT не удался{e}')

    def showStats(targetColumn, table, cur):
        try:
            cur.execute(f'SELECT {targetColumn}, COUNT({targetColumn}) '
                        f'FROM {table} GROUP BY {targetColumn} HAVING COUNT({targetColumn}) > 1;')
        except mariadb.Error as e:
            print(f'Не удалось выести статистику по производителю {e}')

    def getData(column, table, cur):
        try:
            print(cur.execute(f'SELECT {column} FROM {table}'))
        except mariadb.Error as e:
            print(f'Не удалось вернуть результат запроса {e}')

    while 1:
        newData = []
        print('Введите цену:')
        newData.append(float(input()))
        print('Введите наименование товара:')
        newData.append(input())
        print('Введите количество:')
        newData.append(int(input()))
        print('Введите бренд товара:')
        newData.append(input())
        print('Введите размер:')
        newData.append(int(input()))
        print('Введите цвет:')
        addToBase('tshirt', newData, cur)
        showStats('manufacturer', 'tshirt', cur)
        getData('price', 245, cur)
