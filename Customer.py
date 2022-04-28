class Customer():
    def __init__(self, name: str, email: str, phone_number: str, city: str):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__city = city

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
