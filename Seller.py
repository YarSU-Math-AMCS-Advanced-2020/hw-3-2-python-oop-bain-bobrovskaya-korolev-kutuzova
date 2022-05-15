from Addres import Addres
from User import User
# from AddresDBRequests import AddresDBRequests
# from SellerDBRequests import SellerDBRequests


class Seller(User):
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, addres_idx: str,
                 main_category: str, addres_db,
                 seller_db, idx=None):
        super().__init__(login, password, name, email, phone_number,
                         addres_idx, addres_db)
        self.__main_category = main_category
        self.__rating = 0
        self.__total_assessments = 0
        self.__idx = idx
        if idx is None:
            seller_db.add_note(self)

    def __str__(self):
        return self.login

    @property
    def main_category(self):
        return self.__main_category

    @main_category.setter
    def main_category(self, main_category: str):
        self.__main_category = main_category

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating: str):
        self.__rating = rating

    @property
    def total_assessments(self):
        return self.__total_assessments

    @total_assessments.setter
    def total_assessments(self, total_assessments: str):
        self.__total_assessments = total_assessments

    @property
    def idx(self):
        return self.__idx

    @idx.setter
    def idx(self, idx: str):
        self.__idx = idx
