from Addres import Addres
from AddresDBRequests import AddresDBRequests


class User:
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, addres_idx: str,
                 addres_db: AddresDBRequests):
        self.__login = login
        self.__password = password
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__addres = Addres(*addres_db.get_note(addres_idx)[:7], addres_db,
                               addres_db.get_note(addres_idx)[-1])
        self.__addres_idx = addres_idx

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
    def addres(self):
        return self.__addres_idx

    @addres.setter
    def addres(self, addres: int):
        self.__addres = addres

    @property
    def addres_idx(self):
        return self.__addres_idx

    @addres_idx.setter
    def addres_idx(self, addres_idx: int):
        self.__addres_idx = addres_idx
