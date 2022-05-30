from typing import List

from Product import Product
from DeliveryStrategy import DeliveryStrategy
from Order import Order
from User import User


class Customer(User):
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address: dict, idx: str):
        super().__init__(login, password, name, email, phone_number,
                         address)
        self.idx = idx

