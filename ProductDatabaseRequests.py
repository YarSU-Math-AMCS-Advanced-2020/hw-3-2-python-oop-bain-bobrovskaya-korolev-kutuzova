import os
from Singleton import Singleton


# TODO: Create connection with product

class ProductDatabaseRequests(metaclass=Singleton):
    """
    A class used to process requests to a database containing
    information about products

    ...

    Attributes
    ----------
    __db_name : str
        The string is a name of the database containing products
        (located at the root of the project directory)
    __db_column_names : str
        A string consisting of the index and characteristics of the
        product separated by ';'.
        Example: "id;seller;name;price;description;characteristics;
        category;total_quantity;rating;total_assessments"

    Methods
    -------
    get_last_note()
        Returns a list of the elements of the last note in the database
    is_all_elements_product(*elements)
        Check that all elements sent are part of the characteristics
        of the product (which is contained in the database)
    add_note(*product)
        Add a note with the product characteristics that were given to
        the end of the database
    del_note(idx: str)
        Deleting a note with the specified index from the database
        If the index is not in the database, then nothing happened
    get_note(self, idx: str)
        Getting a note with the specified index from the database
        If not found [] was returned

    Raises
    ------
    ValueError
        If wrong arguments were given when product's characteristics
        had been expecting
    """
    def __init__(self, db_name='ProductDatabase.txt'):
        """
        Parameters
        ----------
        db_name : str
            The string is a name of the database containing products
            (located at the root of the project directory)
            (default is 'ProductDatabase.txt')
        """
        self.__db_name = db_name
        self.__db_column_names = "id;seller;name;price;description;" \
                                 "characteristics;category;total_quantity;" \
                                 "rating;total_assessments"
        if self.__db_name not in os.listdir():
            with open(self.__db_name, 'w') as db_file:
                pass
        with open(self.__db_name, 'r+') as db_file:
            # We add '\n' to the end of self.__db_column_names because
            # when we add note to database we also add '\n' to the end
            if db_file.readline() != self.__db_column_names + '\n':
                db_file.write(self.__db_column_names + '\n')

    @property
    def db_name(self):
        return self.__db_name

    @property
    def db_column_names(self):
        return self.__db_column_names

    def get_last_note(self):
        """Get last note in database

        Returns a list of the elements of the last note in the database

        Returns
        -------
        list
            Elements of characteristic of element in database
        """
        with open(self.db_name, 'r') as db_file:
            for note in db_file:
                pass
            # We separate last symbol because is '\n'
            return note[:-1].split(';')

    def is_all_elements_product(self, *elements):
        """Check that all elements sent are part of the product

        Check that all elements sent are part of the characteristics
        of the product (which is contained in the database)

        Parameters
        ----------
        *elements
            All parts product characteristics

        Returns
        -------
        bool
            Result of type comparing element in *elements with type of
            product characteristics
        """
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

    def add_note(self, *product):
        """Add note to database

        Add a note with the product characteristics that were given to
        the end of the database

        Parameters
        ----------
        *product
            All parts of product characteristic

        Raises
        ------
        ValueError
            If wrong arguments were given when product's characteristics
            had been expecting
        """
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
        """Delete note from database

        Deleting a note with the specified index from the database
        If the index is not in the database, then nothing happened

        Parameters
        ----------
        idx : int
            Index which should be deleted from database
        """
        # If the index is not in the database, then nothing happened
        with open(self.__db_name, 'r') as db_file:
            all_needed_notes = [note.split(';') for note in db_file
                                if note.split(';')[0] != idx]
        with open(self.__db_name, 'w') as db_file:
            for note in all_needed_notes:
                db_file.write(';'.join(note))

    def get_note(self, idx: str):
        """Get note from database

        Getting a note with the specified index from the database
        If not found [] was returned

        Parameters
        ----------
        idx : int
            Index which should be deleted from database

        Returns
        -------
        list
            Elements of characteristic of element in database or [] if
            note was not found
        """
        with open(self.__db_name, 'r') as db_file:
            note = db_file.readline()
            not_eof = True
            while note.split(';')[0] != idx and not_eof:
                note = db_file.readline()
                if not note:
                    not_eof = False
        if not_eof:
            # We separate last symbol because is '\n'
            return note[:-1].split(';')
        else:
            return []
