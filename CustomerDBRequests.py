from DBRequests import DBRequests


class CustomerDBRequests(DBRequests):
    """Class is used to work with products database requests

    Parameters
    ----------
    __db_cols : list
        Customer database columns
    """
    __db_cols = ['login', 'password', 'name', 'email',
                 'phone_number', 'addres', 'addres_idx', 'idx']

    def __init__(self, db_name='CustomerDatabase.txt'):
        super().__init__(db_name, self.__db_cols)
