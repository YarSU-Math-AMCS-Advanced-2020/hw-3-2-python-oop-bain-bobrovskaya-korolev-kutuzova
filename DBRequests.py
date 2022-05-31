import os
import Utils
from Singleton import Singleton


class DBRequests(metaclass=Singleton):
    """A class used to process requests to a database

    Attributes
    ----------
    db_name : str
        The string is the name of the database (located at the root
        of the project directory)
    db_cols : list
       List consisting of database column names. Must include 'idx' - unique identifier

    Methods
    -------
    attribute_index(self, attribute_name: str) -> int
        Get index (column number) of attribute in database
    is_there_by(self, attribute_name: str, attribute_value: str) -> bool
        Check if there is an element with <attribute_name> equal to attribute_value
    is_there(self, idx: str) -> bool
        Equivalent to is_there_by('idx', idx)
    unique(self, attribute_name: str) -> list
        Find values that attribute takes across the database
    is_suit_elem(self, elem) -> bool
        Check if elem attributes correspond to database attributes
    add_note(self, elem) -> None
        Add note to database with elem attributes
    del_note(self, idx: str) -> None
        Delete first note with <idx> = idx
    del_note_by(self, attribute_name: str, attribute_value: str) -> None
        Delete first note with <attribute_name> = attribute_value
    get_note(self, idx: str) -> list or None
        Get list of attributes of element with <idx> = idx
    get_note_by(self, attribute_name: str, attribute_value: str) -> list or None
        Get list of attributes of element with <attribute_name> = attribute_value
    update(self, elem) -> None
        Update note of object with the same <idx> attribute
    get_all_notes(self) -> list of lists
        Get list of all notes (lists of attributes for every stored object)

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
            List consisting of database column names. Must include 'idx' - unique identifier
        """
        self.db_name = db_name
        self.db_cols = db_cols

        if 'idx' not in self.db_cols:
            raise ValueError("db_cols in DBRequests must contain 'idx'")

        # Checks if a file with the given name exists and creates
        # it if not
        if self.db_name not in os.listdir():
            with open(self.db_name, 'w') as db_file:
                pass

        with open(self.db_name, 'r+') as db_file:
            # We add '\n' to the end of self.db_cols because
            # when we add note to database we also add '\n' to the end
            if db_file.readline() != ';'.join(self.db_cols) + '\n':
                db_file.write(';'.join(self.db_cols) + '\n')

    def attribute_index(self, attribute_name: str) -> int:
        """
        Get index (column number) of attribute in database
        """
        return self.db_cols.index(attribute_name)

    def is_there_by(self, attribute_name: str, attribute_value: str) -> bool:
        """
        Check if there is an element with <attribute_name> equal to attribute_value
        """
        if attribute_name not in self.db_cols:
            raise ValueError('The attribute_name must be defined')

        attribute_index = self.attribute_index(attribute_name)

        with open(self.db_name, 'r') as db_file:
            note = db_file.readline()
            while note and note[:-1].split(';')[attribute_index] != attribute_value:
                note = db_file.readline()

        return bool(note)

    def is_there(self, idx: str) -> bool:
        """
        Equivalent to is_there_by('idx', idx)
        """
        return self.is_there_by('idx', idx)

    def unique(self, attribute_name: str) -> list:
        """
        Find values that attribute takes across the database
        """
        idx = self.attribute_index(attribute_name)
        u = set()
        for note in self.get_all_notes():
            u.add(note[idx])
        return list(u)

    def is_suit_elem(self, elem) -> bool:
        """
        Check if elem attributes correspond to database attributes

        Parameters
        ----------
        elem
            The element to be added to the database

        Returns
        -------
        bool
            Result of comparing element and database attribute types
        """
        return Utils.get_clear_attr_names(elem) == self.db_cols

    def add_note(self, elem) -> None:
        """
        Add note to database with elem attributes


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
        if self.is_there_by('idx', elem.idx):
            raise ValueError('The element with this id is already in database.')

        with open(self.db_name, 'a') as db_file:
            db_file.write(';'.join(map(str, elem.__dict__.values())) + '\n')

    def del_note(self, idx: str) -> None:
        """
        Delete first note with <idx> = idx

        Equivalent to del_note_by('idx', idx)
        """
        self.del_note_by('idx', idx)

    def del_note_by(self, attribute_name: str, attribute_value: str) -> None:
        """
        Delete first note with <attribute_name> = attribute_value

        Deleting a note with the specified index from the database
        If the index is not in the database, then nothing happens
        """

        if attribute_name not in self.db_cols:
            raise ValueError('The attribute_name must be defined')

        attribute_index = self.attribute_index(attribute_name)

        with open(self.db_name, 'r') as db_file:
            all_notes = [note[:-1].split(';') for note in db_file.readlines()]
        with open(self.db_name, 'w') as db_file:
            for note in all_notes:
                if note[attribute_index] != attribute_value:
                    db_file.write(';'.join(note))
                    db_file.write('\n')

    def get_note(self, idx: str) -> list or None:
        """
        Get list of attributes of element with <idx> = idx
        """
        return self.get_note_by('idx', idx)

    def get_note_by(self, attribute_name: str, attribute_value: str) -> list or None:
        """
        Get list of attributes of element with <attribute_name> = attribute_value
        If note isn't found, returns None

        Parameters
        ----------
        attribute_name : str
        attribute_value : str

        Returns
        -------
        list
            list of attributes required to form a class instance for stored object
        or None
            if note isn't found
        """
        if attribute_name not in self.db_cols:
            raise ValueError('The attribute_name must be defined')

        attribute_index = self.attribute_index(attribute_name)

        with open(self.db_name, 'r') as db_file:
            note = db_file.readline()
            while note and note[:-1].split(';')[attribute_index] != attribute_value:
                note = db_file.readline()

        if note:
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
            return None

    def update(self, elem) -> None:
        """
        Update note of object with the same <idx> attribute

        The function finds entry in database with the same idx attribute, and updates it with ``elem``
        """
        if not self.is_suit_elem(elem):
            raise ValueError('The element\'s attributes should look '
                             'like database columns')
        if not self.is_there_by('idx', elem.idx):
            raise ValueError('The element with this idx is not present in the database')

        idx = elem.idx
        note = self.get_note(idx)
        if note:
            self.del_note(idx)
            self.add_note(elem)

    def get_all_notes(self) -> list:
        """
        Get list of all notes (lists of attributes for every stored object)
        """
        with open(self.db_name, 'r') as db_file:
            notes = db_file.readlines()
        return [note[:-1].split(';') for note in notes[1:]]
