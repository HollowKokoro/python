a = 'type'
b = 'brand'
c = 'amount'
d = 'manufacturer'
e = 'price'
f = 'size'
database = []


def addToBase(db, tpe, brand, amount, manufacturer, price, size):
    good = {a: tpe, b: brand, c: amount, d: manufacturer, e: price, f: size}
    db.append(good)

while 1:
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
