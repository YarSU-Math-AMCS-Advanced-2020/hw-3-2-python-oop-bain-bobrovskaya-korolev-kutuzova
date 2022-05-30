from DBRequests import DBRequests
from Product import Product


class ProductDBRequests(DBRequests):
    """Class is used to work with products database requests

    Parameters
    ----------
    db_cols : list
        Product database columns
    """

    db_cols = list(Product.__init__.__code__.co_varnames[1:])

    def __init__(self, db_name='ProductDatabase.txt'):
        super().__init__(db_name, self.db_cols)


