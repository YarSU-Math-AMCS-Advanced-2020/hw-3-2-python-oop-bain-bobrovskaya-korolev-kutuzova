from DBRequests import DBRequests


class SellerDBRequests(DBRequests):
    """Class is used to work with products database requests

    Parameters
    ----------
    __db_cols : list
        Seller database columns
    """
    __db_cols = ['User__login', 'User__password', 'User__name', 'User__email',
                 'User__phone_number', 'User__addres', 'User__addres_idx',
                 'main_category', 'rating', 'total_assessments', 'idx']

    def __init__(self, db_name='SellerDatabase.txt'):
        super().__init__(db_name, self.__db_cols)
