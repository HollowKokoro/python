a = 'type'
b = 'brand'
c = 'amount'
database = []


def addToBase(db, tpe, brand, amount):
    good = {'Type': tpe, 'Brand': brand, 'Amount': amount}
    db.append(good)

while 1:
    print('Введите тип товара:')
    tpe = input()
    print('Введите бренд товара:')
    brand = input()
    print('Введите количество товара:')
    amount = input()
    addToBase(database, tpe, brand, amount)
    print(database)