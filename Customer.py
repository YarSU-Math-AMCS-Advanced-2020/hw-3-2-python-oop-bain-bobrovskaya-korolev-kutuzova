from typing import List

from Product import Product
from DeliveryStrategy import DeliveryStrategy
from Order import Order
from User import User
from AddressDBRequests import AddressDBRequests
from CustomerDBRequests import CustomerDBRequests


class Customer(User):
    def __init__(self, login: str, password: str, name: str, email: str,
                 phone_number: str, address_idx: str,
                 address_db: AddressDBRequests, customer_db: CustomerDBRequests,
                 idx: str = None):
        super().__init__(login, password, name, email, phone_number,
                         address_idx, address_db)
        self.__idx = idx
        if idx is None:
            if customer_db.check_similar_login(login):
                raise AttributeError('Customer already exist')
            customer_db.add_note(self)

    def make_order(self, composition: List[Product], payment_method: str,
                   delivery: DeliveryStrategy):
        return Order(self.login, composition,
                     self.address, payment_method,
                     delivery, 'in processing')

    @property
    def idx(self):
        return self.__idx

    @idx.setter
    def idx(self, idx: str):
        self.__idx = idx


def create_customer(address_idx, address_db: AddressDBRequests,
                    customer_db: CustomerDBRequests):
    login = input('Input login for account: ')
    password = input('Input password for account: ')
    name = input('Input name for account: ')
    email = input('Input email for account: ')
    phone_number = input('Input phone number for account: ')
    return Customer(login, password, name, email, phone_number, address_idx,
                    address_db, customer_db)
