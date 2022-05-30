from DBRequests import DBRequests
from Seller import Seller


class SellerDBRequests(DBRequests):
    """Class is used to work with products database requests

    Parameters
    ----------
    db_cols : list
        Seller database columns
    """
    # generate database columns from Customers.__init__ arguments list (excluding 'self')
    db_cols = list(Seller.__init__.__code__.co_varnames[1:])

    def __init__(self, db_name='SellerDatabase.txt'):
        super().__init__(db_name, self.db_cols)

    def get_note_by_login(self, login: str) -> list or None:
        return self.get_note_by('login', login)

    def check_similar_login(self, login: str):
        return len(self.get_note_by_login(login)) != 0
