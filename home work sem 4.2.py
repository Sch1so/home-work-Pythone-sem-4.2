# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.


from pathlib import Path


FILE_PATH = Path('kont.txt')
print(FILE_PATH)


def add_contakt():
    with open(FILE_PATH, 'a', encoding='utf8') as file:
        info = input('Введите данные: ')
        file.write(f'\n{info}')

def show_contakt():
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        kont = file.readlines()
        for line in kont:
            print(line)

def find_contakt():
    list_1=[]
    serch=input('Ведите искомое: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contakt in file:
            if serch in contakt:
                list_1.append(contakt)
        print(*[line for line in list_1])

def del_contakt():
    list_1 = []
    list_del = []
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contakt in file:
            list_1.append(contakt)

    for i in range(len(list_1)):
        print(i, list_1[i])

    cont = int(input('Введите индекс контакта для удаления -> '))
    if cont < len(list_1):
        for i in range(len(list_1)):
            if i != cont:
                list_del.append(list_1[i])
            else:
                print(list_1[i], 'Контанк был удален')
        with open(FILE_PATH, 'w', encoding='utf8') as file:
            for new_cont in list_del:
                file.write(new_cont)
    if cont < 0:
        print('Введен отрицательный индекс будте внимательны')
    else:
        print('Введен слишком большой индекс будте внимательны')
        
  
def changes_contakt():
    list_changes = []
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contakt in file:
            list_changes.append(contakt)

    for i in range(len(list_changes)):
        print(i, list_changes[i])

    changes = int(input('Введите индекс контакта для изменения -> '))
    if changes < len(list_changes):
        for i in range(len(list_changes)):
            if i == changes:
                zam = input('Введите данные изменяемого контакта -> ')
                list_changes[i] = (f'{zam}\n')
        with open(FILE_PATH, 'w', encoding='utf8') as file:
            for new_cont in list_changes:
                file.write(new_cont)
    if changes < 0:
        print('Введен отрицательный индекс будте внимательны')
    if changes > len(list_changes):
        print('Введен слишком большой индекс будте внимательны')

def chouse():
    flag = True
    print('1 Сохранить контакт')
    print('2 Показать контакты')
    print('3 Поиск контактов')
    print('4 Удалить контакт')
    print('5 Изменить контакт')
    print('6 Выход')
    while flag:
        n = input('Выберите действие: ')
        match n:
            case '1':
                add_contakt()
            case '2':
                show_contakt()
            case '3':
                find_contakt()
            case '4':
                del_contakt()
            case '5':
                changes_contakt()
            case '6':
                flag = False
            
chouse()
