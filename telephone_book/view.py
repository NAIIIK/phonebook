def select_op():
    op = int(input('Выберите действие:\n1. Добавить контакт\n2. Удалить контакт\n'
                   '3. Изменить контакт\n4. Показать контакт\n5. Посмотреть все контакты\n6. Выход\n'))
    return op

def get_info():
    name = input('Введите имя:\n')
    number = input('Введите номер телефона:\n')
    data = name + ': ' + number
    return data

def search():
    return input('Поиск:\n')

