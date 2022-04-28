from DBRequests import DBRequests


class ProductDBRequests(DBRequests):
    """Class is used to work with products database requests

    Parameters
    ----------
    __db_cols : list
        Product database columns
    """
    __db_cols = ['seller', 'name', 'price', 'description',
                 'characteristics', 'category', 'total_quantity',
                 'rating', 'total_assessments', 'idx']

    def __init__(self, db_name='ProductDatabase.txt'):
        super().__init__(db_name, self.__db_cols)
