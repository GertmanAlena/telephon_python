import json
import test
import logger

def show_contact():
    """Функция вывода всех контактов"""
    with open('contact.json', 'r') as file:
        dict_Phone_Book = json.load(file)
    if len(dict_Phone_Book) == 0:
       print('\033[43m\033[1m {} \033[0m'.format(
           'Ваш справочник пока еще пустой!'))
    else:
        for num, i in enumerate(dict_Phone_Book):
            print(f'\033[44m Контакт № {num+1}\033[0m\n'
                  f'Фамилия: {i["surname"]}\n'
                  f'Имя: {i["name"]}\n'
                  f'Телефон: {i["phon_number"]}\n')

def search_contact():
    """Функция поиска контакта"""
    with open('contact.json', 'r') as file:
        dict_Phone_Book = json.load(file)
    if len(dict_Phone_Book) == 0:
       print('\033[43m\033[1m {} \033[0m'.format(
           'Ваш справочник пока еще пустой!'))
    else:
        search_contact_list = []
        if len(dict_Phone_Book) != 0:
            how_search = test.number_two()
            if how_search == 1:
                contact = test.correct_surname()
                for i in dict_Phone_Book:
                    if i["surname"] == contact:
                        search_contact_list.append(i)
                if search_contact_list == []:  # если пусто
                    print("\033[31m {}\033[0m" .format('Контакт не найден!'))
                else:
                    print("\033[31m {}\033[0m" .format('ВОТ ЧТО НАШЁЛ!'))
                    for num, i in enumerate(search_contact_list):
                        print(f'\033[15m\033[15m\033[15m Контакт № {num+1}\033[0m\n'
                            f'Фамилия: {i["surname"]}\n'
                            f'Имя: {i["name"]}\n'
                            f'Телефон: {i["phon_number"]}\n')
                logger.data_search_contact_name(search_contact_list)
                return search_contact_list

            if how_search == 2:
                contact = test.correct_name()
                for i in dict_Phone_Book:
                    if i["name"] == contact:
                        search_contact_list.append(i)
                if search_contact_list == []:
                    print("\033[31m {}\033[0m" .format('Контакт не найден!'))
                else:
                    print("\033[31m {}\033[0m" .format('ВОТ ЧТО НАШЁЛ!'))
                    for num, i in enumerate(search_contact_list):
                        print(f'\033[15m\033[15m\033[15m Контакт № {num+1}\033[0m\n'
                            f'Фамилия: {i["surname"]}\n'
                            f'Имя: {i["name"]}\n'
                            f'Телефон: {i["phon_number"]}\n')
                logger.data_search_contact_name(search_contact_list)
                return search_contact_list

            if how_search == 3:
                contact = test.correct_tel_number()
                for i in dict_Phone_Book:
                    if i["phon_number"] == contact:
                        search_contact_list.append(i)
                if search_contact_list == []:
                    print("\033[31m {}\033[0m" .format('Контакт не найден!'))
                else:
                    print("\033[31m {}\033[0m" .format('ВОТ ЧТО НАШЁЛ!'))
                    for num, i in enumerate(search_contact_list):
                        print(f'\033[15m\033[15m\033[15m Контакт № {num+1}\033[0m\n'
                            f'Фамилия: {i["surname"]}\n'
                            f'Имя: {i["name"]}\n'
                            f'Телефон: {i["phon_number"]}\n')
                logger.data_search_contact_name(search_contact_list)
                return search_contact_list

def clear_oll():
    """Функция удаления всех контактов"""
    try:
        with open('contact.json', 'r') as file:
            dict_Phone_Book = json.load(file)
    except:
        dict_Phone_Book = []

    dict_Phone_Book.clear()
    logger.data_clear_oll()
    print('\033[30m\033[42m\033[4m {}\033[0m'.format(
        'Список контактов очищен'))
    with open('contact.json', 'w', encoding="utf-8") as file:
        json.dump(dict_Phone_Book, file, indent=2)
