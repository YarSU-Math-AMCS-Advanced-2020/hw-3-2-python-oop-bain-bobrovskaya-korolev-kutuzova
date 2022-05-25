from DBRequests import DBRequests


class SellerDBRequests(DBRequests):
    """Class is used to work with products database requests

    Parameters
    ----------
    db_cols : list
        Seller database columns
    """
    db_cols = ['User__login', 'User__password', 'User__name', 'User__email',
               'User__phone_number', 'User__address', 'User__address_idx',
               'main_category', 'rating', 'total_assessments', 'idx']

    def __init__(self, db_name='SellerDatabase.txt'):
        super().__init__(db_name, self.db_cols)

    def get_note_by_login(self, login: str):
        with open(self.db_name, 'r') as db_file:
            note = db_file.readline()
            not_eof = True
            login_pos_cols = self.db_cols.index('User__login')
            while not_eof and note[:-1].split(';')[login_pos_cols] != login:
                note = db_file.readline()
                if not note:
                    not_eof = False
        if not_eof:
            # We separate the last character because it's '\n'
            cor_note = []
            for elem in note[:-1].split(';'):
                if elem.isdigit():
                    cor_note.append(int(elem))
                else:
                    cor_note.append(elem)
            return cor_note
        else:
            return []

    def check_similar_login(self, login: str):
        return len(self.get_note_by_login(login)) != 0
