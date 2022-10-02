import json
import csv
import logger

def expotr_data():
    with open('contact.json', 'r') as file:
        dict_Phone_Book = json.load(file)
    with open('contact.csv', mode='w', encoding='utf-8', newline='') as csvfile:
        file_wr = csv.writer(csvfile, delimiter=":", lineterminator="\r")
        file_wr.writerow(["Фамилия\t", "Имя\t", "Телефон\t"])

        for i in dict_Phone_Book:
            file_wr.writerow([i["surname"], i["name"], i["phon_number"]])
            
    logger.data_export()
    print(f'\033[5m\033[4m\033[4m Экспорт завершен успешно.\033[0m')

    