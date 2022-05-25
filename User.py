from Address import Address
from AddressDBRequests import AddressDBRequests


class User:
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address_idx: str,
                 address_db: AddressDBRequests):
        self.__login = login
        self.__password = password
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = Address(*address_db.get_note(address_idx)[:7], address_db,
                                 address_db.get_note(address_idx)[-1])
        self.__address_idx = address_idx

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    @property
    def address(self):
        return self.__address_idx

    @address.setter
    def address(self, address: int):
        self.__address = address

    @property
    def address_idx(self):
        return self.__address_idx

    @address_idx.setter
    def address_idx(self, address_idx: int):
        self.__address_idx = address_idx
