import os
import Utils
from Singleton import Singleton


class DBRequests(metaclass=Singleton):
    """A class used to process requests to a database

    Attributes
    ----------
    __db_name : str
        The string is the name of the database (located at the root
        of the project directory)
    __db_cols : list
       List consisting of database column names

    Methods
    -------
    get_max_idx()
        Gets the maximum index in the database
    get_last_note()
        Returns a list of the elements of the last note in the database
    is_suit_elem(elem)
        Checks if this element matches database columns
    add_note(elem)
        Adds a note to the database
    del_note(idx: str)
        Deleting a note with the specified index from the database
        If the index is not in the database, then nothing happens
    get_note(idx: str)
        Getting a note with the specified index from the database
        If not found [] was returned

    Raises
    ------
    ValueError
        If incorrect arguments were given when the element was expected
        to match the attributes of the database element
    ValueError
        If the element at the specified index does not exist
    """

    def __init__(self, db_name: str, db_cols: list):
        """
        Parameters
        ----------
        db_name : str
            The string is the name of the database (located at the root
            of the project directory)
        db_cols : list
            List consisting of database column names
        """
        self.__db_name = db_name
        self.__db_cols = db_cols

        # Checks if a file with the given name exists and creates
        # it if not
        if self.__db_name not in os.listdir():
            with open(self.__db_name, 'w') as db_file:
                pass

        with open(self.__db_name, 'r+') as db_file:
            # We add '\n' to the end of self.__db_cols because
            # when we add note to database we also add '\n' to the end
            if db_file.readline() != ';'.join(self.__db_cols) + '\n':
                db_file.write(';'.join(self.__db_cols) + '\n')

    @property
    def db_name(self):
        return self.__db_name

    @property
    def db_cols(self):
        return self.__db_cols

    def get_max_idx(self):
        """Gets the maximum index in the database"""

        with open(self.__db_name, 'r') as db_file:
            max_idx = 0
            for note in db_file:
                idx_pos_cols = self.__db_cols.index('idx')
                first_attribute = note[:-1].split(';')[idx_pos_cols]
                if first_attribute != 'idx' and \
                        int(first_attribute) > max_idx:
                    max_idx = int(first_attribute)
        return max_idx

    def get_last_note(self):
        """Gets last note in database

        Returns a list of the elements of the last note in the database

        Returns
        -------
        list
            Elements of characteristic of element in database
        """

        with open(self.db_name, 'r') as db_file:
            for note in db_file:
                pass
        # We separate the last character because it's '\n'
        cor_note = []
        for elem in note[:-1].split(';'):
            if elem[0] == '{' and elem[-1] == '}':
                cor_note.append(Utils.str2dict(elem))
            elif elem.isdigit():
                cor_note.append(int(elem))
            else:
                cor_note.append(elem)
        return cor_note

    def is_suit_elem(self, elem):
        """Checks if this element matches database columns

        Checks that all attributes of an element are database columns

        Parameters
        ----------
        elem
            The element to be added to the database

        Returns
        -------
        bool
            Result of comparing element and database attribute types
        """
        # t = Utils.get_clear_attr_names(elem)
        return Utils.get_clear_attr_names(elem) == self.__db_cols

    def add_note(self, elem):
        """Adds note to database

        Adds a note with the element characteristics to the end of
        the database

        Parameters
        ----------
        elem
            The element to be added to the database

        Raises
        ------
        ValueError
            If incorrect arguments were given when the element was
            expected to match the attributes of the database element
        """

        if not self.is_suit_elem(elem):
            raise ValueError('The element\'s attributes should look '
                             'like database columns')
        with open(self.__db_name, 'a') as db_file:
            last_note = self.get_last_note()
            if elem.idx is None:
                last_idx = str(self.get_max_idx() + 1)
                # The element is assumed to have an idx attribute
                elem.idx = last_idx
            db_file.write(';'.join(map(str, elem.__dict__.values())) + '\n')

    def __add_note(self, attribute_values: list, idx=None):
        with open(self.__db_name, 'a') as db_file:
            if idx is None:
                max_idx = self.get_max_idx()
                db_file.write(';'.join(map(str, attribute_values + [max_idx])) + '\n')
            else:
                db_file.write(';'.join(map(str, attribute_values)) + '\n')

    def del_note(self, idx: str):
        """Deleting a note from the database

        Deleting a note with the specified index from the database If
        the index is not in the database, then nothing happens

        Parameters
        ----------
        idx : str
            The index to be removed from the database
        """
        # If the index is not in the database, then nothing happened
        with open(self.__db_name, 'r') as db_file:
            idx_pos_cols = self.__db_cols.index('idx')
            all_needed_notes = [note.split(';') for note in db_file
                                if note[:-1].split(';')[idx_pos_cols] != idx]
        with open(self.__db_name, 'w') as db_file:
            for note in all_needed_notes:
                db_file.write(';'.join(note))

    def get_note(self, idx: str):
        """Gets note from database

        Gets a note with the specified index from the database
        If not found [] was returned

        Parameters
        ----------
        idx : str
            The index to get from the database

        Returns
        -------
        list
            Elements of characteristic of elem in database or [] if
            note was not found
        """
        with open(self.__db_name, 'r') as db_file:
            note = db_file.readline()
            not_eof = True
            idx_pos_cols = self.__db_cols.index('idx')
            while not_eof and note[:-1].split(';')[idx_pos_cols] != idx:
                note = db_file.readline()
                if not note:
                    not_eof = False
        if not_eof:
            # We separate the last character because it's '\n'
            cor_note = []
            for elem in note[:-1].split(';'):
                if elem[0] == '{' and elem[-1] == '}':
                    cor_note.append(Utils.str2dict(elem))
                elif elem.isdigit():
                    cor_note.append(int(elem))
                else:
                    try:
                        is_float = float(elem)
                        cor_note.append(is_float)
                    except:
                        cor_note.append(elem)
            return cor_note
        else:
            return []

    def update_attribute(self, idx: str, attribute: str, value):
        """Sets the specified value to an element attribute

        Parameters
        ----------
        idx : str
            Element index
        attribute : str
            The attribute of the element to be changed
        value
            Some new value

        Raises
        ------
        ValueError
            If the element at the specified index does not exist
        """
        if attribute == 'idx':
            raise ValueError('Index change not allowed')
        if attribute not in self.__db_cols:
            raise ValueError('Attribute not found')
        idx = str(idx)
        note = self.get_note(idx)
        if note:
            self.del_note(idx)
            note[self.__db_cols.index(attribute)] = str(value)
            self.__add_note(note, idx=idx)
        else:
            raise ValueError('The element at the specified index does'
                             ' not exist')

    def get_all(self):
        with open(self.__db_name, 'r') as db_file:
            notes = db_file.readlines()
        return [note[:-1].split(';') for note in notes[1:]]
