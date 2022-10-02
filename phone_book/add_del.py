import logger
import json
import test


def add_contact():
    """
    добавляем контакт и сохраняем в dict
    """
    Phone_Book = {}
    Phone_Book["name"] = test.correct_name()
    Phone_Book["surname"] = test.correct_surname()
    Phone_Book["phon_number"] = test.correct_tel_number()
    return Phone_Book


def create_file(Phone_Book):
    
    """Функция добавления контакта"""
    try:
        with open('contact.json', 'r') as file:
            dict_Phone_Book = json.load(file)
    except:
        dict_Phone_Book = []

    dict_Phone_Book.append(Phone_Book)
    
    with open('contact.json', 'w', encoding="utf-8") as file:
        json.dump(dict_Phone_Book, file, indent=2, ensure_ascii=False)
    print('\033[30m\033[42m\033[4m {}\033[0m'.format('Контакт добавлен'))
    logger.data_create_file(Phone_Book)
    print('-'*50)

def del_contact(search_contact_list):
    print("search_contact_lis сначала", search_contact_list)
    print(type(search_contact_list))
    """
    удаление контакта
    """
    if len(search_contact_list) > 1:
        num = int(input("какой контакт удаляем?-> "))
        search_contact_list2 = []
        search_contact_list2.append(search_contact_list[num-1])
        print("search_contact_lis потом",search_contact_list2)
        print(type(search_contact_list2))
        with open('contact.json', 'r') as file:
            dict_Phone_Book = json.load(file)
        for i in range(len(dict_Phone_Book)-1):
                    
            if dict_Phone_Book[i] == search_contact_list[0]:
                dict_Phone_Book.pop(i)

        with open('contact.json', 'w', encoding="utf-8") as file:
            json.dump(dict_Phone_Book, file, indent=2)
        print('\033[30m\033[42m\033[4m {}\033[0m'.format('Контакт удален'))
        logger.data_del_contact(search_contact_list)
        print('-'*50)

    else:
        with open('contact.json', 'r') as file:
            dict_Phone_Book = json.load(file)
        for i in range(len(dict_Phone_Book)):
                    
            if dict_Phone_Book[i] == search_contact_list[0]:
                dict_Phone_Book.pop(i)

        with open('contact.json', 'w', encoding="utf-8") as file:
            json.dump(dict_Phone_Book, file, indent=2)
        print('\033[30m\033[42m\033[4m {}\033[0m'.format('Контакт удален'))
        logger.data_del_contact(search_contact_list)
        print('-'*50)
