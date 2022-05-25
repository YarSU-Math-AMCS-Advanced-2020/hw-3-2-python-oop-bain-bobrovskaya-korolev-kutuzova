from Address import Address
from AddressDBRequests import AddressDBRequests


class User:
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address_idx: str,
                 address_db: AddressDBRequests):
        self.login = login
        self.password = password
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = Address(*address_db.get_note(address_idx)[:7], address_db,
                                 address_db.get_note(address_idx)[-1])
        self.address_idx = address_idx


