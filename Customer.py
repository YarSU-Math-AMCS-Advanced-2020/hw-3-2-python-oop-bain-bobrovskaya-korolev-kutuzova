from typing import List

import Product
from Addres import Addres
from DeliveryStrategy import DeliveryStrategy
from Order import Order
from User import User
from AddresDBRequests import AddresDBRequests
from CustomerDBRequests import CustomerDBRequests


class Customer(User):
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, addres_idx: str,
                 addres_db: AddresDBRequests, customer_db: CustomerDBRequests,
                 idx: str =None):
        super().__init__(login, password, name, email, phone_number,
                         addres_idx, addres_db)
        self.__idx = idx
        if idx is None:
            customer_db.add_note(self)


    def make_order(self, composition: List[Product], payment_method: str,
                   delivery: DeliveryStrategy):
        Order(self, composition,
              self.addres, payment_method,
              delivery, 'in processing')

    @property
    def idx(self):
        return self.__idx

    @idx.setter
    def idx(self, idx: str):
        self.__idx = idx
