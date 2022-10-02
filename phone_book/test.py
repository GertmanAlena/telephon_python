import logger

def number():
    """Проверка на ввод числа"""
    while True:
        try:
            num = int(input("Введите действие, которое Вы хотите сделать:- > "))
            return num
        except ValueError:
            logger.data_num("Не верный ввод числа в выборе дейсвия.")
            print("\033[33m {}\033[0m".format(
                "Вы вводите что-то не так, попробуйте снова."))


def number_two():
    """Проверка на ввод числа"""
    while True:
        try:
            num = int(input(
                "Введите по какому параметру искать:\n1. По фамилии\n2. По имени\n3. По номеру телефона\n"))
            if num > 0 and num <= 3:
                return num
            else:
                print("\033[33m {}\033[0m".format(
                    "Вы вводите что-то не так, попробуйте снова."))
        except ValueError:
            logger.data_num("Не верный ввод числа.")
            print("\033[33m {}\033[0m".format(
                "Вы вводите что-то не так, попробуйте снова."))


def number_change():
    """Проверка на ввод числа"""
    while True:
        try:
            num = int(input(
                "Введите что нужно изменить:\n1. Фамилию\n2. Имя\n3. Телефон\n"))
            if num > 0 and num <= 3:
                return num
            else:
                print("\033[33m {}\033[0m".format(
                    "Вы вводите что-то не так, попробуйте снова."))
        except ValueError:
            logger.data_num("Не верный ввод числа.")
            print("\033[33m {}\033[0m".format(
                "Вы вводите что-то не так, попробуйте снова."))

def correct_name():
    """Проверка правильности ввода имени"""
    while True:
        name = input("Введите имя-> ")
        if name.isalpha() and len(name) < 10:
            return name.capitalize()
        else:
            logger.data_name("Введено не корректное имя или фамилия.")
            print("\033[31m {}\033[0m" .format("Введены не корректные данные"))
        # name = input("Введите имя-> ")


def correct_surname():
    """Проверка правильности ввода фамилии"""
    while True:
        name = input("Введите фамилию-> ")
        if name.isalpha() and len(name) < 10:
            return name.capitalize()
        else:
            logger.data_name("Введено не корректное имя или фамилия.")
            print("\033[31m {}\033[0m" .format("Введены не корректные данные"))
        name = input("Введите фамилию-> ")


def correct_tel_number():
    while True:
        number = input("Введите номер телефона в фомате +номер без пробелов: ")
        # if number[0] == '+' and number[1:].isdigit() and len(number) <= 13:
        if number[0] == '+' or number[1:].isdigit() and len(number) <= 13:
            return number
        else:
            print("\033[31m {}\033[0m" .format(
                "Номер телефона введён не корректно. Попробуйте ещё раз!!"))
        number = input("Введите номер телефона в фомате +номер без пробелов: ")
def correct_list(contact_change):
    if len(contact_change) > 1:
        num = int(input("какой контакт нужно изменить?-> "))
        contact_change2 = []
        contact_change2.append(contact_change[num-1])
        return contact_change2
    else: return contact_change
        