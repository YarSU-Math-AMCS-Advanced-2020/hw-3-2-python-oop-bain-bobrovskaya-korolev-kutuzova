class Seller():
    def __init__(self, name: str, email: str, phone_number: str, city: str,
                 main_category: str):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__city = city
        self.__main_category = main_category
        self.__rating = 0
        self.__total_assessments = 0

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
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

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
