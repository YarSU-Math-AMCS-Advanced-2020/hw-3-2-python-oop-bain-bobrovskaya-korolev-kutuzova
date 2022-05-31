from User import User


class Customer(User):
    """
    Container class for customer user information
    """
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address: dict, idx: str):
        super().__init__(login, password, name, email, phone_number,
                         address)
        self.idx = idx
