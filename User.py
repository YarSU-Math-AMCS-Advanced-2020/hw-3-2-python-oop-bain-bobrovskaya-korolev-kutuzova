from Address import Address


class User:
    """
    Container base class for users in this application

    Attributes
    ----------
    login : str
    password : str
    name : str
    email : str
    phone_number : str
    address : Address or dict of str
        dict of str must be compatible with call Address(**address)
    """

    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address: dict or Address):
        self.login = login
        self.password = password
        self.name = name
        self.email = email
        self.phone_number = phone_number
        if isinstance(address, Address):
            self.address = address
        else:
            self.address = Address(**address)

    def __str__(self) -> str:
        return self.login
