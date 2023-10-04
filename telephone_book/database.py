from view import *

def add_info(arg):
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(f'{arg}\n')


def search_info(arg):
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        res = []
        count = 1
        for i in range(len(lst)):
            if arg.lower() in lst[i].lower():
                res.append(lst[i])
                print(f'{count}. {lst[i]}')
                count += 1
        return res


def book_view():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        return file.read()


def delete_info(arg):
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        lst = file.readlines()
        counter = 1
        for i in range(len(lst)):
            if arg.lower() in lst[i].lower():
                lst[i] = str(counter) + '. ' + lst[i]
                print(lst[i])
                counter += 1
        if counter == 1:
            print('Похожих контактов не существует')
            return lst
        option = input('Какой контакт хотите удалить?\n')
        for i in lst:
            if option in i[0]:
                lst.pop(lst.index(i))
        file.seek(0)
        file.truncate()
        for i in range(len(lst)):
            if lst[i][2] == ' ':
                file.writelines(lst[i][3:])
            else:
                file.writelines(lst[i])

def change_info(arg):
    with open('phonebook.txt', 'r+', encoding='utf-8') as file:
        lst = file.readlines()
        counter = 1
        for i in range(len(lst)):
            if arg.lower() in lst[i].lower():
                lst[i] = str(counter) + '. ' + lst[i]
                print(lst[i])
                counter += 1
        if counter == 1:
            print('Похожих контактов не существует')
            return lst
        option = input('Какой контакт хотите изменить?\n')
        for i in lst:
            if option in i[0]:
                lst[lst.index(i)] = f'{get_info()}\n'
        file.seek(0)
        file.truncate()
        for i in range(len(lst)):
            if lst[i][2] == ' ':
                file.writelines(lst[i][3:])
            else:
                file.writelines(lst[i])
