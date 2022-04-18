import os
from DatabaseRequests import DatabaseRequests


# TODO: documentations strings
# TODO: Create connection with product

class ProductDatabaseRequests(DatabaseRequests):
    __instance = None

    def __new__(cls, db_name='ProductDatabase.txt'):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, db_name='ProductDatabase.txt'):
        self.__db_name = db_name
        self.__db_column_names = "id;seller;name;price;description;" \
                                 "characteristics;category;total_quantity;" \
                                 "rating;total_assessments"
        if self.__db_name not in os.listdir():
            with open(self.__db_name, 'w') as db_file:
                pass
        with open(self.__db_name, 'r+') as db_file:
            if db_file.readline() != self.__db_column_names + '\n':
                db_file.write(self.__db_column_names + '\n')

    @property
    def db_name(self):
        return self.__db_name

    @property
    def db_column_names(self):
        return self.__db_column_names

    def get_last_note(self):
        with open(self.db_name, 'r') as db_file:
            for note in db_file:
                pass
            return note[:-1].split(';')

    def is_all_elements_product(self, *elements):
        if len(*elements) == len(self.__db_column_names.split(';')) - 1:
            if type(elements[0][0]) == str and \
                    type(elements[0][1]) == str and \
                    type(elements[0][2]) == int and \
                    type(elements[0][3]) == str and \
                    type(elements[0][4]) == dict and \
                    type(elements[0][5]) == str and \
                    type(elements[0][6]) == int and \
                    type(elements[0][7]) == float and \
                    type(elements[0][8]) == int:
                return True
        return False

    # Should be called only in Product.__init__()
    def add_note(self, *product):
        if not self.is_all_elements_product(product):
            raise ValueError("The product should look like this: "
                             "seller: str, name: str, "
                             "price: int, description: str, "
                             "characteristics: dict, category: str, "
                             "total_quantity: int, rating: float, "
                             "total_assessments: int")
        with open(self.__db_name, 'a') as db_file:
            last_note = self.get_last_note()
            last_idx = 0
            if last_note != self.db_column_names.split(';'):
                last_idx = int(last_note[0]) + 1
            db_file.write(str(last_idx) + ";" + ";".join(
                                   [str(product_part) for product_part in
                                    product]) + '\n')

    def del_note(self, idx: str):
        # If the index is not in the database, then nothing happened
        with open(self.__db_name, 'r') as db_file:
            all_needed_notes = [note.split(';') for note in db_file
                                if note.split(';')[0] != idx]
        with open(self.__db_name, 'w') as db_file:
            for note in all_needed_notes:
                db_file.write(';'.join(note))

    def get_note(self, idx: str):
        with open(self.__db_name, 'r') as db_file:
            note = db_file.readline()
            not_eof = True
            while note.split(';')[0] != idx and not_eof:
                note = db_file.readline()
                if not note:
                    not_eof = False
        if not_eof:
            return note[:-1].split(';')
        else:
            return []
