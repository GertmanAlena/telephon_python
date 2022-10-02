import csv
import json
import logger
def import_csv():
    result = []
    with open("contact.csv", encoding='utf-8') as file:
        file_contact_csv = csv.reader(file, delimiter = ":")
        for i in file_contact_csv:
            dict_Phone_Book = {}
            dict_Phone_Book["surname"] = i[0]
            dict_Phone_Book["name"] = i[1]
            dict_Phone_Book["phon_number"] = i[2]
            
            result.append(dict_Phone_Book)
   
    with open('contact.json', 'w') as file:
        json.dump(result, file, indent=2)
    logger.data_import()
    print(f'\033[30m\033[42m\033[4m Импорт завершен успешно. '
          f'Контакты импортированы. \033[0m')