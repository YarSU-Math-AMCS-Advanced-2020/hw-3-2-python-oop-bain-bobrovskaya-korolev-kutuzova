from typing import Dict
from User import User
from Address import Address


class Customer(User):
    """
    Container class for customers

    Attributes
    ----------
    login : str
    password : str
    name : str
    email : str
    phone_number : str
    address : Address or dict of str
        dict of str must be compatible with call Address(**address)
    idx : str
        its unique identifier in the database
    """

    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address: Dict[str, str] or Address, idx: str):
        super().__init__(login, password, name, email, phone_number,
                         address)
        self.idx = idx
