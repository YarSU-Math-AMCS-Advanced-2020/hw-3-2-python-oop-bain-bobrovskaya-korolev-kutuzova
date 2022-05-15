from typing import Dict, List

from Addres import Addres
from Product import Product

yandex_price = 150
sber_price = 200
post_price = 100


# accessing the delivery system
class DeliveryStrategy:
    def __init__(self, product_dict: Dict[Addres, List[Product]], destination: Addres):
        pass

    def price(self) -> int:
        pass


class YandexDelivery(DeliveryStrategy):
    def __init__(self, product_dict: Dict[Addres, List[Product]], destination: Addres):
        super().__init__(product_dict, destination)

    def price(self) -> int:
        return yandex_price


class SberDelivery(DeliveryStrategy):
    def __init__(self, product_dict: Dict[Addres, List[Product]], destination: Addres):
        super().__init__(product_dict, destination)

    def price(self) -> int:
        return sber_price


class PostDelivery(DeliveryStrategy):
    def __init__(self, product_dict: Dict[Addres, List[Product]], destination: Addres):
        super().__init__(product_dict, destination)

    def price(self) -> int:
        return post_price
