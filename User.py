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
    address : dict of str
        must be compatible with call Address(**address)
    """
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address: dict):
        self.login = login
        self.password = password
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def __str__(self) -> str:
        return self.login
