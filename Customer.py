from typing import List

import Product
from Addres import Addres
from DeliveryStrategy import DeliveryStrategy
from Order import Order
from User import User


class Customer(User):
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, addres: Addres):
        super().__init__(login, password, name, email, phone_number, addres)

    def make_order(self, composition: List[Product], payment_method: str,
                   delivery: DeliveryStrategy):
        Order(self, composition,
              self.addres, payment_method,
              delivery, 'in processing')
