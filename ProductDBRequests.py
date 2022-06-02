from DBRequests import DBRequests
from Product import Product


class ProductDBRequests(DBRequests):
    """
    Class that is used to work with products database requests

    Attributes and methods are inherited from DBRequests.
    But db_cols is fixed to Product attributes
    """

    # generate database columns from Product.__init__ arguments list (except 'self')
    db_cols = list(Product.__init__.__code__.co_varnames[1:])

    def __init__(self, db_name: str = 'ProductDatabase.txt'):
        super().__init__(db_name, self.db_cols)
