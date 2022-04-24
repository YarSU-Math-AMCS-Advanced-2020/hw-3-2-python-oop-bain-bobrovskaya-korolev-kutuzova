from Customer import Customer
from Addres import Addres


class Order():
    def __init__(self, customer: Customer, total_price: int, composition: list, destination: Addres,
                 place_of_departure: Addres, payment_method: str, status: str):
        self.__customer = customer
        self.__total_price = total_price
        self.__composition = composition
        self.__destination = destination
        self.__place_of_departure = place_of_departure
        self.__payment_method = payment_method
        self.__status = status

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer: str):
        self.__customer = customer

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: str):
        self.__total_price = total_price

    @property
    def composition(self):
        return self.__composition

    @composition.setter
    def composition(self, composition: int):
        self.__composition = composition

    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination

    @property
    def place_of_departure(self):
        return self.__place_of_departure

    @place_of_departure.setter
    def place_of_departure(self, place_of_departure: dict):
        self.__place_of_departure = place_of_departure

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, payment_method: str):
        self.__payment_method = payment_method

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status
