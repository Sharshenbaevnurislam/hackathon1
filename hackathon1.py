import random 
import json

FILE_PATH = '/home/nurislam/Desktop/ev_25/hackathon/spisok.json'
ID_FILE_PATH ='/home/nurislam/Desktop/ev_25/hackathon/id.txt'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data,file)

def list_of_products():
    data = get_data()
    return f'Список товаров: {data}'

def retriev_product():
    data = get_data()
    try:
        id = int(input('Введиет id продукта: '))
        product = list(filter(lambda x: id == x['id'], data))
        return product[0]
    except:
        return 'Неверный id'

def get_id():
    with open(ID_FILE_PATH, 'r') as file:
        id = int(file.read())
        id += 1
    with open(ID_FILE_PATH, 'w') as file:
        file.write(str(id))
    return id
def creat_product():
    data = get_data()
    try:
        product = {
        'id': get_id(),
        'brand': input('Введите бренд товара: '),
        'model': input('Введите модель товара: '),
        'year_of_issue': input('Введите дату выхода товара: '),
        'description': input('Введите описание товара: '),
        'price': float(input('Введите цену товара: '))
    }
    except:
        return 'Неверные данные'

    data.append(product)
    save_data(data)
    return {'msg': 'Создан новый товар'}

def update_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x ['id'] == id, data))[0]
        print(f'Товар для обновления: {product ["model"]}')
    except:
        return 'Неверный id'

    index = data.index(product)
    choice = input('Что вы хотите изменить?(1-brand, 2-model, 3-year_of_issue, 4-description, 5-price ')
    if choice.strip() == '1':
        data[index]['brand'] = input('Введите новое название брендa: ')
    elif choice.strip() == '2':
        data[index]['model'] = input('Ввкдите новое название модели: ')
    elif choice.strip() == '3':
        data[index]['year_of_issue'] = input('Введите новую дату выхода товара: ')
    elif choice.strip() == '4':
        data[index] ['decription'] = input('Введите новое описание товapa: ')
    elif choice.strip() == '5':
        try:
            data[index] ['price'] = float(input('Введите новую цену товара: '))
        except:
            return 'Неверное значение для цены'
    else:
        return 'Неверное значение для обновления'

    save_data(data)
    return ' Товар обновлен'

def delete_product():
    data = get_data()
    try:
        id = int(input('Введиде id продукта: '))
        product = list(filter(lambda x: x ['id'] == id, data))[0]
        print(f'Товар для удаление {product ["model"]}')
    except:
        return 'Невреный id'

    choice = input('Удалить ли именно этот товар(yes/no?')
    if choice.lower().strip() != 'yes':
        return 'Товар не удален'
    data.remove(product)
    save_data(data)
    return ' Товар удален'

