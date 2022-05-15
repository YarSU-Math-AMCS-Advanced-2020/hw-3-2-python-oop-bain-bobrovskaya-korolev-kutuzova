from Addres import Addres
from User import User


class Seller(User):
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, addres: Addres,
                 main_category: str):
        super().__init__(login, password, name, email, phone_number, addres)
        self.__main_category = main_category
        self.__rating = 0
        self.__total_assessments = 0

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
