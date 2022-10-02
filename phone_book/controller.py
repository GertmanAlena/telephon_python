import export
import ui
import add_del
import create
import change
import logger
import import_file


def buttun_click():
    while True:

        var = ui.menu()
        if var == 1:
            create.show_contact()
        elif var == 2:
            create.search_contact()
        elif var == 3:
            Phone_Book = add_del.add_contact()
            add_del.create_file(Phone_Book)
            print('Данные внесены')
        elif var == 4:
            search_contact_list = create.search_contact()
            add_del.del_contact(search_contact_list)
        elif var == 5:
            create.clear_oll()
        elif var == 6:
            contact_change = create.search_contact()
            change.change_cont(contact_change)
        elif var == 7:
            export.expotr_data()
        elif var == 8:
            import_file.import_csv()
        elif var == 0:
            logger.data_exit()
            print("\033[43m {}\033[0m".format("Пока!!"))
            break
