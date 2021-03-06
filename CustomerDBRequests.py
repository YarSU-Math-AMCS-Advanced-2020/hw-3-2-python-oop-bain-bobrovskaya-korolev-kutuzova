from DBRequests import DBRequests
from Customer import Customer


class CustomerDBRequests(DBRequests):
    """
        Class that is used to work with customer database requests

        Attributes and methods are inherited from DBRequests.
        But db_cols is fixed to Customer attributes
    """

    # generate database columns from Customers.__init__ arguments list (except 'self')
    db_cols = list(Customer.__init__.__code__.co_varnames[1:])

    def __init__(self, db_name='CustomerDatabase.txt'):
        super().__init__(db_name, self.db_cols)

    def get_note_by_login(self, login: str) -> list or None:
        return self.get_note_by('login', login)
