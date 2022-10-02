import json
import test


def change_cont(contact_change):
    """функция замены принимает найденный контакт"""
    contact_change = test.correct_list(contact_change)
    with open('contact.json', 'r') as file:
        dict_Phone_Book = json.load(file)
    for i in range(len(dict_Phone_Book)):
        if dict_Phone_Book[i] == contact_change[0]:  # если совпали фамилии
            what_search = test.number_change()  # что меняем
            if what_search == 1:
                dict_Phone_Book.pop(i)  # удаляем фамилию старую
                # вводим новую
                contact_change[0]["surname"] = test.correct_surname()
                dict_Phone_Book.append(contact_change[0])
            if what_search == 2:
                dict_Phone_Book.pop(i)  # удаляем старое
                # вводим новое
                contact_change[0]["name"] = test.correct_name()
                dict_Phone_Book.append(contact_change[0])
            if what_search == 3:
                dict_Phone_Book.pop(i)  # удаляем старый
                # вводим новый
                contact_change[0]["phon_number"] = test.correct_tel_number()
                dict_Phone_Book.append(contact_change[0])
    with open('contact.json', 'w', encoding="utf-8") as file:
        json.dump(dict_Phone_Book, file, indent=2)
    print('\033[30m\033[42m\033[4m {}\033[0m'.format('Контакт ИЗМЕНЁН'))
    print('-'*50)
