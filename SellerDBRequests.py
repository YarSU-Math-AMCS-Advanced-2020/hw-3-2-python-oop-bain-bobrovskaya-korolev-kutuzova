from DBRequests import DBRequests
from Seller import Seller


class SellerDBRequests(DBRequests):
    """
    Class that is used to work with seller database requests

    Attributes and methods are inherited from DBRequests.
    But db_cols is fixed to Seller attributes
    """

    # generate database columns from Seller.__init__ arguments list (excluding 'self')
    db_cols = list(Seller.__init__.__code__.co_varnames[1:])

    def __init__(self, db_name: str = 'SellerDatabase.txt'):
        super().__init__(db_name, self.db_cols)

    def get_note_by_login(self, login: str) -> list or None:
        return self.get_note_by('login', login)
