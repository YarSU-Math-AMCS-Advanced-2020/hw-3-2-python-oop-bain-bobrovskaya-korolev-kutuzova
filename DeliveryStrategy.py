from typing import Dict, List, Tuple
from abc import ABC, abstractmethod
from enum import Enum, auto
from Address import Address
from Product import Product

class DELIVERY(Enum):
    YANDEX = 1
    SBER = 2
    POST = 3

# accessing the delivery system
class DeliveryStrategy(ABC):
    def __init__(self, product_dict: Dict[Address, List[Tuple[Product, int]]], destination: Address):
        self.product_dict = product_dict
        self.destination = destination

    @abstractmethod
    def price(self) -> float:
        """
        Returns
        -------
        float
            price of delivery based on delivery information
        """
        pass


class YandexDelivery(DeliveryStrategy):
    def __init__(self, product_dict: Dict[Address, List[Tuple[Product, int]]], destination: Address):
        super().__init__(product_dict, destination)

    def price(self) -> float:
        """
        Returns
        -------
        float
            price of delivery based on delivery information
        """
        return 150. * len(self.product_dict)


class SberDelivery(DeliveryStrategy):

    def __init__(self, product_dict: Dict[Address, List[Tuple[Product, int]]], destination: Address):
        super().__init__(product_dict, destination)

    def price(self) -> float:
        """
        Returns
        -------
        float
            price of delivery based on delivery information
        """
        return 300. * len(self.product_dict) ** 0.5


class PostDelivery(DeliveryStrategy):
    def __init__(self, product_dict: Dict[Address, List[Tuple[Product, int]]], destination: Address):
        super().__init__(product_dict, destination)

    def price(self) -> float:
        """
        Returns
        -------
        float
            price of delivery based on delivery information
        """
        return 100. * len(self.product_dict) ** 2


def choose_delivery(delivery_company: DELIVERY) -> YandexDelivery or SberDelivery or PostDelivery:
    """
    Select delivery strategy by its name
    """
    if delivery_company == DELIVERY.YANDEX:
        return YandexDelivery
    elif delivery_company == DELIVERY.SBER:
        return SberDelivery
    elif delivery_company == DELIVERY.POST:
        return PostDelivery
    else:
        raise ValueError("Wrong delivery name")
