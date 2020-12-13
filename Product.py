import mariadb
import sys


class Product:
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

    keys = ['price', 'name', 'quantity', 'brand']

    try:
        cur.execute('USE test IF EXISTS;')
    except mariadb.Error as e:
        print(f'Не получилось использовать БД {e}')

    try:
        cur.execute('CREATE TABLE IF NOT EXISTS product('
                    'sku MEDIUMINT NOT NULL AUTO_INCREMENT, '
                    'price FLOAT, '
                    'name VARCHAR(255), '
                    'quantity MEDIUMINT, '
                    'brand VARCHAR(255)'
                    ');')
    except mariadb.Error as e:
        print(f'Не создал таблицу{e}')

    while 1:
        newData = []
        print('Введите цену:')
        newData.append(float(input()))
        print('Введите наименование товара:')
        newData.append(input())
        print('Введите количество:')
        newData.append(int(input()))
        print('Введите бренд товара')
        newData.append(input())
        try:
            cur.execute('INSERT INTO product VALUES (newData);')
        except mariadb.Error as e:
            print(f'INSERT не удался{e}')

        try:
            cur.execute('SELECT manufacturer, COUNT(manufacturer) '
                        'FROM product GROUP BY manufacturer HAVING COUNT(manufacturer) > 1;')
        except mariadb.Error as e:
            print(f'Не удалось выести статистику по производителю')
