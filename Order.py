from typing import List

from Addres import Addres
from Product import Product


class Order:
    # the class of the strategy we need is passed to the constructor
    def __init__(self, customer: str, composition: List[Product],
                 destination: Addres, payment_method: str,
                 delivery, status: str):
        self.__customer = customer
        self.__composition = composition
        self.__total_price = 0
        for product in composition:
            self.__total_price += product.price
        self.__destination = destination
        self.__payment_method = payment_method
        product_dict = {}
        for i in composition:
            if i.seller.addres in product_dict.keys():
                product_dict[i.seller.addres].append(i)
            else:
                product_dict[i.seller.addres] = [i]
        self.__delivery = delivery(product_dict, destination)
        self.__total_price += self.__delivery.price()
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
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, payment_method: str):
        self.__payment_method = payment_method

    @property
    def delivery(self):
        return self.__delivery

    @delivery.setter
    def delivery(self, delivery: str):
        self.__delivery = delivery

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: int):
        self.__status = status
