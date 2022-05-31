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
        self.db_name = db_name
        self.db_cols = db_cols

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

    def field_index(self, field_name: str) -> int:
        """
        Get column number of the field_name.
        """
        return self.db_cols.index(field_name)

    def is_there_by(self, field_name: str, field_value: str) -> bool:
        """
        Check if the object with ``field_name`` equal to ``field_value`` presents in database.
        """
        if field_name not in self.db_cols:
            raise ValueError('The field_name must be defined')

        field_index = self.field_index(field_name)

        with open(self.db_name, 'r') as db_file:
            note = db_file.readline()
            while note and note[:-1].split(';')[field_index] != field_value:
                note = db_file.readline()

        return bool(note)

    def is_there(self, idx: str) -> bool:
        return self.is_there_by('idx', idx)

    def unique(self, field_name: str) -> list:
        """
        Make list of unique values across the column ``field_name``
        """
        idx = self.field_index(field_name)
        u = set()
        for note in self.get_all_notes():
            u.add(note[idx])
        return list(u)

    def is_suit_elem(self, elem) -> bool:
        """
        Checks if this element matches database columns

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
        return Utils.get_clear_attr_names(elem) == self.db_cols

    def add_note(self, elem) -> None:
        """
        Adds note to database

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
        self.del_note_by('idx', idx)

    def del_note_by(self, field_name: str, field_value: str) -> None:
        """Deleting a note from the database

        Deleting a note with the specified index from the database
        If the index is not in the database, then nothing happens
        """

        if field_name not in self.db_cols:
            raise ValueError('The field_name must be defined')

        field_index = self.field_index(field_name)

        with open(self.db_name, 'r') as db_file:
            all_notes = [note[:-1].split(';') for note in db_file.readlines()]
        with open(self.db_name, 'w') as db_file:
            for note in all_notes:
                if note[field_index] != field_value:
                    db_file.write(';'.join(note))
                    db_file.write('\n')

    def get_note(self, idx: str) -> list or None:
        return self.get_note_by('idx', idx)

    def get_note_by(self, field_name: str, field_value: str) -> list or None:
        """
        Form list of attributes for the object in database with first ``field_name`` field equal to ``field_value``.

        Parameters
        ----------
        field_name : str
        field_value : str

        Returns
        -------
        list of attributes required to form a class instance for stored object
        """
        if field_name not in self.db_cols:
            raise ValueError('The field_name must be defined')

        field_index = self.field_index(field_name)

        with open(self.db_name, 'r') as db_file:
            note = db_file.readline()
            while note and note[:-1].split(';')[field_index] != field_value:
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
        Update ``elem`` in database

        The function finds entry in database with the same idx field, and updates it with ``elem``
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
        with open(self.db_name, 'r') as db_file:
            notes = db_file.readlines()
        return [note[:-1].split(';') for note in notes[1:]]
