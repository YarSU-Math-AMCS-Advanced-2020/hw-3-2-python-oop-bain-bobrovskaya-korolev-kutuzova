from Address import Address
from User import User
from AddressDBRequests import AddressDBRequests
from SellerDBRequests import SellerDBRequests


class Seller(User):
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address_idx: str,
                 main_category: str, rating=0, total_assessments=0,
                 address_db: AddressDBRequests = None,
                 seller_db: SellerDBRequests = None,
                 idx=None):
        super().__init__(login, password, name, email, phone_number,
                         address_idx, address_db)
        self.main_category = main_category
        self.rating = rating
        self.total_assessments = total_assessments
        self.idx = idx
        if idx is None:
            if seller_db.check_similar_login(login):
                raise AttributeError('Seller already exist')
            seller_db.add_note(self)

    def __str__(self):
        return self.login


def create_seller(address_idx: str, address_db: AddressDBRequests = None,
                  seller_db: SellerDBRequests = None):
    login = input('Input login for account: ')
    password = input('Input password for account: ')
    name = input('Input name for account: ')
    email = input('Input email for account: ')
    phone_number = input('Input phone number for account: ')
    main_category = input('Input main category for account')
    return Seller(login, password, name, email, phone_number, address_idx,
                  main_category, address_db=address_db, seller_db=seller_db)
