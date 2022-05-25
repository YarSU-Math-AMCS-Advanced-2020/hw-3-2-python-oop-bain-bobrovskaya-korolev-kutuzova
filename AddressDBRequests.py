from DBRequests import DBRequests


class AddressDBRequests(DBRequests):
    """Class is used to work with products database requests

    Parameters
    ----------
    __db_cols : list
        Address database columns
    """
    __db_cols = ['country', 'region', 'locality', 'street',
                 'index', 'house', 'flat', 'idx']

    def __init__(self, db_name='AddressDatabase.txt'):
        super().__init__(db_name, self.__db_cols)
