from typing import List

from Address import Address
from Product import Product


class Order:
    # the class of the strategy we need is passed to the constructor
    def __init__(self, customer: str, composition: List[Product],
                 destination: Address, payment_method: str,
                 delivery, status: str):
        self.customer = customer
        self.composition = composition
        self.total_price = 0
        for product in composition:
            self.total_price += product.price
        self.destination = destination
        self.payment_method = payment_method
        product_dict = {}
        for i in composition:
            if i.seller.address in product_dict.keys():
                product_dict[i.seller.address].append(i)
            else:
                product_dict[i.seller.address] = [i]
        self.delivery = delivery(product_dict, destination)
        self.total_price += self.delivery.price()
        self.status = status
