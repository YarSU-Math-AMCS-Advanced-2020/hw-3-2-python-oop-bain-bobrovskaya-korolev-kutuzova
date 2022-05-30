from Address import Address
from enum import Enum, auto


class OrderStatus(Enum):
    IN_PROGRESS = auto()
    DELIVERING = auto()
    COMPLETED = auto()


class Order:
    # the class of the strategy we need is passed to the constructor
    def __init__(self, customer: str, composition: list,
                 destination: Address, payment_method: str,
                 delivery, status: OrderStatus):
        self.customer = customer
        self.composition = composition.copy()
        self.total_price = 0
        for product, quantity, address in composition:
            self.total_price += product.price * quantity
        self.destination = destination
        self.payment_method = payment_method
        product_dict = {}
        for product, quantity, address in composition:
            if address in product_dict.keys():
                product_dict[address].append((product, quantity))
            else:
                product_dict[address] = [(product, quantity)]
        self.delivery = delivery(product_dict, destination)
        self.total_price += self.delivery.price()
        self.status = status
