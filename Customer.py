from User import User


class Customer(User):
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, city: str):
        super().__init__(login, password, name, email, phone_number, city)
