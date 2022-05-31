from User import User


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
    address : dict of str
        must be compatible with call Address(**address)
    idx : str
        its unique identifier in the database
    """
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address: dict, idx: str):
        super().__init__(login, password, name, email, phone_number,
                         address)
        self.idx = idx
