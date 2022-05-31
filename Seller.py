from User import User


class Seller(User):
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address: dict,
                 main_category: str, rating: float, total_assessments: int,
                 idx: str):
        super().__init__(login, password, name, email, phone_number,
                         address)
        self.main_category = main_category
        self.rating = rating
        self.total_assessments = total_assessments
        self.idx = idx
